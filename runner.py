# Basic Data Types
n = int(input())
arr = list(map(int, input().split()))
print(n)
print(arr.sort())
print(arr[arr.index(max(arr))]-1)
