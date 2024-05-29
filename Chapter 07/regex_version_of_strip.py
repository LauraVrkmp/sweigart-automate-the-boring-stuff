import re

myStripLeftRegex = re.compile(r'^\s+')
myStripRightRegex = re.compile(r'\s+$')

def my_strip(string, substitute=''):
    new_string = myStripLeftRegex.sub(substitute, string)
    new_string = myStripRightRegex.sub(substitute, new_string)
    print(new_string)

string = "   ab  c   "
my_strip(string, 'def')
my_strip(string)