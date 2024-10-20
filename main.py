from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    result_text = ""
    for letter in text:
        if letter in alphabet:
            number = alphabet.index(letter)
            if direction == "encode":
                shifted_number = number + shift
            elif direction == "decode":
                shifted_number = number - shift
            shifted_letter = alphabet[shifted_number]
            result_text += shifted_letter
        else:
            result_text += letter
    print(f'The {direction}d text is "{result_text}"')

restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(text, shift, direction)
    response = input("Do you want to restart the cipher program? Type 'Y' for Yes, 'N' for No.\n").upper()
    if response == "N":
        restart = False
        print("Good bye!")