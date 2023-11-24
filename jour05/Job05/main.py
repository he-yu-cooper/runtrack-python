def caesar_cipher(message, shift):
    cipher = ''
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            cipher += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            cipher += char
    return cipher


print(caesar_cipher('hello', 3)) 
