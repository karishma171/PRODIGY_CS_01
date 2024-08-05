def caesar_cipher(text, shift, mode):
    # Function to perform Caesar Cipher encryption or decryption
    result = ""

    # Traverse the text
    for char in text:
        # Encrypt/decrypt uppercase characters
        if char.isupper():
            if mode == "encrypt":
                result += chr((ord(char) + shift - 65) % 26 + 65)
            elif mode == "decrypt":
                result += chr((ord(char) - shift - 65) % 26 + 65)
        # Encrypt/decrypt lowercase characters
        elif char.islower():
            if mode == "encrypt":
                result += chr((ord(char) + shift - 97) % 26 + 97)
            elif mode == "decrypt":
                result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # If it's not an alphabetic character, keep it as it is
            result += char

    return result

# Get inputs from the user
message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter mode (encrypt/decrypt): ").lower()

# Perform the requested operation
if mode == "encrypt":
    encrypted_message = caesar_cipher(message, shift, mode)
    print(f"Encrypted message: {encrypted_message}")
elif mode == "decrypt":
    decrypted_message = caesar_cipher(message, shift, mode)
    print(f"Decrypted message: {decrypted_message}")
else:
    print("Invalid mode selected. Please choose either 'encrypt' or 'decrypt'.")
