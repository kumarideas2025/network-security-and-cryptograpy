def power(base, exp, mod):
    return pow(base, exp, mod)

p = 3
q = 11

n = p * q
e = 3
d = 7

message = 5

encrypted = power(message, e, n)
decrypted = power(encrypted, d, n)

print("Original :", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)