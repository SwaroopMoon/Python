# Write a program to count the number of students with grade "A" in the following  tuple.
# ["C","D","A","B","B","A"]
# Store the above value in list and sort them.

#Program:

tup = ("C","D","A","B","B","A")                          # Define a tuple containing student grades
tup_count=tup.count("A")                                 # Count how many times grade "A" appears in the tuple
print('''The count of "A" grade is :''', tup_count)      # Display the count of grade "A"
tup_list =list(tup)                                      # Convert the tuple into a list to perform sorting
tup_list.sort()                                          # Sort the list in ascending order (A to D)
print('''Sorted list from "A" to "D" is :''', tup_list)  