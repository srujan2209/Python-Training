# The included code stub will read an integer, n, from STDIN. Without using any string methods, try to print the following:
# 123....n
# Constrains , 1<=n<=150, if n value is 2, o/p should be 12
# Case 1 :

# n = int(input("Enter the number: "))
# j=1
# for i in range(n):
#     print(j+i,end='')
#     if j+1 == n+1:
#         break
# ------------------------------------------------------------------------------------------------------------------------------
#Case 2 :

if __name__ == '__main__':
    n = int(input("Enter the number: "))
    for i in range(1,n+1):
        print(i,end='')

