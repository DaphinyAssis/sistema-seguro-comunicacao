import ctypes
from _crypt._crypt import Crypt
crypt = Crypt()
class Database:
    def __init__(self):
        
        self.db = ctypes.CDLL(r"C:\Users\assis\OneDrive\Anexos\Documentos\sistema-seguro-comunicacao\src\repository\C\database.dll")
        # Definir argumentos para evitar problemas de string
        self.db.insert_user.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
        self.db.get_user.argtypes = [ctypes.c_char_p]
        self.db.update_user.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.db.delete_user.argtypes = [ctypes.c_char_p]
        self.db.send_message.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
        self.db.list_messages.argtypes = [ctypes.c_char_p]
        self.db.list_chats.argtypes = [ctypes.c_char_p]
        self.db.list_messages_from_chat.argtypes = [ctypes.c_int]
        self.db.list_users.argtypes = [ctypes.c_char_p, ctypes.c_size_t]

    @crypt.hash_password_decorator
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
        # Decodifica o buffer e ignora erros de decodificação
        users_str = buffer.value.decode("utf-8", errors="ignore").strip()

        if "Error!" in users_str or "No users found" in users_str:
            return []  # Retorna uma lista vazia se houver erro ou nenhum usuário

        # Divide os registros corretamente com base no '\n' adicionado
        users_list = [user.split("|") for user in users_str.split("\n") if user]

        return users_list
    
    @crypt.aes_encrypt_decorator
    def send_message(self, sender_email, recipient_email, message):
        self.db.send_message(sender_email.encode(), recipient_email.encode(), message.encode())

    def list_messages(self, email):
        self.db.list_messages(email.encode())

    def list_chats(self, email):
        buffer_size = 4096
        buffer = ctypes.create_string_buffer(buffer_size)
        self.db.list_chats(email.encode(), buffer, buffer_size)

        chats_str = buffer.value.decode("utf-8", errors="ignore").strip()

        if "Error!" in chats_str or "No chats found" in chats_str:
            return []

        chats_list = [line.split("|") for line in chats_str.split("\n") if line]
        
        return [[int(chat[0]), chat[1]] for chat in chats_list]

    def list_messages_from_chat_original(self, chat_id):
        buffer_size = 4096
        buffer = ctypes.create_string_buffer(buffer_size)
        self.db.list_messages_from_chat(ctypes.c_int(chat_id), buffer, buffer_size)

        messages_str = buffer.value.decode("utf-8", errors="ignore").strip()

        if "Error!" in messages_str or "Chat ID not found" in messages_str:
            return []
        
        
        #@crypt.aes_decrypt_decorator
        messages_list = [line.split("|") for line in messages_str.split("\n") if line]
        
        return messages_list

    def list_messages_from_chat(self, chat_id):
            buffer_size = 4096
            buffer = ctypes.create_string_buffer(buffer_size)
            self.db.list_messages_from_chat(ctypes.c_int(chat_id), buffer, buffer_size)

            messages_str = buffer.value.decode("utf-8", errors="ignore").strip()

            if "Error!" in messages_str or "Chat ID not found" in messages_str:
                return []

            # Quebra as mensagens em uma lista
            messages_list = [line.split("|") for line in messages_str.split("\n") if line]

            # Descriptografar as mensagens e garantir que não haja duplicatas
            decrypted_messages_list = []
            seen_messages = set()  # Armazena as mensagens já vistas, por exemplo, usando hash

            for sender_email, encrypted_message in messages_list:
                decrypted_message = crypt.decrypt_aes(encrypted_message)

                # Gerar um hash único para a mensagem (pode ser uma combinação de email e conteúdo)
                message_hash = hash(decrypted_message + sender_email)

                # Se a mensagem não foi vista antes, adicione-a à lista
                if message_hash not in seen_messages:
                    seen_messages.add(message_hash)
                    decrypted_messages_list.append([sender_email, decrypted_message])

            return decrypted_messages_list
"""db = Database()
#db.insert_user("diana@example.com", "Diana", "pass123", "hash789", "555-1234")
db.send_message("diana@example.com", "teste@example.com", "Outra mensagem")
#print(db.list_users())
db.list_messages("teste@example.com")"""
"""
db.list_users()
db.insert_user("diana@example.com", "Diana", "pass123", "hash789", "555-1234")
db.get_user("diana@example.com")
db.update_user("diana@example.com", "new_hash_123")
db.delete_user("diana@example.com")
"""