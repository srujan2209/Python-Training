#write a program to find the smallest of three numbers
a = int(input("Enter Number:"))
b = int(input("Enter Number:"))
c = int(input("Enter Number:"))

if a<b and a<c:
    print("the smallest is:",a)
elif b<a and b<c:
    print("the smallest is:",b)
else:
    print("the smallest is:",c)
