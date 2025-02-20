# Documento de Funcionalidades do Sistema

## O que o sistema faz?

Este sistema foi desenvolvido para garantir a **segurança da comunicação** entre os usuários. Aqui está como ele funciona:

- **Cadastro de usuário** 📝: Quando um novo usuário se cadastra, a senha dele é protegida com **bcrypt** antes de ser armazenada, garantindo que a senha não seja salva em texto simples.
  
- **Login** 🔑: Ao fazer login, se a senha fornecida estiver correta, o sistema gera um **Token JWT**. Esse token será usado para autenticar o usuário nas próximas ações.

- **Enviar mensagem** ✉️🔒: Quando um usuário envia uma mensagem, ela é **criptografada** com **AES** (uma chave simétrica) antes de ser salva no sistema, garantindo que ninguém além do destinatário possa ler.

- **Receber mensagem** 🔓: Quando o destinatário recebe a mensagem, ele **descriptografa** a chave AES com a chave **RSA** (criptografia assimétrica), podendo então acessar o conteúdo da mensagem de forma segura.

---

Este sistema assegura que todas as informações e comunicações entre os usuários sejam protegidas e privadas, utilizando tecnologias modernas de **hashing**, **criptografia** e **autenticação**. 😎🔐
