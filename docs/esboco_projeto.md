# Documento de Esboço do Projeto

## 🎯 Objetivo
Este projeto visa melhorar a segurança na comunicação corporativa, prevenindo acessos indevidos a mensagens sigilosas.

## 🛠️ Tecnologias Utilizadas

- 🔒 **bcrypt** → Versão: **3.2.1**  
  Usado para realizar o **hashing seguro de senhas**, garantindo que as senhas não sejam armazenadas em texto simples.

- 🔑 **PyJWT** → Versão: **2.6.1**  
  Utilizado para **autenticação confiável via tokens JWT**, permitindo uma comunicação segura sem a necessidade de manter sessões no servidor.

- 🔐 **cryptography** → Versão: **38.0.1**  
  Responsável pela **criptografia de dados utilizando AES e RSA**, garantindo a segurança das mensagens e proteção das chaves de criptografia.

## 🔄 Funcionamento do Sistema

1. 👤 **Registro de usuário** → O sistema verifica se o usuário já está cadastrado. Se não estiver, seus dados são criptografados antes de serem armazenados no banco.
2. 🔑 **Autenticação** → O login verifica se as credenciais são corretas. Se forem, um token JWT é gerado para autenticação.
3. ✉️ **Envio de mensagens** → O sistema segue os seguintes passos:
   - A mensagem é criptografada com **AES** antes de ser enviada.
   - Se necessário, a mensagem pode ser criptografada com a chave do usuário antes do armazenamento.
   - A mensagem criptografada é então enviada para o banco de dados.
4. 🔓 **Recebimento de mensagens** → Para garantir o acesso seguro:
   - A mensagem criptografada é recuperada do banco.
   - Se necessário, ela é primeiro descriptografada com a chave do usuário.
   - A chave AES da mensagem é descriptografada com a chave RSA do destinatário.
   - O destinatário pode então acessar a mensagem de forma segura.

