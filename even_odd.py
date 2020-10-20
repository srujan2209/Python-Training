# Count the number of even and odd numbers from a series of numbers
# Input
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
# Output
# Number of even numbers : 4
# Number of odd numbers : 5

Input_number = (1,2,3,4,5,6,7,8,9)
Even_Number = 0
Odd_Number = 0
for i in Input_number:
    if i%2==0:
        Even_Number=Even_Number+1
    else:
        Odd_Number=Odd_Number+1
print("Even Number:",Even_Number)
print("Odd Number:",Odd_Number)

