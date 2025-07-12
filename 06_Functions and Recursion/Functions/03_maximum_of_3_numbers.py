#Program to find the maximum of 3 numbers

#I/P :

def maximum(a,b,c):
    return max(a,b,c)

a1=int(input("Enter the 1st number:"))
b1=int(input("Enter the 2nd number:"))
c1=int(input("Enter the 3rd number:"))

print("Maximum number is:", maximum(a1,b1,c1))