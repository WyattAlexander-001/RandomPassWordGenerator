"""

Random Password Generator

"""

import random

letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o','p','q', 'r', 's','t','u', 'v', 'w', 'x', 'y','z'
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
          ]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

symbols = ['!', '$', '#','&']


print('Welcome To The Password Generator')


desired_letters = int(input('How many letters would you like?'))

desired_numbers = int(input('How many numbers would you like?'))

desired_symbols = int(input('How many symbols would you like?'))

#PASSWORD STARTS AS EMPTY LIST
password= []


for char in range(0, desired_letters ):
	password += random.choice(letters)
	
for char in range(0, desired_numbers ):
	password += random.choice(numbers)	

for char in range(0, desired_symbols):
	password += random.choice(symbols)


random.shuffle(password)


passwordFinal = ""
for char in password:
	passwordFinal += char
	
print(f'Your desired password is: \n{passwordFinal}')