"""
Write a Python program that performs the following actions for managing order records:
 1. Allow the user to input the details of ten orders one by one: order_date, number_of-items, total. 
 2. Use the name of each order as a key in the dictionary and store number_of-items, total. as a tuple value. 
 3. Calculate and print the average number_of-items, all the orders in the records. Find the order with the highest total and print its details
"""
"""
o_reco = {}
for i in range(1,10+1): # otherwise we set as a 11 or 10+1 like n+1  #condition 1st
    o_name=input(f"Enter a order name {i}: ")
    o_item=int(input(f"Enter a number of items of {o_name}: "))
    o_total=int(input(f"Enter a total price of {o_name}: "))

    o_reco[o_name]=(o_item,o_total) #condition 2nd

fetch_item = sum(item[0] for item in o_reco.values()) #condition 3rd(A)
average = fetch_item / len(o_reco)
print(f"Average of order items: {average}")

highest = max(o_reco, key=lambda k: o_reco[k][1]) #condition 3rd(B)

print(f"Name of order: {highest}")
print(f"Items: {o_reco[highest][0]}")
print(f"Total: {o_reco[highest][1]}")


output
Enter a order name 1: a
Enter a number of items of a: 6
Enter a total price of a: 66
Enter a order name 2: b
Enter a number of items of b: 1
Enter a total price of b: 22
Enter a order name 3: c
Enter a number of items of c: 5
Enter a total price of c: 66
Enter a order name 4: d
Enter a number of items of d: 65
Enter a total price of d: 655
Enter a order name 5: e
Enter a number of items of e: 554
Enter a total price of e: 112
Enter a order name 6: f
Enter a number of items of f: 56
Enter a total price of f: 1212
Enter a order name 7: g
Enter a number of items of g: 9
Enter a total price of g: 52
Enter a order name 8: h
Enter a number of items of h: 12
Enter a total price of h: 33
Enter a order name 9: i
Enter a number of items of i: 223
Enter a total price of i: 233
Enter a order name 10: j
Enter a number of items of j: 32
Enter a total price of j: 23
Average of order items: 96.3
Name of order: f
Items: 56
Total: 1212
"""

"""
Write a  program that takes in the the number of terms and finds the 
sum of series: 1 + x^2/2 + x^3/3 + … x^n/n.
"""

n=int(input("Enter the value of N: "))
x=int(input("Enter the value of X: "))
sum=0; formula=0
for i in range(1, n+1):
    formula = (x**i)/i
    sum+=formula

print(f"Sum of Series: {sum}")

"""
dryrun
n=5
x=4
i   formula     sum
1   4((4^1)/1)  4
2   8((4^2)/2)  12
3   32          44
4   
5   
"""
