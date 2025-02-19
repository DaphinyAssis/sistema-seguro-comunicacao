# Proposta de Implementação do Sistema

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

