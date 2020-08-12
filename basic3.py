# Write a Python program that accepts an integer (t) and computes the value of t+tt+ttt.
#Suppose if we entered the value of t as 5. it should gives us result 615.

n=int(input("Enter a number n: "))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
value = n+int(t1)+int(t2)
print("The Expected outcome is :",value)

