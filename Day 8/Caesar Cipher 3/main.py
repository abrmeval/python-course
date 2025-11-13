# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

#
# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#
#     for letter in original_text:
#         if encode_or_decode == "decode":
#             shift_amount *= -1
#
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {output_text}")
#
#
# # TODO-3: Can you figure out a way to restart the cipher program?
#
# print(logo)
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

#Final function
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
        for char in original_text:
            if char in alphabet:
                index = alphabet.index(char)
                new_index = (index + shift_amount) % length
                processed_text +=  alphabet[new_index]
            else:
                processed_text += char
        print(f"Here is the {direction}d result: {processed_text}")

go_again = True
print(logo)
while go_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)

    answer = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
    if answer == "no":
        go_again = False
print("Goodbye")

