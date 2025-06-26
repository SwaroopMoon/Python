cars =[]                                             # Create an empty list to store car names
cars.append(input("Enter 1st car name:"))            # Take input from the user and add 6 car names to the list
cars.append(input("Enter 1st car name:"))
cars.append(input("Enter 2nd car name:"))
cars.append(input("Enter 3rd car name:"))
cars.append(input("Enter 4th car name:"))
cars.append(input("Enter 5th car name:"))
cars.append(input("Enter 6th car name:"))
print("Sliced list is:",cars[1:4])                   # Display a slice of the list from index 1 to 3 (i.e., 2nd to 4th car)
                                                     #cars[1:4] gives elements from index 1 to 3 (4 is not included).