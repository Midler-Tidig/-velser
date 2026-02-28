num1 = input("Please choose a number")
num1 = int(num1)

if num1 % 2 == 0:
    print("Your number is even!")
    if num1 % 4 == 0:
        print("And is divisible by 4!")
else:
    print("Your number is odd!")