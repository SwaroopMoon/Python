# Print below pattern:


# * * * *
# * * *
# * *
# *

# I/P:

n=4
i=n
for i in range(n,0,-1):
    for j in range(i):
        print("*", end="")
    print()