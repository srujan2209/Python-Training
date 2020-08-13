# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.
# Input
# Input number of rows: 3
# Input number of columns: 5
# Output
# [[0, 0, 0, 0, 0],
# [0, 1, 2, 3, 4],
# [0, 2, 4, 6, 8].

a = input("Enter the dimensional for array as row,column: ")
print(a)

rows,columns=a.split(",")
rows=int(rows)
columns=int(columns)

print("rows:",rows,"columns:",columns)

c=[[0]*columns]*rows


for i in range(rows):
    for j in range(columns):
        c[i][j] = i*j

print(c)





