
# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     length =  26
#     last_index = length - 1
#     encrypted_text = ""
#     for letter in original_text:
#         if letter != " ":
#             index = alphabet.index(letter)
#             new_index = index + shift_amount
#
#             if new_index > last_index:
#                 new_index = new_index % length
#             new_letter =  alphabet[new_index]
#             encrypted_text += new_letter
#         else:
#             encrypted_text += letter
#     print(f"Here is the encoded result: {encrypted_text}")
#
# def decrypt(original_text, shift_amount):
#     length = 26
#     last_index = - (length - 1)
#     decrypted_text = ""
#
#     for letter in original_text:
#         if letter != " ":
#             index = alphabet.index(letter)
#             new_index = index - shift_amount
#             if new_index < last_index:
#                 new_index = new_index % length
#             new_letter =  alphabet[new_index]
#             decrypted_text += new_letter
#         else:
#             decrypted_text += letter
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, original_text, shift_amount):
    length =  26
    processed_text = ""
    step = 0

    if direction == "encode":
        step = 1
    elif direction == "decode":
        step = - 1

    if step != 0:
        shift_amount = step * shift_amount
        for letter in original_text:
            if letter != " ":
                index = alphabet.index(letter)
                new_index = (index + shift_amount) % length
                processed_text +=  alphabet[new_index]
            else:
                processed_text += letter
        print(f"Here is the {direction}d result: {processed_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caesar(direction, text, shift)

# gvvsvnpza