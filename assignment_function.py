"""
Write a function find_max that accepts four numbers as arguments and returns the largest number among four. 
Write another function main, in main() function accept four numbers from user and call find_max
"""
"""
def main():
    n1 = input("Enter a number 1 :")
    n2 = input("Enter a number 2 :")
    n3 = input("Enter a number 3 :")
    n4 = input("Enter a number 4 :")
    find_max(n1,n2,n3,n4)


def find_max(n1,n2,n3,n4):
    num=0
    if n1>n2 and n1>n3 and n1>n4:
        num=n1
        print(num+" is big")
    elif n2>n3 and n2>n4 and n2>n1:
        num=n2
        print(num+" is big")
    elif n3>n4 and n3>n1 and n3>n2:
        num=n3
        print(num+" is big")
    elif n4>n1 and n4>n2 and n4>n3:
        num=n4
        print(num+" is big")

    return num

print(main())

output
Enter a number 1 :2
Enter a number 2 :5
Enter a number 3 :6
Enter a number 4 :44
6 is big
"""

"""
Write a definition of a method count_in(student) to find and display those student names, in which there are more 
than 5 characters…use variable to store values.
"""	
"""
nm = input("Enter a name :")

def count_in(nm):
    storeNm = "0"
    if len(nm)>5:
        storeNm=nm
    else:
        print(nm+" is less than 5.")
    
    return storeNm

print(count_in(nm))

output
Enter a name :prakash
prakash
"""

"""
Write the definition of a function zero_ending(scores). Pass 5 to it. Display sum of the numbers which are 
ending with zero.
"""	
"""
scores1 = int(input("Enter a Scores 1:"))
scores2 = int(input("Enter a Scores 2:"))
scores3 = int(input("Enter a Scores 3:"))
scores4 = int(input("Enter a Scores 4:"))
scores5 = int(input("Enter a Scores 5:"))

def zero_ending(n1,n2,n3,n4,n5):
    sum=n1+n2+n3+n4+n5
    last_digit=sum%10
    if last_digit==0:
        print(sum)
    else:
        print(str(sum)+" of last digit is not a zero.")

zero_ending(scores1,scores2,scores3,scores4,scores5)

output
Enter a Scores 1:2
Enter a Scores 2:3
Enter a Scores 3:6
Enter a Scores 4:4
Enter a Scores 5:5
20

Enter a Scores 1:1
Enter a Scores 2:2
Enter a Scores 3:3
Enter a Scores 4:4
Enter a Scores 5:5
15 of last digit is not a zero.
"""

"""
Write a function named is_prime, which takes an integer as an argument and returns true if the argument 
is a prime number, or false otherwise. Also, write the main function that displays prime numbers between 1 to 100
"""
"""
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    print("Prime numbers between 1 and 100:")
    for num in range(1, 101):
        if is_prime(num):
            print(num, end=" ")

main()
Prime numbers between 1 and 100:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
"""

"""
Write a function, is_vowel that returns the value true if a given character is a vowel, and otherwise 
returns false. Write another function main, in main() function accept a string from user and count number of 
vowels in that string.
"""
"""
import re

str1 = input("Enter a string :")

def is_vowel(input_str) :
    vowel ="AaEeIiOoUu"
    str_list = re.findall(f'[{vowel}]',input_str,re.I)
    print("Vowels :",str_list)
    main(str_list)

def main(str_l):
    print("Total vowels :",len(str_l))

is_vowel(str1)

Enter a string :prakash
Vowels : ['a', 'a']
Total vowels : 2
"""