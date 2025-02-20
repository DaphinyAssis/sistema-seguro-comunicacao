from tkinter import *
from utils.database import Database


class GInterface:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('400x400')
        self.window.title('Teste')
        self.window.mainloop()
        self.db = Database()
        self.get_all_users()

    def get_all_users(self):
        self.db.list_users()

    def gui_register(self):
        self.input_email = Entry(self.windo)
