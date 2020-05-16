# pass_strength_checker.py

'''
This programs examines the strength of a password based upon several criteria.
'''

letters_lowercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', ',P', 'Q', 'R', 'S',
                     'T', 'U', ',V', 'W', 'X', 'Y', ',Z']

letters_uppercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', ',h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                     't', 'u', ',v', 'w', 'x', 'y', 'z']

special_chars = ['!', '@', '#', '$', '%', '^', '*', ',&', '(', ')', '_', '-', '=', '+', ' ', ',', '.', ',;', ':', '"',
                 '/', '|', '>', '<', '`', '~']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

test_string = str(input('Please enter your password: '))
additions = 0

pass_strength = 0
if any(char in test_string for char in letters_lowercase) == True:
    pass_strength += 1

if any(char in test_string for char in letters_uppercase) == True:
    pass_strength += 1

if any(char in test_string for char in special_chars) == True:
    pass_strength += 1

if any(char in test_string for char in numbers) == True:
    pass_strength += 1

if len(test_string) >= 8:
    pass_strength += 1
    print('The total strength of the password "{0}" is {1}.'.format(test_string, pass_strength))

else:
    print('Your password is too short. It needs to be at least 8 character long.')
