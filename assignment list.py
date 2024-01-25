# Write a program that generates a list L of 50 random numbers  between 1 and 100.
"""
import random

random_list = []
num = 50
for i in range(num):
    random_list.append(random.randint(1,50))
print(random_list)

output
[14, 7, 48, 31, 7, 40, 36, 8, 16, 24, 38, 24, 48, 47, 2, 7, 1, 46, 27, 5, 25, 22, 8, 31, 42, 37, 17, 28, 50, 12, 48, 12, 31, 11, 43, 9, 28, 43, 26, 21, 20, 29, 26, 3, 32, 20, 18, 42, 30, 39]
"""

# Replace each element in a list L with its square.
"""
try:
    print("Press two times Enter to terminate list1 :")
    list1 = []
    while True:
        list1.append(int(input()))
except:
    print("list is ",list1)

try:
    print("Press two times Enter to terminate list2:")
    list2 = []
    while True:
        list2.append(int(input()))
except:
    print("list is ",list2)
    
#list1 = [1,2,3]
#list2 = [1,2,3]

res = []
for i in list1:
    for j in list2:
        if i==j:
            res.append(list1.index(j))

print("initial 2 list are")
print(list1, "\n", list2)
print("Second list after replacement is:", res)

output
Press two times Enter to terminate list1 :
1
2
3

list is  [1, 2, 3]
Press two times Enter to terminate list2:
1
2
3

list is  [1, 2, 3]
initial 2 list are
[1, 2, 3] 
 [1, 2, 3]
Second list after replacement is: [0, 1, 2]
"""

# Count how many items in a list L are greater than 50.
"""
L = [65, 23, 78, 49, 37, 62]
count = 0
for i in L:
    if i > 50:
        count += 1

print(f"Number of items greater than 50: {count}")

output
Number of items greater than 50: 3
"""

# flip the order of the entries in the lists below  L = [[1,2], [3,4], [5,6]]
"""
l = [[1,2],[3,4],[5,6]]
new_list = l[::-1]
print("New List : ",new_list)

output
New List :  [[5, 6], [3, 4], [1, 2]]
"""

# Create a 3X3X3 list each element in list need to be zero.
"""
import pprint

c1 = int(input("Inner Column : "))
c2 = int(input("Outer Column : "))
r1 = int(input("Row 1 : "))

list1=[[['0' for col in range(c1)] for col in range(c2)] for row in range(r1)]
pprint.pprint(list1)

output
Inner Column : 3
Outer Column : 3
Row 1 : 3
[[['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']],
 [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']],
 [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]]
"""

# Make a function that sums the list mylist = [1,2,3,4,5]
"""
import operator
list1 = [1,2,3,4,5] ;s=0
for i in list1:
    s=s+operator.add(0,i)
print("sum of list 1 is :",s)

output
sum of list 1 is : 15
"""

# Take two 3X4 matrices and display their addition.
"""
m1 = [[1,2,3],
	  [4,5,6],
	  [7,8,9],
      [3,6,9]]

m2 = [[9,8,7],
	  [6,5,4],
	  [3,2,1],
      [7,4,1]]

res = [[0,0,0],
		 [0,0,0],
	     [0,0,0],
       	 [0,0,0]]

for i in range(len(m1)):
	for j in range(len(m1[0])):
		res[i][j] = m1[i][j] + m2[i][j]

for r in res:
	print(r)

output
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]
"""

"""
    write a program that returns a list that contains only the elements that are common between the 
    lists (without duplicates). Make sure your program works on two lists of different sizes.
"""
"""
l1 = [1,2,3,4,5]
l2 = [11,12,13,4,15,5]
setA = set(l1)
setB = set(l2)
 
if (setA & setB):
    print("Common Elements is : ",setA & setB)
else:
    print("No common elements")

output
Common Elements is :  {4, 5}
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
# Accept five numbers from user and store them in list. Display positive if number is positive else negative
"""
try:
    print("Press two times Enter to terminate list1 :")
    list1 = []
    while True:
        list1.append(int(input()))
except:
    print("list is ",list1)

pos_count, neg_count = 0, 0
for num in list1:
	if num >= 0:
		pos_count += 1

	else:
		neg_count += 1

print("Positive numbers in the list : ", pos_count)
print("Negative numbers in the list : ", neg_count)

output
Press two times Enter to terminate list1 :
2
-6
9
-8
5
10

list is  [2, -6, 9, -8, 5, 10]
Positive numbers in the list :  4
Negative numbers in the list :  2
"""
# Accept five values from user. Store them in list & apply sort , max and min function on list
"""
try:
    print("Press two times Enter to terminate list1 :")
    list1 = []
    while True:
        list1.append(int(input()))
except:
    print("list is ",list1)

a = list1.sort()
b = list1.index(min(list1))
c = list1.index(max(list1))

print("Sort : ",a)
print("Min : ",b)
print("Max : ",c)

output
Press two times Enter to terminate list1 :
1
2
3
-4 

list is  [1, 2, 3, -4]
Sort :  None
Min :  0
Max :  3
"""

# Write a Python program to find the list of words that are longer than n from a given list of words.
"""
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
    
print(long_words(3, "Write a Python program to find the list of words that are longer than n from a given list of words"))

output
['Write', 'Python', 'program', 'find', 'list', 'words', 'that', 'longer', 'than', 'from', 'given', 'list', 'words']
"""