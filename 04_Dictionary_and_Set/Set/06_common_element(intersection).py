#Que: Find common elements in two sets accepted from user using intersection.

set_1 = set()
for i in range(1 ,6):
    value_1 = input(f"Enter the element {i} for set-1:")
    set_1.add(value_1)

set_2 = set()
for i in range(1 ,6):
    value_2 = input(f"Enter the element {i} for set-2:")
    set_2.add(value_2)

interacted= set_1.intersection(set_2)

print("set-1 is:",set_1)
print("set-2 is:",set_2)
print("Interaction of both sets is :",interacted)