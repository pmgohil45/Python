# write a program that calculates euclidian distance between two points 
"""
import math
x1 = int(input("Enter a x1 : "))
y1 = int(input("Enter a y1 : "))
x2 = int(input("Enter a x2 : "))
y2 = int(input("Enter a y2 : "))

d=math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("The Euclidean Distance is "+str(d))

output
Enter a x1 : 1
Enter a y1 : 3
Enter a x2 : 2
Enter a y2 : 5
The Euclidean Distance is 2.23606797749979
"""

# write a program to find out sum of all digits using while loop
"""
num = int(input("Enter a number : "))
sum = 0
while num > 0:
    sum = num % 10
    sum += num
    num //= 10
print("sum of each digit :",sum)

output
Enter a number : 19
sum of each digit : 2
"""

# WAP that checks if given word is pallindrome or not.
"""
word = input("Enter a word :")
word = word.lower()
rword = word[::-1]
if word==rword:
    print(word," is pallindrome.")
else:
        print(word," is not pallindrome.")

output
Enter a word :ABA
aba  is pallindrome.
"""