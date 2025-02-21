from tkinter import *
from utils.database import Database
from utils.login_verify import login

class GInterface:
    def __init__(self):
        self.window = Tk()
        self.db = Database()
        self.window.geometry('400x400')
        self.window.title('Teste')
        self.login_page = Label(self.window)
        self.login_page.pack(fill=BOTH)
        self.logged_email = ""
        self.gui_login()
        self.window.mainloop()

    def gui_login(self):
        self.input_email = Entry(self.login_page)
        self.input_email.pack()
        self.input_password = Entry(self.login_page)
        self.input_password.pack()
        self.button_login = Button(self.login_page, command=lambda entry_email=self.input_email, entry_password=self.input_password : self.logged_pages(entry_email, entry_password),text='Login') 
        self.button_login.pack()

    def gui_dashboard(self):
        self.dashboard_page = Label(self.window)
        self.dashboard_page.pack(fill=BOTH)
        print(self.db.list_chats(self.logged_email))

    def logged_pages(self, entry_email, entry_password):
        if login(entry_email, entry_password):
            self.logged_email = entry_email.get()
            self.login_page.destroy()
            self.gui_dashboard()
