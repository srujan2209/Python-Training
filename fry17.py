# Write a number which is divisible by 3 and but not 5 in the list up to 20 (12,15,10,18,6,3,30):

list = [12,15,10,18,6,3,30]
for i in list:
    if i%3==0 and i%5!=0:
        print(i)
