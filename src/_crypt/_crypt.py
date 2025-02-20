from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

class Crypt:
    def __init__(self):
        self.key = b"389dynrw789ryruysnofuish"  # Chave para AES

    # Função para criptografar com AES (modo CBC)
    def encrypt_aes(self, data):
        iv = os.urandom(16)  # Geração de IV aleatório de 16 bytes
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data.encode()) + padder.finalize()
        
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ct = encryptor.update(padded_data) + encryptor.finalize()
        
        # Codifica IV e ciphertext em base64 para transmissão
        iv_b64 = base64.b64encode(iv).decode('utf-8')
        ct_b64 = base64.b64encode(ct).decode('utf-8')
        
        return iv_b64 + ":" + ct_b64

    # Função para descriptografar com AES (modo CBC)
    def decrypt_aes(self, data):
        iv_b64, ct_b64 = data.split(":")
        iv = base64.b64decode(iv_b64)
        ct = base64.b64decode(ct_b64)
        
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(ct) + decryptor.finalize()
        
        unpadder = padding.PKCS7(128).unpadder()
        data = unpadder.update(padded_data) + unpadder.finalize()
        
        return data.decode('utf-8')

    # Função para gerar hash (SHA-256)
    def hash_password(self, password):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(password.encode())
        return digest.finalize().hex()
    
    # Decorator para criptografar a mensagem com AES
    def aes_encrypt_decorator(self, func):
        def wrapper(*args, **kwargs):
            message = args[3]  # O terceiro argumento é a mensagem
            encrypted_message = self.encrypt_aes(message)
            
            # Atualiza o argumento de mensagem com a versão criptografada
            args = args[:3] + (encrypted_message,) + args[4:]
            
            return func(*args, **kwargs)
        return wrapper

    # Decorator para descriptografar a mensagem com AES
    def aes_decrypt_decorator(self, func):
        def wrapper(*args, **kwargs):
            message = args[2]  # Supondo que a mensagem seja o 3º argumento
            decrypted_message = self.decrypt_aes(message)
            # Atualiza o argumento de mensagem com a mensagem descriptografada
            args = args[:2] + (decrypted_message,) + args[3:]
            return func(*args, **kwargs)
        return wrapper

    # Decorator para criptografar a senha com hash
    def hash_password_decorator(self, func):
        def wrapper(*args, **kwargs):
            password = args[3]  # Supondo que a senha seja o 3º argumento
            hashed_password = self.hash_password(password)
            args = args[:3] + (hashed_password,) + args[4:]
            return func(*args, **kwargs)
        return wrapper