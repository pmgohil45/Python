#python program to multipy two nunbers
"""
a = int(input("Enter 1st a number : "))
b = int(input("Enter 2st a number : "))
c = a*b
print("Answer :",c)

output
Enter 1st a number : 2
Enter 2st a number : 3
Answer : 6
"""

# Python program for Arithmetic Operations
"""
a = int(input("Enter 1st a number : "))
b = int(input("Enter 2st a number : "))
print("+, -, *, /, %, //, **")
symbol = input("Enter any one symbol show as above : ")
if(symbol == "+"):
    print("Addition : ",a+b)
elif(symbol == "-"):
    print("Subtraction : ",a-b)
elif(symbol == "*"):
    print("Multiplication : ",a*b)
elif(symbol == "/"):
    print("Division : ",a/b)
elif(symbol == "%"):
    print("Moduls : ",a%b)
elif(symbol == "//"):
    print("Floor Division : ",a//b)
elif(symbol == "**"):
    print("Exponent : ",a**b)
else:
    print("Pleas, Enter a valid symbol..!")

output
Enter 1st a number : 3
Enter 2st a number : 3
+, -, *, /, %, //, **
Enter any one symbol show as above : //
Floor Division :  1
"""

# Python program to check whether the given number is even or not.
"""
a = int(input("Enter 1st a number : "))
if (a%2==0):
    print(a, "is Even number")
else:
    print(a, "is Odd number")

output
Enter 1st a number : 3
3 is Odd number

Enter 1st a number : 2
2 is Odd number
"""

#Python program to print Even Numbers from 1 to 100
"""
i=0
while(i<=100):
    if i%2==0:
        print(i)
    i=i+1

output
0
2
4
6
8
10
12
14
16
18
20
22..... 98, 100
"""

#Python program to print Odd Numbers from 1 to 100
"""
i=0
while(i<=100):
    if i%2!=0:
        print(i)
    i=i+1

output
1
3
5
7
9
11
13
15
17
19
21
23.... 97, 99
"""

# Python program to find Sum of Digits in a Number
"""
num = input("Enter a number : ")
sum = 0
for d in num:
	sum=sum+int(d)
print("sum of each digit :",sum)

output
Enter a number : 15
sum of each digit : 6
"""

# Python program to check whether the given integer is a multiple of 5
"""
n = int(input("Enter a number : "))
if n%5==0:
    print("Multiple of 5")
else:
    print("Not Multiple of 5")

output
Enter a number : 25
Multiple of 5

Enter a number : 24
Not Multiple of 5
"""

# Python program to find Cube of a Number
"""
n = int(input("Enter a number : "))
c=n*n*n
print("Cube of",n,"is",c)

output
Enter a number : 3
Cube of 3 is 27
"""

#Python program to find Largest of 2 Numbers
"""
n1 = int(input("Enter a n1 : "))
n2 = int(input("Enter a n2 : "))
if(n1>n2):
    print(n1," is largest than ",n2)
else:
    print(n2," is largest than ",n1)

output
Enter a n1 : 3
Enter a n2 : 2
3  is largest than  2
"""

#Python program to find Largest of 3 Numbers
"""
n1 = int(input("Enter a n1 : "))
n2 = int(input("Enter a n2 : "))
n3 = int(input("Enter a n3 : "))
if(n1>n2):
    print(n1," is large than ",n2," & ",n3)
elif(n2>n3):
    print(n2," is large than ",n1," & ",n3)
else:
    print(n3," is large than ",n1," & ",n2)

output
Enter a n1 : 2
Enter a n2 : 5
Enter a n3 : 4
5  is large than  2  &  4
"""

# Python program to check whether the given integer is a multiple of both 5 and 7
"""
n = int(input("Enter a n1 : "))
if n%5==0:
    print(n,"is multiple of 5.")
elif n%7==0:
    print(n,"is multple of 7.")
else:
    print("not multiple with 5 & 7.")

output
Enter a n1 : 40
40 is multiple of 5.

Enter a n1 : 41
not multiple with 5 & 7.

Enter a n1 : 42
42 is multple of 7.
"""


# Python program to display all the multiples of 3 within the range 10 to 50
"""
i = 10
while i<=50:
    if i%3==0:
        print("3 is multiple with",i)
    i+=1

output
3 is multiple with 12
3 is multiple with 15
3 is multiple with 18
3 is multiple with 21
3 is multiple with 24
3 is multiple with 27
3 is multiple with 30
3 is multiple with 33
3 is multiple with 36
3 is multiple with 39
3 is multiple with 42
3 is multiple with 45
3 is multiple with 48
"""

# Python program to find the average of 10 numbers using while loop
"""
n = int(input("Enter a number :"))
sum = 0
avg = 0
i = 1
while i<=n:
    print("i :",i)
    sum=sum+n
    i=i+1
    
avg=sum/n
print("avg :",avg)

output
Enter a number :10
i : 1
i : 2
i : 3
i : 4
i : 5
i : 6
i : 7
i : 8
i : 9
i : 10
avg : 10.0
"""

