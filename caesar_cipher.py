def encrypt(text, shift):
    encrypted = ""

    for ch in text:
        if ch.isupper():
            encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif ch.islower():
            encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += ch

    return encrypted


def decrypt(text, shift):
    decrypted = ""

    for ch in text:
        if ch.isupper():
            decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        elif ch.islower():
            decrypted += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += ch

    return decrypted


print("=== Basic Encryption & Decryption (Caesar Cipher) ===")

text = input("Enter text: ")
shift = int(input("Enter shift key: "))

encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)