import base64
from cryptography.fernet import Fernet
from Cryptodome.Cipher import AES

class MyCrypto:

    def encrypt(texto):
        key = base64.urlsafe_b64encode('master_key'.encode()) #Fernet.generate_key() #this is your "password"
        fernet = Fernet(key)
        encoded_text = fernet.encrypt(texto)
        return encoded_text

    def decrypt(encrypted):
        key = base64.urlsafe_b64encode('master_key'.encode())
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted)
        return decrypted

    def encrypt_id(texto):
        master_key = 'master_key'
        raw = MyCrypto._pad(str(texto))
        raw = raw.encode()
        #iv = Random.new().read( 16 )
        iv = b'JW1Ym2DsUe52OePV'
        cipher = AES.new(master_key, AES.MODE_CBC, iv, segment_size=128 )
        encrypted = base64.b64encode( iv + cipher.encrypt( raw ) ).decode()
        return encrypted

    def decrypt_id(text):
        master_key = 'master_key'
        enc = base64.b64decode(text)
        iv = enc[:AES.block_size]
        cipher = AES.new(master_key, AES.MODE_CBC, iv)
        decrypted = MyCrypto._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
        return decrypted

    def _pad(s):
        padded = s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
        return padded

    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]