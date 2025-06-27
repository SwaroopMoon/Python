#Que: Accept 5 integers as input from user and create a set and check if 3 is present in the set.

# I/P:

member=()
for i in range(1, 6):
    val = int(input(f"Enter the element{i}:"))    
member.add(val)                                       #To add values inside set "member'
print("3 is present in set?", 3 in member)


#An f-string (short for formatted string literal) is a super-convenient way
#  to embed variables or expressions directly inside a string.
#  It was introduced in Python 3.6 and has become the go-to method for string formatting.