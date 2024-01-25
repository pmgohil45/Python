# 1²+2²+3²+….+n²
"""
n=int(input("Enter a number : "))
res=0
for i in range(1, n+1):
    res=res+i**2

print("Sum of Square : ",res)
output
Enter a number : 3
Sum of Square :  14
"""

# 1/1! 2/2! 3/3!... 1/n!
"""
import math
n=int(input("Enter a number : "))
res=0
for i in range(1,n+1):
    res+=i/math.factorial(i)
print("Sum of given series : ",res)
output
Enter a number : 3
Sum of given series :  2.5
"""

# [1+(1+2)+(1+2+3)+–+(1+2+3+–+n)]
"""
n=int(input("Enter a number : "))
res=0;sum=0
for i in range(1,n+1):
    sum+=i
    res+=sum
print("Result : ",res)
output
Enter a number : 3
Result :  10
"""

# 1 + 1/2 + 1/3 + ... + 1/n..
"""
n=int(input("Enter a number : "))
res=0
for i in range(1,n+1):
    res+=1/i
print("Sum of Series: ",res)
output
Enter a number : 3
Sum of Series:  1.8333333333333333
"""