p = 23
g = 5

a = 6
b = 15

A = (g ** a) % p
B = (g ** b) % p

key_A = (B ** a) % p
key_B = (A ** b) % p

print("Public Key A:", A)
print("Public Key B:", B)

print("Shared Secret at A:", key_A)
print("Shared Secret at B:", key_B)