# Documento de Esboço do Projeto

## 🎯 Objetivo
Este projeto visa melhorar a segurança na comunicação corporativa, prevenindo acessos indevidos a mensagens sigilosas.

## 🛠️ Tecnologias Empregadas

- 🔒 **bcrypt** → Para armazenamento seguro de senhas.
- 🔑 **PyJWT** → Para autenticação confiável via tokens JWT.
- 🔐 **cryptography** → Para criptografia de dados utilizando AES e RSA.

## 🔄 Funcionamento do Sistema

1. 👤 **Registro de usuário** → Senha armazenada de forma segura com bcrypt.
2. 🔑 **Autenticação** → O login gera um token JWT para o usuário.
3. ✉️ **Envio de mensagens** → O conteúdo é protegido com criptografia AES.
4. 🏆 **Acesso restrito** → Apenas o destinatário autorizado pode descriptografar a mensagem com RSA.

