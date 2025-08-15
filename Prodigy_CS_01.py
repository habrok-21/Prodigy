def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

print("\n🔐 Welcome to the Caesar Cipher Tool 🔐")
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))

encrypted = caesar_cipher(message, shift, 'encrypt')
decrypted = caesar_cipher(encrypted, shift, 'decrypt')

print("\n📄 Encrypted Message:", encrypted)
print("📜 Decrypted Message:", decrypted)
