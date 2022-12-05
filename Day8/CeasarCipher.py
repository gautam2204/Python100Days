alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
'''
direction = "encrypt"
text = "Hello".lower()
shift = 5
'''

def ceasar(text,shift,direction):
    if direction == "encode":
        print(f"Plain Text = {text}\nshift = {shift}")
        cipher_word = ""
        for char in text.lower():
            charIndex = alphabet.index(char)
            newIndex = charIndex + shift
            cipher_word += alphabet[newIndex]

        print(f"Encrypted String is = {cipher_word}")

    elif direction == "decode":
        print(f"Encrypted Text = {text}\nshift = {shift}")
        plain_word = ""
        for char in text.lower():
            charIndex = alphabet.index(char)
            newIndex = charIndex - shift
            plain_word += alphabet[newIndex]

        print(f"decrypted String is = {plain_word}")

ceasar(text=text,shift=shift,direction=direction)
'''def encrypt(text, shift):
    print(f"Plain Text = {text}\nshift = {shift}")
    cipher_word = ""
    for char in text.lower():
        charIndex = alphabet.index(char)
        newIndex =  charIndex + shift
        cipher_word += alphabet[newIndex]

    print(f"Encrypted String is = {cipher_word}")

def dencrypt(text, shift):
    print(f"Encrypted Text = {text}\nshift = {shift}")
    plain_word = ""
    for char in text.lower():
        charIndex = alphabet.index(char)
        newIndex =  charIndex - shift
        plain_word += alphabet[newIndex]

    print(f"decrypted String is = {plain_word}")'''




