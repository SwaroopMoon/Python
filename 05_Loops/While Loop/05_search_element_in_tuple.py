# Search for a number "x" in tuple using loop : [1,4,9,16,25,36,49,64,81,100]

#I/P:

tup = (1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the number to search:"))
index=0
while index<len(tup):
    if tup[index]==x:
        print(f"Found at index {index}")
        break
    index+=1
else:
        print(f"Not Found")