# WAP to enter marks of three subjects from the user and store them in a dictionary.
# Start with an empty dictionary and add one by one.
# Use subject name as key and marks as value.

#Program :
marks={}

x = input("Enter Physics marks :")
marks.update({"Phy":x})

y = input("Enter Physics marks :")
marks.update({"Chem": y})

z = input("Enter Physics marks :")
marks.update({"Math": z})

print(marks)