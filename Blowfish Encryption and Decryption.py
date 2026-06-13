from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad

key = b'SecretKey'
message = b'Hello Blowfish'

cipher = Blowfish.new(key, Blowfish.MODE_ECB)

encrypted = cipher.encrypt(
    pad(message, Blowfish.block_size)
)

print("Encrypted:", encrypted)

decrypted = unpad(
    cipher.decrypt(encrypted),
    Blowfish.block_size
)

print("Decrypted:", decrypted.decode())