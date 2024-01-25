"""
Write a Python function that computes the harmonic sum of n. Accept n from user.
Harmonic Sum = (1/2) + (1/4) + (1/8) + (1/16) + ….. + (1/2n)
"""
"""
def harmonic_sum(n):
    tot = 0
    for i in range(1, n+1):
        tot += 1/(2**i)
    return tot

num = int(input("Enter a value of N: "))
print("Harmonic Sum is : ",harmonic_sum(num))

output
Enter a value of N: 2
Harmonic Sum is :  0.75
"""

# Write a python program to accept two 3X4 matrices and display their addition and multiplication
"""
def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter position of element({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def sum_matrix(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

row = int(input("Enter a Rows :"))
col = int(input("Enter a Cols :"))

print("Enter elements for the first matrix:")
m1 = input_matrix(row, col)

print("\nEnter elements for the second matrix:")
m2 = input_matrix(row, col)

print("Display Matrix 1 : ")
display_matrix(m1)

print("Display Matrix 2 : ")
display_matrix(m2)

print("Sum of Matrix(1+2) : ",sum_matrix(m1,m2))

output
Enter a Rows :3
Enter a Cols :4
Enter elements for the first matrix:
Enter position of element(1, 1): 2
Enter position of element(1, 2): 2
Enter position of element(1, 3): 2
Enter position of element(1, 4): 2
Enter position of element(2, 1): 2
Enter position of element(2, 2): 2
Enter position of element(2, 3): 2
Enter position of element(2, 4): 2
Enter position of element(3, 1): 2
Enter position of element(3, 2): 2
Enter position of element(3, 3): 2
Enter position of element(3, 4): 2

Enter elements for the second matrix:
Enter position of element(1, 1): 3
Enter position of element(1, 2): 4
Enter position of element(1, 3): 4
Enter position of element(1, 4): 4
Enter position of element(2, 1): 4
Enter position of element(2, 2): 4
Enter position of element(2, 3): 4
Enter position of element(2, 4): 4
Enter position of element(3, 1): 4
Enter position of element(3, 2): 4
Enter position of element(3, 3): 4
Enter position of element(3, 4): 4
Display Matrix 1 :
2 2 2 2
2 2 2 2
2 2 2 2
Display Matrix 2 :
3 4 4 4
4 4 4 4
4 4 4 4
Sum of Matrix(1+2) :  [[5, 6, 6, 6], [6, 6, 6, 6], [6, 6, 6, 6]]
"""

"""
Write a Python program that performs the following operations on a given input string:
length, uppercase, lowercase, Count the number of vowels in the string, Count the number of consonants 
in the string, Reverse the string, print total number of words in the string, Capitalizes the first 
letter of each word in the string
"""
"""
def check_vowels_consonants(line):
    v=0;c=0
    for i in line:
        if i=='A' or i=='a' or i=='E' or i=='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u':
            v=v+1
        else:
            c=c+1

    print("Count of Vowels : ",v)
    print("Count of Consonants : ",c)

def rev(str):
    str=list(str)
    str.reverse()
    return str

line1 = input("Enter a anything which you want : ")
print("Length of String : ",len(line1))
print("String in Uppercase : ",line1.upper())
print("String in Lowercase : ",line1.lower())
check_vowels_consonants(line1)
print("Reverse String is :",rev(line1))
print("Number of words in string : ",len(line1.split()))
print("Capitalization of each word available in String : ",line1.title())

output
Enter a anything which you want : my name is prakash
Length of String :  18
String in Uppercase :  MY NAME IS PRAKASH
String in Lowercase :  my name is prakash
Count of Vowels :  5
Count of Consonants :  13
Reverse String is : ['h', 's', 'a', 'k', 'a', 'r', 'p', ' ', 's', 'i', ' ', 'e', 'm', 'a', 'n', ' ', 'y', 'm']
Number of words in string :  4
Capitalization of each word available in String :  My Name Is Prakash
"""

"""
Write a python program with a function for given a simple list of objects like string or integers as a 
parameter, checks whether there are duplicate elements in the list and return True of False accordingly. 
The input list should not be changed.
"""
"""
def has_duplicates(line1):
    l1=list(line1)
    seen = set() 
    for i in l1:
        if i in seen:
            return True
        seen.add(i)
    return False

line1 = input("Enter a anything : ")

result = has_duplicates(line1)
if result:
    print("The list contains duplicate elements.")
else:
    print("The list does not contain duplicate elements.")

output
Enter a anything : prakash
The list contains duplicate elements.

Enter a anything : pra
The list does not contain duplicate elements.
"""

"""
Write a python program to create a function called collatz() which reads as parameter named number. 
If the number is even it should print and return number //2 and if the number is odd then it should 
print and return 3*number+1. The function should keep calling on that number until the function 
returns a value 1.
"""
"""
def collatz(number):
    if number % 2 == 0:
        print("Even : ",number)
        number = number // 2
        print("number // 2 : ",number)
    else:
        print("Odd : ",number)
        number = 3 * number + 1
        print("3 * number + 1 : ",number)
    return number

num = int(input("Enter a number: "))
print("The final result is: ",collatz(num))

ouput
Enter a number: 10
Even :  10
number // 2 :  5
The final result is:  5

Enter a number: 9
Odd :  9
3 * number + 1 :  28
The final result is:  28
"""

"""
Print the following table using list :
    2 3 4 5 6 7 
    3 4 5 6 7 8 
    4 5 6 7 8 9 
    5 6 7 8 9 10 
    6 7 8 9 10 11 
    7 8 9 10 11 12

"""
"""
table = [
    [2,3,4,5,6,7],
    [3,4,5,6,7,8],
    [4,5,6,7,8,9],
    [5,6,7,8,9,10],
    [6,7,8,9,10,11],
    [7,8,9,10,11,12]
]

for row in table:
    for number in row:
        print(number, end=" ")
    print()

output
2 3 4 5 6 7 
3 4 5 6 7 8 
4 5 6 7 8 9 
5 6 7 8 9 10
6 7 8 9 10 11
7 8 9 10 11 12
"""