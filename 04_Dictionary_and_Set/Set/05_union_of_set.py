#Que : Input two sets from user and find the union using a set operator.

#I/P:

set_1= set()
for i in range(1, 4):
    val_1 = input(f"Enter the element {i} for set-1:")
    set_1.add(val_1)

set_2= set()
for i in range(1, 4):
    val_2 = input(f"Enter the element {i} for set-2:")
    set_2.add(val_2)

union_set = set_1.union(set_2)
sorted_union = sorted(union_set)
print("Set 1:", set_1)
print("Set 2:", set_2)
print("The union of both sets is:", sorted_union)