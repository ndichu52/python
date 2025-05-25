msg = "Cipher"

# 1. Print the first character
print(msg[0])

# 2. Print the last 2 letters
print(msg[-2:])

# 3. Convert to uppercase
print(msg.upper())

# 4. Reverse the string
print(msg[::-1])
#caesar cipher
message="Hello World"
shift=3
def caesar():
    alphabet="abcdefghijklmnopqrstuvwxyz"
    encrypted_text=""
    for char in message.lower():
        if char in alphabet:
            index = alphabet.find(char)
            new_index = (index + shift) % 26
            encrypted_text += alphabet[new_index]
    else:
        encrypted_text += char  # keep spaces and punctuation
