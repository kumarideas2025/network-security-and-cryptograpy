plaintext = input("Plaintext: ")
key = int(input("key: "))
result = ""

for ch in plaintext:
    if ch.isalnum():
        if ch.islower():
            # Shift lowercase letters (a-z)
            ch = chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        elif ch.isupper():
            # Shift uppercase letters (A-Z)
            ch = chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        else:
            # Shift digits (0-9) - Note: Using % 10 for digits
            ch = chr((ord(ch) - ord('0') + key) % 10 + ord('0'))
            
    result += ch

print("ciphertext: ", result)