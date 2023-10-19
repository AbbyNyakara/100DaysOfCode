# Create a ceaser cypher encoder.


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
              'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 
              'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
              'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(alphabets)


choice = input("Type 'encode' to encode or 'decode' to decode a message. \n ").lower()
text = input(f"Enter the text you want to {choice} \n").lower()
shift = int(input("Enter the shift number \n"))

def encrypt(plain_text, shift_amount):
    encoded_message = ''   
    for letter in plain_text:
        encoded_index = (alphabets.index(letter) + shift_amount)
        encoded_letter = alphabets[encoded_index]
        encoded_message += encoded_letter
    print(encoded_message)

encrypt(text, shift)

def decrypt(encoded_text, shift_number):
    decoded_message = ''   
    for letter in encoded_text:
        decoded_index = (alphabets.index(letter) - shift_number)
        decoded_letter = alphabets[decoded_index]
        decoded_message += decoded_letter
    print(decoded_message)


if choice == 'encode'.lower():
    encrypt(text, shift)
elif choice == "decode".lower():
    decrypt(text, shift)