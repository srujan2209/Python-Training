# find the biggest of a given values using lambda given by user
a = int(input("Enter Number: "))
b = int(input("Enter NUmber : "))
Largest = lambda a,b : a if a>b else b

print(Largest(a,b))
