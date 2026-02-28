num = int(input("Please write any number:"))
num_original = num
divisor = 2
print(f"The prime factors of your number {num_original} are: ")
while num > 1:
    if num % divisor == 0:
        print(int(divisor), end=" x " )
        num = num / divisor
    else: 
        divisor = divisor + 1 
