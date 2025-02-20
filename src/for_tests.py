import tkinter as tk
from tkinter import ttk, messagebox
from utils.database import Database

db = Database()

"""db.send_message("teste2@gmail.com", "teste3@gmail.com", "A mensagem deve estar criptografada")
print(db.list_chats("teste3@gmail.com"))
print(db.list_chats("teste2@gmail.com"))"""
print(db.list_messages_from_chat(1))
print(db.list_messages_from_chat_original(1))
