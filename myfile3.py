#Filter Even Numbers from a list using lambda and filter function

list1 = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2==0,list1)))

#Sum of all items in a list using lambda and reduce function:

from functools import reduce
list2 = [ 1,2,3,4,5]
print(reduce(lambda a,b: a+b,list2))

##Multiplying Each item present in the list using lamnda and map function
list3 = [1,23,3,4,5,6,7]
print(list(map(lambda a:a*2,list3)))







