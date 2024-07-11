import getpass
print("One-Million-To-One")
myNumber = getpass.getpass(prompt='Give me the number: ')
count = 0
while True:
    yourNumber = input("What is your gess?: ")
    count += 1
    if myNumber == yourNumber:
        print("Correct")
        break
    elif myNumber > yourNumber:
        print("Too low")
    elif myNumber < yourNumber:
        print("Too higth")
    elif yourNumber > 1000000:
        print("your number is too high than 1 million")
        exit()
    elif yourNumber < 0:
        exit()
    else:
        continue
print("It took you ", count, "guesses to get it correct!")