# def greet():
#     print("hello")

# greet()

import string
import math

alphabets = list(string.ascii_lowercase)
print(alphabets)

msg = list('abb')

for letter in msg:
    new = alphabets.index(letter) + 2
    print(alphabets[new])


