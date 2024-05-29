import re

numberRegex = re.compile(r'^\d{1,3}(,\d{3})*$', re.VERBOSE)

print(numberRegex.search('42'))
print(numberRegex.search('1,234'))
print(numberRegex.search('6,368,745'))

print(numberRegex.search('12,34,567'))
print(numberRegex.search('1234'))