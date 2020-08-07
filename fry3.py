#Write a program to find the highest of three numbers
a=int(input("Enter Number: "))
b=int(input("Enter Number: "))
c=int(input("Enter Number: "))

if a>b and a>c:
    print("The highest of three numbers is:",a)
elif b>c and b>a:
    print("The highest of three numbers is:",b)
else:
    print("The highest of three numbers is:",c)

