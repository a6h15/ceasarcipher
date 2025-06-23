alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def decrypt(original_text ,shift_amount):
    decoded_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        decoded_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {decoded_text}")

decrypt(original_text=text,shift_amount=shift)

def encrypt(original_text,shift_amount):
    cipher_text = ""
    for char in original_text:
        shifted_position = alphabet.index(char) + shift_amount
        shifted_position %= len(alphabet) # always between 0 - 25
        cipher_text += alphabet[shifted_position]

    print(f"Here is your encrypted text - {cipher_text}")


encrypt(original_text=text,shift_amount=shift)

