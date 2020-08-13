#  Write a Python program to construct the following pattern, using a nested for loop.
#            *
#          * *
#        * * *
#      * * * *
#    * * * * *
#      * * * *
#        * * *
#          * *
#            *

n = int(input("Enter n Value: "))
for i in range(n):
    print('  '*(n-i-1)+'* '*(i+1))
for i in range(n-1):
    print('  '*(i+1)+'* '*(n-i-1))
