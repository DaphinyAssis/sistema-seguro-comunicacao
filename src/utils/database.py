import ctypes

class Database:
    def __init__(self):
        self.db = ctypes.CDLL(r"C:\Users\assis\Documents\sistema-seguro_comunicacao\src\repository\C\database.dll")
        # Definir argumentos para evitar problemas de string
        self.db.insert_user.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
        self.db.get_user.argtypes = [ctypes.c_char_p]
        self.db.update_user.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.db.delete_user.argtypes = [ctypes.c_char_p]

    def insert_user(self, email, name, password, hash, phone):
        self.db.insert_user(email.encode(), name.encode(), password.encode(), hash.encode(), phone.encode())

    def get_user(self, email):
        self.db.get_user(email.encode())

    def update_user(self, email, new_hash):
        self.db.update_user(email.encode(), new_hash.encode())

    def delete_user(self, email):
        self.db.delete_user(email.encode())

    def list_users(self):
        buffer_size = 4096  # Define um tamanho grande para armazenar os dados
        buffer = ctypes.create_string_buffer(buffer_size)
        self.db.list_users(buffer, buffer_size)
        return buffer.value.decode()


db = Database()
print(db.list_users())
# Testando as funções no Python
"""
insert_user("diana@example.com", "Diana", "pass123", "hash789", "555-1234")
get_user("diana@example.com")
update_user("diana@example.com", "new_hash_123")
delete_user("diana@example.com")
"""