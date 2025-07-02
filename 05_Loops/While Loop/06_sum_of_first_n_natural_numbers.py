#Que : WAP to find the sum of first 'n' natural numbers.


#I/P :


n = int(input("Enter the number:"))
i=1
sum=0 
while (i<=n):
    sum+=i
    i+=1
print("The sum of first", n , "natural numbers is:",sum)