size = int(input("Enter a number: "))
r = int(input("Enter a range: "))
for k in range(r):
    for i in range(size):
        for j in range(i+1):
            if i == j :
                print("*", end="")
            else:
                print(" ", end="")
        print()

    for i in range(size-2, 0, -1):
        for j in range(size):
            if i == j :
                print("*", end="")
            else:
                print(" ", end="")
        print() 

"""
output:
Enter a number: 6
Enter a range: 3
*
 *
  *
   *
    *
     *
    *
   *
  *
 *
*
 *
  *
   *
    *
     *
    *
   *
  *
 *
*
 *
  *
   *
    *
     *
    *
   *
  *
 *
"""
