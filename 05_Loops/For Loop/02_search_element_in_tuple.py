# Search for a number "x" in tuple using loop : (1,4,9,16,25,36,49,64,81,100)

#I/P :

numbers= (1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the number:"))
idx=0
for idx in range(0,len(numbers)):
    if(numbers[idx]==x):
        print(f"Found at {idx}")
        break
    idx+=1
else:
    print("Not found")