# Create a ceaser cypher encoder.


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
              'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 
              'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
              'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(alphabets)


choice = input("Type 'encode' to encode or 'decode' to decode a message. \n ").lower()
text = input("Enter the text you want to encrypt \n").lower()
shift = int(input("Enter the shift number \n"))

def encrypt(plain_text, shift_amount):
    encoded_message = ''   
    for letter in plain_text:
        encoded_index = (alphabets.index(letter) + shift_amount)
        encoded_letter = alphabets[encoded_index]
        encoded_message += encoded_letter
    print(encoded_message)


encrypt(text, shift)
    




# if choice == 'encode'.lower():
#     encode_message(message="hello")