# Documentação da Proposta de Implementação do Sistema

## 🎯 Objetivo
Este projeto visa melhorar a segurança na comunicação corporativa, prevenindo acessos indevidos a mensagens sigilosas.

## 🛠️ Tecnologias Utilizadas

- 🔒 **bcrypt** → Versão: **3.2.1**  
  Usado para realizar o **hashing seguro de senhas**, garantindo que as senhas não sejam armazenadas em texto simples.

- 🔑 **PyJWT** → Versão: **2.6.1**  
  Utilizado para **autenticação confiável via tokens JWT**, permitindo uma comunicação segura sem a necessidade de manter sessões no servidor.

- 🔐 **cryptography** → Versão: **38.0.1**  
  Responsável pela **criptografia de dados utilizando AES e RSA**, garantindo a segurança das mensagens e proteção das chaves de criptografia.

## 📌 Uso das Tecnologias e suas funções no nosso projeto

### 1. bcrypt: Hashing Seguro de Senhas 🔐

#### Objetivo:
O `bcrypt` é utilizado para realizar o **hashing** seguro de senhas, garantindo que as senhas dos usuários não sejam armazenadas em texto simples.

#### Como será utilizado:
- **Geração de Hash**: Ao cadastrar uma senha, o `bcrypt` gera um hash único e irreversível utilizando um salt (valor aleatório).
- **Verificação**: Durante o login, a senha fornecida é comparada com o hash armazenado para autenticar o usuário.

---

### 2. PyJWT: Autenticação via Tokens JWT 🔑

#### Objetivo:
O `PyJWT` será utilizado para implementar autenticação por meio de **Tokens JWT**, permitindo uma comunicação segura sem a necessidade de manter sessões no servidor.

#### Como será utilizado:
- **Geração de Token**: Quando o usuário faz login, um token JWT é gerado com informações do usuário e um tempo de expiração.
- **Validação de Token**: O token será enviado nas requisições subsequentes para validar a autenticidade do usuário e conceder acesso aos recursos protegidos.

---

### 3. cryptography: Implementação de AES e RSA 🔒

#### Objetivo:
A biblioteca `cryptography` será utilizada para implementar **criptografia simétrica** (AES) e **criptografia assimétrica** (RSA), garantindo a proteção de dados sensíveis.

#### Como será utilizado:

##### AES (Criptografia Simétrica)
- **Criptografia**: Utiliza uma chave única para criptografar e descriptografar dados.
  
##### RSA (Criptografia Assimétrica)
- **Criptografia**: Utiliza um par de chaves, pública para criptografar e privada para descriptografar dados, permitindo a troca segura de informações.

---

## 🔄 Funcionamento do Sistema

### 1. 👤 **Cadastro de Usuário**
- O sistema verifica se o usuário já está cadastrado.
- Se não estiver, os dados são criptografados antes de serem armazenados no banco de dados.

### 2. 🔑 **Login**
- Durante o login, será **verificado** se os dados do usuário estão corretos.
- Se forem, um **Token JWT** será gerado e utilizado para autenticação nas requisições subsequentes.

### 3. ✉️ **Envio de Mensagens**
- O sistema segue os seguintes passos:
  - A mensagem é criptografada com **AES** antes de ser enviada.
  - Se necessário, a mensagem pode ser criptografada com a chave do usuário antes do armazenamento.
  - A mensagem criptografada é então enviada para o banco de dados.

### 4. 🔓 **Recebimento de Mensagens**
- Para garantir o acesso seguro:
  - A mensagem criptografada é recuperada do banco.
  - Se necessário, ela é primeiro descriptografada com a chave do usuário.
  - A chave AES da mensagem é descriptografada com a chave RSA do destinatário.
  - O destinatário pode então acessar a mensagem de forma segura.

---

## 🔐 Explicação Sobre Armazenamento Seguro de Dados

### Objetivo:
Garantir que os dados sensíveis, como senhas e informações pessoais, sejam armazenados de maneira protegida e que, mesmo em caso de vazamento, esses dados não possam ser facilmente acessados ou utilizados.

### Estratégias de Armazenamento Seguro:
1. **Hashing de Senhas**: 
   - **bcrypt** é utilizado para hashear as senhas antes de armazená-las. Como o hashing é irreversível, mesmo que o banco de dados seja comprometido, as senhas não podem ser recuperadas.

2. **Criptografia de Dados Sensíveis**: 
   - Dados como mensagens ou informações confidenciais são **criptografados** usando **AES**, garantindo que, caso sejam acessados indevidamente, permaneçam ilegíveis sem a chave de descriptografia correta.

3. **Proteção de Chaves**:
   - A chave AES usada para criptografar dados sensíveis é protegida com criptografia **RSA**. Isso impede que a chave seja acessada por usuários não autorizados, aumentando a segurança do armazenamento.

4. **Uso de Salt**:
   - Ao gerar o hash de senhas com **bcrypt**, é utilizado um **salt** (valor aleatório) para garantir que mesmo senhas iguais resultem em hashes diferentes, tornando os ataques de dicionário e de força bruta mais difíceis.

5. **Armazenamento Seguro da Chave Privada**:
   - A chave privada RSA, usada para descriptografar a chave AES, deve ser armazenada de forma segura, como em um ambiente seguro de gerenciamento de chaves ou dentro de hardware de segurança especializado (HSM).

### Benefícios:
- **Confidencialidade**: A criptografia assegura que dados sensíveis sejam acessíveis apenas por usuários autorizados.
- **Integridade**: O uso de hashes impede que os dados sejam alterados sem que isso seja detectado.
- **Segurança no Vazamento de Dados**: Mesmo que os dados sejam acessados sem autorização, eles permanecem protegidos devido à criptografia e hashing.

Essas práticas garantem que os dados sensíveis sejam protegidos durante o armazenamento, mantendo a privacidade e a segurança dos usuários.