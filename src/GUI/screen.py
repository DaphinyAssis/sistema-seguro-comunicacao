import customtkinter as ctk
from tkinter import Tk, Label, Entry, Button
from utils.database import Database
from utils.login_verify import login
from utils.register_verify import register
import random

class Chat:
    def __init__(self, parent, chat, gui_instance):
        self.chat = chat
        self.id = chat[0]
        self.email = chat[1]
        self.gui_instance = gui_instance
        
        self.item_chat = ctk.CTkLabel(parent, text=self.email, width=280, height=50, fg_color="gray")
        self.item_chat.pack(pady=5, padx=10, fill='x')
        self.item_chat.bind("<Button-1>", self.on_click)
    
    def on_click(self, event):
        self.gui_instance.chat_id = self.id  # Armazena apenas o ID
        self.gui_instance.load_message_in_canvas()

class Phone:
    def __init__(self, window):
        self.window = window
        self.code = str(random.randint(111111,999999))
        self.modal = ctk.CTkToplevel(self.window)
        self.modal.geometry("400x300")
        self.modal.title("Phone")

    def get_code(self):
        return self.code
    
    def show_code(self):
        """Exibe um modal para adicionar um novo chat"""
        label_email = ctk.CTkLabel(self.modal, text=self.code)
        label_email.pack(pady=5)

