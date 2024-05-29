def collatz(number):
    return number // 2 if (number % 2) == 0 else number * 3 + 1

if __name__ == '__main__':
    print("Enter a number greater than one:")

    try:
        number = int(input())
    except ValueError:
        print("You must enter an integer.")
        exit()

    while True:
        if number == 1:
            break
        else:
            number = collatz(number)
            print(number)