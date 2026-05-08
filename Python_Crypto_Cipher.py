import string

def caesar_cipher(message, key):
    shift = key % 26
    ciphered = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])

    encrypted_message = message.lower().translate(ciphered)

    return encrypted_message

def caesar_decipher(encrypted_message, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    decrypted_message = encrypted_message.translate(cipher)
    return decrypted_message

message = input("Enter a message to encrypt: ")
key = int(input("Enter a key (number of positions to shift): "))

encrypted_message = caesar_cipher(message, key)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = caesar_decipher(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")