from collections import Counter


def count_letter_frequency(text):
    text = text.lower()
    text = ''.join(filter(str.isalpha, text))
    frequency = Counter(text)

    return frequency


def substitution_cipher(text, substitution_map):

    plaintext = ""
    for char in text:
        if char in substitution_map:
            plaintext += substitution_map[char]
        elif char.isalpha():
            plaintext += '*'
        else:
            plaintext += char
    return plaintext


ciphertext = "xs czi pljm l aglo lok czi elou uz xfagmfmou xu xo czit gxsm upmo czi omnk kxwqxagxom"
print("ciphertext:\n", ciphertext)

letter_freq = count_letter_frequency(ciphertext)
print("alphabet frequency: ")

for letter, freq in sorted(letter_freq.items(), key=lambda x: x[1], reverse=True):
    print(f"{letter}: {freq}")


substitution_map = {
    'x': 'i',
    'm': 'e',
    'l': 'a',
    'o': 'n',
    'k': 'd',
    's': 'f',
    'w': 's',
    'q': 'c',
    'a': 'p',
    'g': 'l',
    'f': 'm',
    'u': 't',
    'p': 'h',
    'e': 'w',
    'j': 'v',
    'z': 'o',
    'c': 'y',
    'i': 'u',
    't': 'r',
    'n': 'e'
}

plaintext = substitution_cipher(ciphertext, substitution_map)
print("\n\nplaintext: ", plaintext)