class GInterface:
    def __init__(self):
        ctk.set_appearance_mode("light")
        self.window = ctk.CTk()
        self.db = Database()
        self.window.geometry('1280x720')
        self.window.title('Chat App')
        self.logged_email = ""  
        self.chat_id = None
        self.last_messages = []  

        #self.gui_login()
        self.gui_register()

        self.window.mainloop()

    def gui_register(self):
        try:
            self.login_page.destroy()
        except:
            pass
        #inicia celular phone = Phone()
        self.phone = Phone(self.window)

        self.register_page = ctk.CTkFrame(self.window, width=400, height=300)
        self.register_page.place(relx=0.5, rely=0.5, anchor="center")

        Label(self.register_page, text="E-mail").pack(pady=5)
        self.register_input_email = Entry(self.register_page, width=30)
        self.register_input_email.pack(pady=5)

        Label(self.register_page, text="Nome").pack(pady=5)
        self.register_input_name = Entry(self.register_page, width=30)
        self.register_input_name.pack(pady=5)

        Label(self.register_page, text="Senha").pack(pady=5)
        self.register_input_password = Entry(self.register_page, width=30)
        self.register_input_password.pack(pady=5)

        Label(self.register_page, text="Confirmar Senha").pack(pady=5)
        self.register_input_confirm_password = Entry(self.register_page, width=30)
        self.register_input_confirm_password.pack(pady=5)

        Label(self.register_page, text="Telefone").pack(pady=5)
        self.register_input_number = Entry(self.register_page, width=30)
        self.register_input_number.pack(pady=5)
        self.button_send_code = Button(
            self.register_page, 
            text='Enviar codigo', 
            command=lambda: self.phone.show_code()
        )
        self.button_send_code.pack(pady=20)

        Label(self.register_page, text="Codigo").pack(pady=5)
        self.register_input_code = Entry(self.register_page, width=30)
        self.register_input_code.pack(pady=5)

        self.button_register = Button(
            self.register_page, 
            text='Registrar', 
            command=lambda: self.register_load()
        )
        self.button_register.pack(pady=20)

        self.button_alredy_registred = Button(
            self.register_page, 
            text='Já tenho conta', 
            command=lambda: self.gui_login()
        )
        self.button_alredy_registred.pack(pady=20)

    def register_load(self):
        verify = register(self.register_input_email, self.register_input_name, self.register_input_password, self.register_input_confirm_password, self.register_input_number, self.register_input_code, self.phone.get_code())
        print(verify)
        if verify:
            self.gui_login()


    def gui_login(self):
        self.register_page.destroy()
        """Cria a tela de login"""
        self.login_page = ctk.CTkFrame(self.window, width=400, height=300)
        self.login_page.place(relx=0.5, rely=0.5, anchor="center")

        Label(self.login_page, text="E-mail").pack(pady=5)
        self.input_email = Entry(self.login_page, width=30)
        self.input_email.pack(pady=5)

        Label(self.login_page, text="Senha").pack(pady=5)
        self.input_password = Entry(self.login_page, width=30, show='*')
        self.input_password.pack(pady=5)

        self.button_login = Button(
            self.login_page, 
            text='Login', 
            command=lambda: self.logged_pages(self.input_email, self.input_password)
        )
        self.button_login.pack(pady=20)

        self.button_create_account = Button(
            self.login_page, 
            text='Criar uma conta', 
            command=lambda: self.gui_register()
        )
        self.button_create_account.pack(pady=20)

    def chat_frame(self):
        """Cria a barra lateral para chats"""
        self.component_chat_canvas = ctk.CTkScrollableFrame(self.window, width=300, height=680, fg_color='white')
        self.component_chat_canvas.place(x=0, y=0)
        self.load_chats()
    
    def load_chats(self):
        """Carrega os chats do usuário logado sem duplicar emails"""
        #print(f"Carregando chats para {self.logged_email}")  # Debug
        chats = self.db.list_chats(self.logged_email)
        #print("Chats encontrados:", chats)  # Debug

        # Limpa os widgets da lista antes de adicionar novos
        for widget in self.component_chat_canvas.winfo_children():
            widget.destroy()

        # Usa um conjunto para evitar emails duplicados
        emails_adicionados = set()

        for chat in chats:
            if chat[1] not in emails_adicionados:  # Verifica se o email já foi adicionado
                Chat(self.component_chat_canvas, chat, self)
                emails_adicionados.add(chat[1])  # Adiciona o email ao conjunto

    def message_frame(self):
        """Cria a área de mensagens"""
        self.component_message_canvas = ctk.CTkScrollableFrame(self.window, width=970, height=670, fg_color='white')
        self.component_message_canvas.place(x=305, y=0)

    def load_message_in_canvas(self, force_update=False):
        """Carrega as mensagens no chat"""
        if not self.chat_id:
            return  # Evita erro ao tentar carregar mensagens sem chat ativo

        #print(f"Atualizando mensagens para o chat: {self.chat_id}")  # Debug
        messages = self.db.list_messages_from_chat(self.chat_id)

        if not force_update and messages == self.last_messages:
            return

        self.last_messages = messages

        for widget in self.component_message_canvas.winfo_children():
            widget.destroy()

        for msg in messages:
            text = msg[1]
            align = "e" if msg[0] == self.logged_email else "w"
            color = "#D1E7DD" if msg[0] == self.logged_email else "#F8D7DA"

            label = ctk.CTkLabel(
                self.component_message_canvas, 
                text=text, 
                fg_color=color, 
                width=700, 
                corner_radius=5,
                wraplength=700  # Define o limite de quebra de linha
            )
            label.pack(pady=5, padx=10, anchor=align)

        self.window.after(100, lambda: self.component_message_canvas._parent_canvas.yview_moveto(1.0))
    
    def update_messages_loop(self):
        """Atualiza mensagens e chats a cada 2 segundos"""
        self.load_message_in_canvas(force_update=True)
        self.load_chats()  # Atualiza a lista de chats em tempo real
        self.window.after(2000, self.update_messages_loop)

    def input_send_message(self):
        """Cria o campo de entrada de mensagens"""
        self.component_input_send_message = ctk.CTkEntry(self.window, width=800, height=40)
        self.component_input_send_message.place(x=305, y=680)
    
    def button_send_message(self):
        """Cria o botão de envio de mensagens"""
        self.component_button_send_message = ctk.CTkButton(self.window, text='Enviar', command=self.send_message)
        self.component_button_send_message.place(x=1120, y=680)
    
    def button_create_chat(self):
        """Cria o botão para adicionar um novo chat"""
        self.component_button_create_chat = ctk.CTkButton(self.window, text='Adicionar Chat', command=self.show_chat_modal)
        self.component_button_create_chat.place(x=20, y=690)
    
    def send_message(self):
        """Envia uma mensagem no chat ativo"""
        if not self.chat_id:
            #print("Nenhum chat ativo selecionado!")
            return

        message = self.component_input_send_message.get()
        if not message.strip():
            #print("Mensagem vazia não será enviada.")
            return

        #print(f"Enviando mensagem: {message} para {self.chat_id}")

        recipient_email = self.get_chat_email(self.chat_id)
        self.db.send_message(self.logged_email, recipient_email, message)

        self.component_input_send_message.delete(0, 'end')
        self.load_message_in_canvas(force_update=True)

    def get_chat_email(self, chat_id):
        """Obtém o e-mail do destinatário com base no chat_id"""
        for chat in self.db.list_chats(self.logged_email):
            if chat[0] == chat_id:
                return chat[1]  # Retorna o e-mail do destinatário
        return None  # Retorna None caso não encontre

    def create_new_chat(self, email, message, modal):
        """Cria um novo chat com um usuário"""
        #print(f"Criando chat com {email} e enviando mensagem: {message}")  # Debug
        if email and message:
            self.db.send_message(self.logged_email, email, message)
            modal.destroy()
            self.load_chats()
 
    def show_chat_modal(self):
        """Exibe um modal para adicionar um novo chat"""
        modal = ctk.CTkToplevel(self.window)
        modal.geometry("400x300")
        modal.title("Novo Chat")

        label_email = ctk.CTkLabel(modal, text="Email do Destinatário")
        label_email.pack(pady=5)
        input_email = ctk.CTkEntry(modal, width=300)
        input_email.pack(pady=5)

        label_message = ctk.CTkLabel(modal, text="Mensagem Inicial")
        label_message.pack(pady=5)
        input_message = ctk.CTkEntry(modal, width=300)
        input_message.pack(pady=5)

        button_send = ctk.CTkButton(modal, text="Enviar", command=lambda: self.create_new_chat(input_email.get(), input_message.get(), modal))
        button_send.pack(pady=10)

    def logged_pages(self, entry_email, entry_password):
        """Verifica login e carrega a interface do chat"""
        if login(entry_email, entry_password):
            self.logged_email = entry_email.get()
            self.register_page.destroy()
            self.login_page.destroy()
            self.chat_frame()
            self.message_frame()
            self.input_send_message()
            self.button_send_message()
            self.button_create_chat()
            self.update_messages_loop()