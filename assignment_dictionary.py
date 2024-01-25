"""
write a program to accept a paragraph from user and print it in reverse order of words. don't perform
reverse of each word using python
"""
"""
paragraph = input("Enter a paragraph: ")
words = paragraph.split()
print("Reversed paragraph: "+' '.join(words[::-1]))

output
Enter a paragraph: write a program to accept a paragraph from user and print it in reverse order of words. don't perform 
Reversed paragraph: perform don't words. of order reverse in it print and user from paragraph a accept to program a write
"""

"""
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary
"""
"""
keys = {'Ten', 'Twenty', 'Thirty'}
values = {10, 20, 30}
new_dictionary = dict(zip(keys, values))
print(new_dictionary)

output
{'Thirty': 10, 'Ten': 20, 'Twenty': 30}
"""

"""
Write a Python program to convert them into a dictionary in a way that item from list1 is the key and
item from list2 is the value
E.g keys = ['Ten', 'Twenty', 'Thirty']    values = [10, 20, 30]
Expected output:     {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
"""
"""
keys = ['Ten','Twenty','Thirty']
values = [10,20,30]
print(dict(zip(keys,values)))

output
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
"""

# Write a Python program to merge two Python dictionaries into one.
"""
d1={'a':1,'b':2}
d2={'c':3,'d':4}
d1.update(d2)
print(d1)

output
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
"""

"""
Write a program that reads two strings from keyboard and prints the common words. Your program should 
convert input string to lower case.
"""
"""
string1 = input("Enter the first string: ").lower()
string2 = input("Enter the second string: ").lower()

words1 = string1.split()
words2 = string2.split()

common_words = set(words1) & set(words2)
if common_words:
    print("Common words between the two strings:")
    for word in common_words:
        print(word)
else:
    print("There are no common words between the two strings.")

output
Enter the first string: PRAKASH GOHIL
Enter the second string: KASH  GOHIL 
Common words between the two strings:
gohil
"""