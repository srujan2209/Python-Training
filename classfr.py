lst = [1,2,3,4,20]
lst.append(5)
print(lst)
lst3 = [3,4,5]
lst3.extend('a')
lst3.extend([6,7,8,9]) #list inside
print(lst3)      # Diff between Extend and append

lst4 = [10,20,30]
lst4.insert(1,15)                       #list method(Use to add a specific elemnet at required elemnt) at first index 15 is place
print(lst4)
lst4.insert(3,'a')
print(lst4)

lst4.insert(1,[1,2,3])
print(lst4)
#append, extend, remove, pop,

#palendrome number
#prime number or not
#fibaconnic series

# diff between remove(argument must be element name not index name) and pop

lst5 = [20,15,30]
lst5.remove(15)
print(lst5)
lst5.remove(50)
print(lst5)

# pop is used (by mentioning indexing name we can remove element)

# different between insert, append , remove, pop,
# string clear is not supported is static object
# Clear method it removes the entire method:
#List dynamic
lst7.clear()
#Del Mthod
#used Specific
# Clear(entire list delete) and DEl(specific list or entire list)diference

lst8 = [1,2,3,4]
del lst8[0]
print(lst8)

#Remove
# lst3.sort(reverse=true)