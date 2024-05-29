import re

sentenceRegex = re.compile(r'''(
                           ^(Alice|Bob|Carol)\s
                           (eats|pets|throws)\s
                           (apples|cats|baseballs)\.$
                           )''', re.IGNORECASE | re.VERBOSE)

print(sentenceRegex.search('Alice eats apples.'))
print(sentenceRegex.search('Bob pets cats.'))
print(sentenceRegex.search('Carol throws baseballs.'))
print(sentenceRegex.search('Alice throws Apples.'))
print(sentenceRegex.search('BOB EATS CATS.'))

print(sentenceRegex.search('RoboCop eats apples.'))
print(sentenceRegex.search('ALICE THROWS FOOTBALLS.'))
print(sentenceRegex.search('Carol eats 7 cats.'))