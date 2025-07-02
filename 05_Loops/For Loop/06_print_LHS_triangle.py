# Print this pattern:

# *
# * *
# * * *
# * * * *


#I/P :

n=4
for i in range(1,n+1):
    for j in range(i):
         print("*", end="")
    print()