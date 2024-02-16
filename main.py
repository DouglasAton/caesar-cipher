"""
Caesar Cipher Program:

This Python script implements the Caesar cipher, a simple substitution cipher that shifts letters in the alphabet
by a certain number of positions. The user can choose to encode or decode a message by specifying the direction
of the cipher and the number of positions to shift.

Usage:
- Run the script.
- Choose 'encode' to encrypt a message or 'decode' to decrypt a message.
- Enter the message you want to encrypt or decrypt.
- Specify the number of positions to shift.
- The script will output the encrypted or decrypted message.
- Optionally, choose to run the program again or exit.
"""

from art import logo

# List of alphabet letters (lowercase), with duplicates to handle shifts that go beyond the end of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    """
        Encrypts or decrypts a message using the Caesar cipher.
        Args:
            start_text (str): The original message to be encrypted or decrypted.
            shift_amount (int): The number of positions to shift the alphabet for encryption or decryption.
            cipher_direction (str): The direction of the cipher operation, either 'encode' or 'decode'.
        Returns:
            str: The encrypted or decrypted message.
        """
    end_text = ""

    # Adjust shift_amount if decrypting
    if cipher_direction == "decode":
        shift_amount *= -1  # Reverse the direction of the shift for decoding
    for char in start_text:
        # Check if the character is in the alphabet
        if char in alphabet:
            position = alphabet.index(char)  # Get the position of the letter in the alphabet
            new_position = position + shift_amount  # Calculate the new position after the shift
            end_text += alphabet[new_position]  # Add the shifted letter to the end text
        else:
            end_text += char  # Keep non-letter characters unchanged
    print(f"Here's the {cipher_direction}d result: {end_text}") # Display the encrypted or decrypted result


# Display the program logo
print(logo)

should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()  # Convert the message to lowercase for compatibility
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  # Ensure the shift is a number between 0 and 25

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
