# Write a python to print different vowels present in the given word , user


word = input("Enter the word: ")

vowel =['a','e','i','o','u']

word1=[]

for x in word:
    if x in vowel and x not in word1:
        word1.append(x)
print("The vowels Present in the word is ",word1)
