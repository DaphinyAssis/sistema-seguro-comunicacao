# Documento de Funcionalidades do Sistema

## O que o sistema faz?

Este sistema foi desenvolvido para garantir a **segurança da comunicação** entre os usuários. Aqui está como ele funciona:

- **Cadastro de usuário** 📝: Quando um novo usuário se cadastra, seus dados sensíveis são protegidos. A senha é protegida com **bcrypt**, enquanto outros dados são **criptografados** antes de serem armazenados no banco de dados.
  
- **Login** 🔑: O usuário informa suas credenciais, que são verificadas no banco de dados. Se estiverem corretas, o sistema gera um **Token JWT**, que será usado para autenticação em ações futuras. Se os dados forem incorretos, o login falha e o usuário deve tentar novamente.

- **Envio de mensagem** ✉️🔒: Quando um usuário envia uma mensagem, o sistema segue o seguinte fluxo:
  1. A mensagem é criptografada com **AES** (chave simétrica).
  2. Caso necessário, a mensagem também pode ser criptografada com a chave do usuário antes de ser armazenada no banco.
  3. A mensagem criptografada é enviada e salva no banco de dados.

- **Recebimento de mensagem** 🔓: Para garantir que apenas o destinatário possa ler a mensagem:
  1. O sistema recupera a mensagem criptografada do banco.
  2. Se necessário, ela é **descriptografada** primeiro com a chave do usuário.
  3. A chave **AES** da mensagem é então descriptografada com a chave **RSA** do destinatário.
  4. O destinatário pode então ler a mensagem de forma segura.

---

Este sistema assegura que todas as informações e comunicações entre os usuários sejam protegidas e privadas, utilizando tecnologias modernas de **hashing**, **criptografia** e **autenticação**. 😎🔐

