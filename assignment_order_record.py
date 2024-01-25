"""
Write a Python program that performs the following actions for managing order records:
 1. Allow the user to input the details of ten orders one by one: order_date, number_of-items, total. 
 2. Use the name of each order as a key in the dictionary and store number_of-items, total. as a tuple value. 
 3. Calculate and print the average number_of-items, all the orders in the records. Find the order with the highest total and print its details
"""
"""
# Initialize an empty dictionary to store order records
order_records = {}

# Input details for ten orders one by one
for i in range(1, 3):
    order_name = input(f"Enter the name of order {i}: ")
    order_date = input(f"Enter the order date for {order_name}: ")
    number_of_items = int(input(f"Enter the number of items for {order_name}: "))
    total = float(input(f"Enter the total for {order_name}: "))
    
    # Store number_of_items and total as a tuple value
    order_records[order_name] = (number_of_items, total)

# Calculate the average number_of_items for all orders
total_items = sum(item[0] for item in order_records.values())
average_items = total_items / len(order_records)

print(f"Average number of items for all orders: {average_items}")

# Find the order with the highest total
max_total_order = max(order_records, key=lambda k: order_records[k][1])

print(f"The order with the highest total is '{max_total_order}' with details:")
print(f"Order Date: {order_date}")
print(f"Number of Items: {order_records[max_total_order][0]}")
print(f"Total: {order_records[max_total_order][1]}")

output
Enter the name of order 1: a
Enter the order date for a: 1/1/1
Enter the number of items for a: 2
Enter the total for a: 4
Enter the name of order 2: b
Enter the order date for b: 2/2/2
Enter the number of items for b: 6
Enter the total for b: 3
Average number of items for all orders: 4.0
The order with the highest total is 'a' with details:
Order Date: 2/2/2
Number of Items: 2
Total: 4.0
"""