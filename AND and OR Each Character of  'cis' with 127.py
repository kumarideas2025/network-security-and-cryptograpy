text = "CIS"

print("AND with 127")
for ch in text:
    print(f"{ch} -> {ord(ch) & 127}")

print("\nOR with 127")
for ch in text:
    print(f"{ch} -> {ord(ch) | 127}")