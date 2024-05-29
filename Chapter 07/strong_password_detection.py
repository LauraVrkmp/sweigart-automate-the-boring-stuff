import re

lengthRegex = re.compile(r'.{8,}')
upperCaseRegex = re.compile(r'[A-Z]+')
lowerCaseRegex = re.compile(r'[a-z]+')
digitRegex = re.compile(r'\d+')

def passwordChecker(password):
    if not lengthRegex.search(password):
        print('Password is not long enough.')
    elif not upperCaseRegex.search(password):
        print('Password doesn\'t contain an upper-case character.')
    elif not lowerCaseRegex.search(password):
        print('Password doesn\'t contain a lower-case character.')
    elif not digitRegex.search(password):
        print('Password doesn\'t contain a digit.')
    else:
        print('Password is strong!')

password = 'HAVEAGOAakjeioj9'
passwordChecker(password)