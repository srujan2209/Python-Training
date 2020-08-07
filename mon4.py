#pgm to find the missing even value in the list=[1,2,3,4,5,6,9,10].

list = [1,2,3,4,5,6,9,10]

for i in range(1,11):
    if i%2==0:
        if i not in list:
            print(i)