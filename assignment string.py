# calculate the length of a string
"""
s = input("Enter a string :")
print(len(s))

output
Enter a string :PRAKASH
7
"""

# count the number of character frequency in string
"""
s = input("Enter a string :")
b = {}
for i in s:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(str(b))

output
Enter a string :PRAKASH
{'P': 1, 'R': 1, 'A': 2, 'K': 1, 'S': 1, 'H': 1}
"""

# create a string made of the middle three characters
"""
s = input("Enter a string :")
m = len(s)//2
print(s[m-1:m+2])

output
Enter a string :PraKAsh prAkaSH
h p
"""

# create a string in upper case
"""
s = input("Enter a string :")
print(s.upper())

output
Enter a string :PrakASH prAkash
PRAKASH PRAKASH
"""

# count the fequency of each character
"""
input_string = input("Enter a string: ")

char_frequency = {}

for char in input_string:
    char_frequency[char] = char_frequency.get(char, 0) + 1

print("Character frequencies:")
for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")

output
Enter a string: PrakASH prAkash         
Character frequencies:
P: 1
r: 2
a: 2
k: 2
A: 2
S: 1
H: 1
 : 1
p: 1
s: 1
h: 1
"""

# Write a program to accept a string and count the frequency of each vowel (usecount())
"""
import re
def check_vow():
    vowels = 'aeiou'
    input_str = input("Enter a String :")
    str_list = re.findall(f'[{vowels}]',input_str,re.I)
    print(len(str_list))
    print(str_list)

print(check_vow())

output
Enter a String :prakash gohill
4
['a', 'a', 'o', 'i']
"""

# Write a Python programto append new string in the middle of a given string
"""
real_str = input("Enter a String :")
print("Real String is :",str(real_str))
split_str = real_str.split()
middle_str = "Symbiosis"
middle_pos = len(split_str)//2
split_str.insert(middle_pos,middle_str)
print("ReFormated String is : ",str(" ".join(split_str)))

output
Enter a String :PRAKASH GOHIL         
Real String is : PRAKASH GOHIL
ReFormated String is :  PRAKASH Symbiosis GOHIL
"""

# Write a Python program to arrange string characters such that lowercase letters should come first (use lower())
"""
real_str = input("Enter a String :")
print("Real String is :",str(real_str))
res = real_str[0].lower() + real_str[1:]
print("Formated String is: ",str(res))

output
Enter a String :PRAKASH
Real String is : PRAKASH
Formated String is : pRAKASH
"""

# Write a Python program to count all letters, digits, and special symbols from a given string (use isalpha(),isdigit()) 
"""
alpha = 0
input_str = input("Enter a String :")
for i in input_str:
    if(i.isalpha()):
        alpha+=1
print("Digit :",len(input_str)-alpha)
print("Alphabets :",alpha)

output
Enter a String :PrAkash 2001
Digit : 5
Alphabets : 7
"""

# Write a Python program to find all occurrences of a substring in a given string by ignoring the case
"""
import re
real_str = input("Enter a String :").lower()
print("Real String is :",str(real_str))
sub_str = "prakash"
res = [i.start() for i in re.finditer(sub_str, real_str)]
print(str(res))

output
Enter a String :Prakash prakash PRAKASH
Real String is : prakash prakash prakash
[0, 8, 16]
"""

# Write a program to count occurrences of all characters within a string
"""
real_str = input("Enter a String :")
print("Real String is :",str(real_str))
count = real_str.count('a')
print(str(count))

output
Enter a String :Prakash prakash Prakash
Real String is : Prakash prakash Prakash
2
"""

# Write a program to reverse a given string
"""
def rev(str):
    str=list(str)
    str.reverse()
    print("Reverse String is :",str)

real_str = input("Enter a String :")
print("Real String is :",str(real_str))
print(rev(real_str))

output
Enter a String :Prakash
Real String is : Prakash
Reverse String is : ['h', 's', 'a', 'k', 'a', 'r', 'P']
None
"""

# Write a program to accept a string and display the string with changed case.(Change upper case alphabet to lower case and vice versa) (use swapcase())
"""
real_str = input("Enter a String :")
print("Real String is :",str(real_str))
print("Swapcase string :",real_str.swapcase())

output
Enter a String :Prakash
Real String is : Prakash
Swapcase string : pRAKASH
"""

# Write a program to count the number of letters in a word. (use len())
"""
real_str = str(input("Enter a String :"))
print("Real String is :",str(real_str))
print("Length of string :",len(real_str))

output
Enter a String :Prakash 
Real String is : Prakash
Length of string : 7
"""

# Write a Python programto search a specific word in a string. (use ‘in’operator)
"""
real_str = str(input("Enter a String :"))
print("Real String is :",str(real_str))
find_str = "Prakash"
if find_str in real_str:
    print(f"{find_str} is present in {real_str}.")
else:
    print("Not Present.")

output
Enter a String :Hyy, I am Prakash gohil. 
Real String is : Hyy, I am Prakash gohil.
Prakash is present in Hyy, I am Prakash gohil..
"""

# Write a program in Python to count lower, upper, numeric and special characters in a string. (use islower(), isupper(), isnumeric())
"""
real_str = input("Enter a String :")
print("Real String is :",str(real_str))
lower = 0
upper = 0
number = 0
for i in real_str:
    if i.islower():
        lower+=1
    elif i.isupper():
        upper+=1
    elif i.isnumeric():
        number+=1

print("Lowercase char is :",lower)
print("Uppercase char is :",upper)
print("Number char is :",number)

output
Enter a String :1
Real String is : 1
Lowercase char is : 0
Uppercase char is : 0
Number char is : 1
"""

"""
1.Write a program to create a new string made of the middle three characters of an input string.
E.g str1 = "JhonDipPeta"  o/p Output  Dip
"""
"""
def middle_three_chars(input_str):
    length = len(input_str)
    
    if length < 3:
        return "Input string is very short"
    
    middle_index = length // 2
    return input_str[middle_index - 1:middle_index + 2]

str1 = "JhonDipPeta"
result = middle_three_chars(str1)
print("Output:", result)
Output: Dip
"""

"""
2. Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
Given: s1 = "Atul" s2 = "Patil" Expected Output:  AtPatilul
"""
"""
def append_middle(s1, s2):
    middle_index = len(s1) // 2
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    return s3

s1 = "Atul"
s2 = "Patil"
result = append_middle(s1, s2)
print("Output:", result)
Output: AtPatilul
"""

"""
3.Create a new string made of the first, middle, and last characters of each input string
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
Given: s1 = "America"  s2 = "Japan"  Expected Output: AJrpan
"""
"""
def get_first_middle_last_chars(s):
    length = len(s)
    
    if length < 3:
        return s
        
    first_char = s[0]
    middle_char = s[length // 2]
    last_char = s[-1]
    
    return first_char + middle_char + last_char

def combine_strings(s1, s2):
    result = get_first_middle_last_chars(s1) + get_first_middle_last_chars(s2)
    return result

s1 = "America"
s2 = "Japan"
result = combine_strings(s1, s2)
print("Output:", result)
Output: AraJpn
"""