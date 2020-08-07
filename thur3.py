#write a program to display the count the vowels in the string

def vowel(name):
    count = 0
    vowels = 'aeiou'
    for  letter in name:
        if letter in vowels:
            count +=1
    return count
print(vowel("Start up factory"))
