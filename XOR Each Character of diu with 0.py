text = "DIU"

print("Original String:", text)
print("After XOR with 0:")

for ch in text:
    result = chr(ord(ch) ^ 0)
    print(f"{ch} -> {result}")
    