# Python program to display the given integer in reverse manner
"""
num = int(input("Enter a numner :"))
rnum = 0
while num>0:
    r=num%10
    rnum=(rnum*10)+r
    num = num//10
print("reverse number :",rnum)

output
Enter a numner :12
reverse number : 21
"""

# Python program to find the sum of the digits of an integer using while loop
"""
num = int(input("Enter a numner :"))
tot = 0
while num>0:
    d=num%10
    tot=tot+d
    num=num//10

print("total sum of digit :",tot)

output
Enter a numner :12
total sum of digit : 3
"""
"""
# Python program to display all integers within the range 100-200 whose sum of digits is an even number
def sum_of_digits_is_even(number):
    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum % 2 == 0

for num in range(100, 201):
    if sum_of_digits_is_even(num):
        print(num)
output
101
103
105
107
109
110
112
114
116
118
121... 198, 200
"""

# Python program to check whether the given integer is a prime number or not
"""
n = int(input("Enter number : "))
def check_prime(n):
    if n<=1:
        return False
    
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    
    return True # If no factors are found, the number is prime

if check_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
    
output
Enter number : 97
97 is a prime number.
"""

# Python program to generate the prime numbers from 1 to N
"""
n = int(input("Enter number : "))
def check_prime(n):
    if n<=1:
        return False

    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    
    return True

prime_numbers = [i for i in range(1,n) if check_prime(i)]
print("Prime numbers from 1 to 100:")
print(prime_numbers)

output
Enter number : 100
Prime numbers from 1 to 100:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""

# Python program for Leap Year
"""
y = int(input("Enter a year :"))
if y%4==0:
    print(y,"is leap year.")
else:
    print(y,"is not leap year.")

output
Enter a year :2024
2024 is leap year.
"""

# To check whether a given number is an Armstrong number or not in Python
"""
n = int(input("Enter a number :"))
n1=n
length = len(str(n))
sum = 0
while n!=0:
    remainder=n%10
    sum+=remainder**length #exponent
    n//=10
if n1==sum:
    print(n1,"is armstrong number")
else:
    print(n1,"is not armstrong number")

output
Enter a number :153
153 is armstrong number

dryrun
1^3 + 5^3 + 3^3 = 153

Enter a number :8
8 is armstrong number

dryrun
8^1 = 8*1 = 8
"""
# Python Program to Count Number of Digits in a Armstrong Number
"""
num = int(input("Enter a number: "))
length = len(str(num))
if num == sum(int(i) ** length for i in str(num)):
    print(f"{num} is an Armstrong number with {length} digits.")
else:
    print(f"{num} is not an Armstrong number.")

output
Enter a number: 153
153 is an Armstrong number with 3 digits.
"""

# Python Program to Print Fibonacci Series
"""
n = int(input("Enter a number :"))
n1=0; n2=1; c=0
while n>c:
    print(n1)
    tot=n1+n2
    n1=n2
    n2=tot
    c+=1

output
Enter a number :7
0
1
1
2
3
5
8
"""

# Python example to find Factors of a Number
"""
n = int(input("Enter a number :"))
f=1
for i in range(1,n+1):
    f=f*i
    print(f)
    i+=1

output
Enter a number :5
1
2
6
24
120
"""

# Python example to find Factorial of a Number
"""
n = int(input("Enter a number to find its factorial: "))
res = 1
if n>0:
    for i in range(1, n + 1):
        res *= i
    print(f"The factorial of {n} is {res}.")
else:
    print(res)

output
Enter a number to find its factorial: 10
The factorial of 10 is 3, 628, 800.
"""

"""
 Python program to find GCD of Two Numbers
 Python program to find LCM of Two Numbers
"""
"""
import math
n1 = int (input("Enter a number 1 :"))
n2 = int (input("Enter a number 2 :"))
print("the GCD of",n1,"and",n2,"is",math.gcd(n1,n2))
print("the LCM of",n1,"and",n2,"is",math.lcm(n1,n2))

output
Enter a number 1 :2
Enter a number 2 :50
the GCD of 2 and 50 is 2
the LCM of 2 and 50 is 50
"""
# Python program to check Palindrome Number
"""
n = int(input("Enter a number :"))
temp = n
revers = 0
while n>0:
    d=n%10
    revers=revers*10+d
    n=n//10
if temp==revers:
    print(revers,"is palindrome number.")
else:
    print(revers,"is not palindrome number.")

output
Enter a number :121
121 is palindrome number.
"""

"""
1
12
123
1234
12345
"""
"""
n=int(input("Enter a number :"))
i=0
j=1
for i in range(n):
    for j in range(0,i+1):
        print(j+1,end="")
    print("\r")

output
Enter a number :5
1
12
123
1234
12345
"""