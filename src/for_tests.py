import tkinter as tk
from tkinter import ttk, messagebox
from utils.database import Database
from utils.register_verify import register

db = Database()

#print(register('usuarinhoteste2@gmail.com', "usuarinhoteste2", "123", "123", "123123", "30", "30")) # False

#db.insert_user("teste@gmail.com", "Teste", "123", "anyhash", "anyphone")
#db.insert_user("namorandinha@gmail.com", "Namorandinha", "password123", "anyhash", "anyphone")
#db.insert_user("namorandinho@gmail.com", "Namorandinho", "password321", "anyhash", "anyphone")
#print(db.list_users())


#db.send_message("teste", "namorandinha@gmail.com", "oassi")
#db.send_message("namorandinho@gmail.com", "teste", "Ola teste") #parametros: Email remetente, Email destinatrio, mensagem | Envia uma mensagem para um email
#print(db.list_chats("teste@gmail.com"))
#print(db.list_chats("namorandinha@gmail.com"))  #parametros: Email | Lista todos os chats que o usuario tem (um chat é adicionado quando recebe ou envia uma mensagem) | Retorna: [[1, 'namorandinha@gmail.com'], [2, 'destinatario@example.com'], [3, 'namorandinho@gmail.com']] | Uma lista com o id do chat e o email de quem enviou a mensagem
#print(db.list_messages_from_chat(1)) parametros: ID do chat | Lista todos os chats iniciados e pega todas as mensagens de um chat pelo ID
#print(db.list_chats("teste"))
#print(db.list_chats("teste2@gmail.com"))
#print(db.list_messages_from_chat(1))
#print(db.list_messages_from_chat_original(1))
#print(db.list_messages_from_chat_original(2))
