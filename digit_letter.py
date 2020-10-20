# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6
# Digits 2

Enter_String = input(" Input a string : ")
digit = letter = 0
for i in Enter_String:
    if i.isdigit():
        digit=digit+1
    elif i.isalnum():
        letter=letter+1
    else:
        pass
print("digit count = ",digit)
print("letter count = ",letter)


