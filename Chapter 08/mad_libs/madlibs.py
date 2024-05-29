print("Enter an adjective:")
adjective = input()
print("Enter a noun:")
noun_1 = input()
print("Enter a verb:")
verb = input()
print("Enter another noun:")
noun_2 = input()

output = "The " + adjective + " panda walked to the " + noun_1 + " and then " \
        + verb + ". A nearby " + noun_2 + " was unaffected by these events."

print(output)
outputFile = open('output.txt', 'w')
outputFile.write(output)
outputFile.close()