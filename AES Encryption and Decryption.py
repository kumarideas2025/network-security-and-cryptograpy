from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890123456'
message = b'Hello AES'

cipher = AES.new(key, AES.MODE_ECB)

encrypted = cipher.encrypt(pad(message, AES.block_size))
print("Encrypted:", encrypted)

decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)
print("Decrypted:", decrypted.decode())