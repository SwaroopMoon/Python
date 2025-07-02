# Print only odd numbers between 1 and n

# I/P :

n=int(input("Enter the number:"))
i=1
while i<=n:
    if(i%2==1):
        print(i)
    i+=1
    