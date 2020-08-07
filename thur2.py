#write a pgm to display the Name and their percentage in dictionary#

d = {}
n = int(input("Enter Number of students:  "))
i = 1
while i<=n:
    name = input("Enter the Name: ")
    Percentage = input("Enter your percentage: ")
    d[name]= Percentage
    i = i+1
print(d)