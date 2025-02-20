# Sistema de Segurança para Comunicação Interna 🔒💬

## Descrição do Projeto

Este projeto tem como objetivo garantir a **segurança da comunicação** entre os funcionários de uma empresa, protegendo dados sensíveis e credenciais contra acessos não autorizados. Nossa equipe ficou responsável por desenvolver e implementar os módulos de **autenticação** e **criptografia** no sistema da empresa.

O foco da implementação será:

- 🔐**Proteção de credenciais dos usuários** : Implementação de **hashing seguro de senhas** utilizando o **bcrypt**.
- 🛡️**Autenticação via Tokens JWT** : Geração e verificação de **tokens JWT** para garantir que apenas usuários autenticados possam acessar recursos protegidos.
- ✉️🔒**Criptografia de mensagens** : Uso do algoritmo **AES** para criptografar as mensagens sensíveis trocadas entre os funcionários.
- 🔑**Proteção da chave de criptografia** : A chave AES será protegida utilizando **RSA**, garantindo que só o destinatário correto possa descriptografá-la.

Este sistema irá proporcionar um ambiente mais seguro e confiável para a comunicação e o armazenamento de dados sensíveis dentro da organização.
