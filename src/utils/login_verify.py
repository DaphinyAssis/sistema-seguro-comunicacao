from hashlib import sha256
from utils.database import Database

db = Database()

def login(entry_email, entry_password):
        email = entry_email.get()
        password = entry_password.get()
        hashed_password = sha256(password.encode()).hexdigest()
        for i in db.list_users():
            if email == i[0]:
                if hashed_password == i[2]:
                    return True
                else:
                    return False