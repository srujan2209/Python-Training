# Write a Python program to check a triangle is valid or not

def triangle_check(a,b,c):
    if (a>b+c) or (b>a+c) or (c>a+b):
        print('No, The length wont form a triangle')
    elif (a==b+c) or (b==a+c) or (c==a+b):
        print('yes, it can forma a degenerated triangle')
    else:
        print('Yes, it can be formed out of from measurements')

length1 = int(input("Enter the first side: "))
length2 = int(input("Enter the second side: "))
length3 = int(input("Enter the third side: "))

triangle_check(length1,length2,length3)