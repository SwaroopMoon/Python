#Write a program to accept input elements from user to list and check if list contains palindrome of elements.

#(Hint: use copy() method)
#[1,2,3,2,1]     [1,"abc","abc",1]


#Program :

# Create an empty list
list=[]

# Accept 5 elements from the user and append to the list
list.append(input("Enter 1st element:"))
list.append(input("Enter 2nd element:"))
list.append(input("Enter 3rd element:"))
list.append(input("Enter 4th element:"))
list.append(input("Enter 5th element:"))

# Create a copy of the list using copy() method
copy_list=list.copy()

# Reverse the copied list
copy_list.reverse()


# Compare original list with the reversed one
if(list==copy_list):
    print("List is Palindrome.")       # If equal, it's a palindrome
else:
    print("List is not Palindrome.")   # If not equal, not a palindrome