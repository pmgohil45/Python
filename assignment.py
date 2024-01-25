# Arrange string characters such that lowercase letters should come first
"""
input_str = input("Enter a string which you want..: ")
lowercase_chars = []
uppercase_chars = []

for char in input_str:
    if char.islower():
        lowercase_chars.append(char)
    else:
        uppercase_chars.append(char)

sorted_string = ''.join(lowercase_chars + uppercase_chars)
print(sorted_string)

output
Enter a string which you want..: PRakaSh GohIL
akahohPRS GIL
"""

# Calculate the sum and average of the digits present in a string
"""
num = input("Enter a Number : ")
digit_sum = 0
digit_count = 0
for char in num:
    if char.isdigit():
        digit_sum += int(char)
        digit_count += 1
print(f"Sum of digits: {digit_sum}")
    
if digit_count > 0:
    average = digit_sum / digit_count
else:
    average = 0  # To handle the case when there are no digits in the string
print(f"Average of digits: {average}")

output
Enter a Number : Prakash45
Sum of digits: 9
Average of digits: 4.5
"""