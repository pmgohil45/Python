"""
Write a program that keeps student's name and his marks in a dictionary as key-value pairs. The program 
should store records of 10 students and display students name and marks of five students in decreasing 
order of marks obtained.
"""
"""
student_records = {}

for i in range(10):
    name = input(f"Enter student {i + 1}'s name: ")
    marks = float(input(f"Enter {name}'s marks: "))
    student_records[name] = marks

sorted_records = dict(sorted(student_records.items(), key=lambda item: item[1], reverse=True))

print("\nTop 5 students:")
count = 0
for name, marks in sorted_records.items():
    if count >= 5:
        break
    print(f"{name}: {marks}")
    count += 1

output
Enter student 1's name: 1
Enter 1's marks: 33
Enter student 2's name: 2
Enter 2's marks: 33
Enter student 3's name: 3
Enter 3's marks: 55
Enter student 4's name: 4
Enter 4's marks: 44
Enter student 5's name: 5
Enter 5's marks: 666
Enter student 6's name: 6
Enter 6's marks: 45
Enter student 7's name: 7
Enter 7's marks: 65
Enter student 8's name: 8
Enter 8's marks: 54
Enter student 9's name: 9
Enter 9's marks: 11
Enter student 10's name: 10
Enter 10's marks: 99

Top 5 students:
5: 666.0
10: 99.0
7: 65.0
3: 55.0
8: 54.0
"""
"""	
Write a program that keeps name and birthday in a dictionary as key-value pairs. The program should 
display a menu that lets the user search a person’s birthday, add a new name and birthday, change an 
existing birthday, and delete an existing name and birthday.
"""
"""
user_data = {}

def display_menu():
    print("1. Search for a person's birthday")
    print("2. Add a new name and birthday")
    print("3. Change an existing birthday")
    print("4. Delete an existing name and birthday")
    print("5. Exit")

def search_birthday(user_data):
    name = input("Enter the name to search for: ")
    if name in user_data:
        print(f"{name}'s birthday is on {user_data[name]}")
    else:
        print(f"{name} not found in user_data.")

def add_birthday(user_data):
    name = input("Enter the name: ")
    birthday = input("Enter the birthday: ")
    user_data[name] = birthday
    print(f"{name}'s birthday added to user_data.")

def change_birthday(user_data):
    name = input("Enter the name whose birthday you want to change: ")
    if name in user_data:
        new_birthday = input("Enter the new birthday: ")
        user_data[name] = new_birthday
        print(f"{name}'s birthday updated.")
    else:
        print(f"{name} not found in user_data.")

def delete_birthday(user_data):
    name = input("Enter the name whose birthday you want to delete: ")
    if name in user_data:
        del user_data[name]
        print(f"{name}'s birthday deleted from user_data.")
    else:
        print(f"{name} not found in user_data.")

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        search_birthday(user_data)
    elif choice == '2':
        add_birthday(user_data)
    elif choice == '3':
        change_birthday(user_data)
    elif choice == '4':
        delete_birthday(user_data)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
"""