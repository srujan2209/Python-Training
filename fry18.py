# Write a program to print the number is prime or not

num = int(input("Enter Number: "))
for i in range(2, num):
    if num <= 1:
        print("Not prime")
    elif num % i == 0:
        print("Not prime")
        break
else:
    print("Prime",num)
