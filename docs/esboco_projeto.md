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

1. 👤 **Registro de usuário** → Senha armazenada de forma segura com bcrypt.
2. 🔑 **Autenticação** → O login gera um token JWT para o usuário.
3. ✉️ **Envio de mensagens** → O conteúdo é protegido com criptografia AES.
4. 🔒 **Acesso restrito** → Apenas o destinatário autorizado pode descriptografar a mensagem com RSA.

