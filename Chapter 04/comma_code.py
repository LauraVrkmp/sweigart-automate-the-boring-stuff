def comma_coder(list_values):
    for item in range(len(list_values) - 1):
        print(list_values[item] + ', ', end='')
    print('and ' + list_values[-1])

spam = ['apples', 'bananas', 'tofu', 'cats']

comma_coder(spam)