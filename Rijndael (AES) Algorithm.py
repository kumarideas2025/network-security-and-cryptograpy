from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890123456'
plaintext = b'Rijndael Example'

cipher = AES.new(key, AES.MODE_ECB)

ciphertext = cipher.encrypt(
    pad(plaintext, AES.block_size)
)

print("Cipher Text:", ciphertext)

decrypted = unpad(
    cipher.decrypt(ciphertext),
    AES.block_size
)

print("Decrypted:", decrypted.decode())