def encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            start = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch)-start+key)%26 + start)
        else:
            result += ch

    return result

def decrypt(text, key):
    return encrypt(text, -key)

plain = "HELLO"
key = 3

cipher = encrypt(plain, key)

print("Plain Text :", plain)
print("Encrypted  :", cipher)
print("Decrypted  :", decrypt(cipher, key))