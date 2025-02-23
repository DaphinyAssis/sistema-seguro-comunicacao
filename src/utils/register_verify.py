from utils.database import Database

db = Database()

def register(entry_email, entry_name, entry_password, entry_confirm_password, entry_phone, entry_code, receive_code):
        email = entry_email.get()
        name = entry_name.get()
        password = entry_password.get()
        password_confirm = entry_confirm_password.get()
        phone = entry_phone.get()
        print(entry_code.get())
        print(receive_code)
        #db.list_users() retorno: [['teste@gmail.com', 'Teste', '123', 'anyhash', 'anyphone'], ['namorandinha@gmail.com', 'Namorandinha', '1233', 'anyhash', 'anyphone']]
        for users in db.list_users():
            if email == users[0]:
                return False
        if password == password_confirm and entry_code.get() == receive_code:
            db.insert_user(email, name, password, "anyhash", phone) 
            return True
        
        return False