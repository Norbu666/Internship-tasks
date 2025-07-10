def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    
    if mode == "decrypt":
        shift = -shift  # reverse shift for decryption
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char  
    
    return result

# get user input
message = input("enter your message: ")
shift_value = int(input("enter shift value: "))

# encrypt and decrypt
encrypted_message = caesar_cipher(message, shift_value, mode="encrypt")
decrypted_message = caesar_cipher(encrypted_message, shift_value, mode="decrypt")

print(f"encrypted message: {encrypted_message}")
print(f"decrypted message: {decrypted_message}")
