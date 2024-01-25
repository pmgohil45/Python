# Python Program to Multiply Two numbers
"""
a = int(input("Enter 1st a number : "))
b = int(input("Enter 2st a number : "))
c = a*b
if (c/2==0):
    print(c, "is Even number")
else:
    print(c, "is Odd number")

output
Enter 1st a number : 5
Enter 2st a number : 5
25 is Odd number
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
Enter 1st a number : 5
Enter 2st a number : 2
+, -, *, /, %, //, **
Enter any one symbol show as above : **
Exponent :  25
"""

# Python program to check whether the given number is even or not.
"""
a = int(input("Enter 1st a number : "))
if (a%2==0):
    print(a, "is Even number")
else:
    print(a, "is Odd number")

output
Enter 1st a number : 10
10 is Even number
"""

#Python program to print Even Numbers from 1 to 100
"""
i=0
while(i<=100):
    if i%2==0:
        print(i)
    i=i+1
    
for i in range(1,100):
    if i%2==0:
        print(i)

output
print even number from 1 to 100 number
"""

#Python program to print Odd Numbers from 1 to 100
"""
i=1
while(i<=100):
    if i%2!=0:
        print(i)
    i=i+1

for i in range(1,100):
    if i%2!=0:
        print(i)

print odd number from 1 to 100 number
"""

#Python program to find Largest of 2 Numbers
"""
n1 = int(input("Enter a n1 : "))
n2 = int(input("Enter a n2 : "))
if(n1>n2):
    print(n1," is large than ",n2)
else:
    print(n2," is large than ",n1)

output
Enter a n1 : 10
Enter a n2 : 20
20  is large than  10
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
Enter a n1 : 10
Enter a n2 : 30
Enter a n3 : 20
30  is large than  10  &  20
"""

"""
Write a program that asks the user to enter a length in centimeters. If the user  enters a negative
length, the program should tell the user that the entry is  invalid. Otherwise, the program should 
convert the length to inches and print out  the result. There are 2.54 centimeters in an inch.
"""
"""
cm = int(input("Enter a centimeters : "))
if(cm>0):
    print(f"Centimiter: {cm}")
else:
    print(cm,"is invalid or nagative value.")
    print(cm,"Converted to inch.")
    print(cm*2.54,"inch")

output
Enter a centimeters : -2
-2 is invalid or nagative value.
-2 Converted to inch.
-5.08 inch
"""

"""
Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature is in.
Your program should convert the temperature  to the other unit.

1 celsius = 33.8 fahrenheit
1 fahrenheit = -17.2 celsius
"""
"""
unit = input("Enter your weather temperature unit in Celsius or Fahrenheit (c/f):")
n1 = int(input("Enter Your Weather Temperature :"))
if(unit=='c' or unit=='C'):
    a=n1*33.8
    print("Celsius convert to Fahrenheit is : ",a)
elif(unit=='f' or unit=='F'):
    a=n1*(-17.2)
    print("Fahrenheit convert to Celsius is : ",a)
else:
    print("Enter a valid Choise.!")

output
Enter your weather temperature unit in Celsius or Fahrenheit (c/f):f
Enter Your Weather Temperature :10
Fahrenheit convert to Celsius is :  -172.0
"""

"""
Ask the user to enter a temperature in Celsius. The program should print a  message based on the
temperature:
If the temperature is less than -273.15, print that the temperature is invalid  because it is below absolute zero.
If it is exactly -273.15, print that the temperature is absolute 0.
If the temperature is between -273.15 and 0, print that the temperature is  below freezing.
If it is 0, print that the temperature is at the freezing point.
If it is between 0 and 100, print that the temperature is in the normal range.
If it is 100, print that the temperature is at the boiling point.
If it is above 100, print that the temperature is above the boiling point.
"""
"""
n1 = int(input("Enter Your Weather Temperature :"))
if(-273.15>n1):
    print(f"{n1} temperature is invalid  because it is below absolute zero.")
elif(-273.15==n1):
    print(f"{n1} temperature is absolute 0.")
elif(-273.15<n1 and 0>n1):
    print(f"{n1} the temperature is below freezing.")
elif(0==n1):
    print(f"{n1} temperature is at the freezing point.")
elif(0<n1 and 100>n1):
    print(f"{n1} temperature is in the normal range.")
elif(100==n1):
    print(f"{n1} temperature is at the boiling point.")
elif(100<n1):
    print(f"{n1} temperature is above the boiling point.")

output
Enter Your Weather Temperature :-88
-88 the temperature is below freezing.
"""

