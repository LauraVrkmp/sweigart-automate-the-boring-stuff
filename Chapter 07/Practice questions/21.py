import re

fullNameRegex = re.compile(r'^[A-Z][a-zA-Z]* Nakamoto$')

print(fullNameRegex.search('Satoshi Nakamoto'))
print(fullNameRegex.search('Alice Nakamoto'))
print(fullNameRegex.search('RoboCop Nakamoto'))

print(fullNameRegex.search('satoshi Nakamoto'))
print(fullNameRegex.search('Mr. Nakamoto'))
print(fullNameRegex.search('Nakamoto'))
print(fullNameRegex.search('Satoshi nakamoto'))