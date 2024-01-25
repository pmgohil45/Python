# Replace each element in a list L with its square.
"""
list1 = [1,2,3]
list2 = [3,2,6]

res = []
for i in list1:
    for j in list2:
        if i==j:
            res.append(list1.index(j))

print("initial 2 list are")
print(list1, "\n", list2)
print("Second list after replacement is:", res)

output
initial 2 list are
[1, 2, 3] #index value 0,1,2,...
[3, 2, 6] #index value 0,1,2,...
Second list after replacement is: [1, 2]
"""