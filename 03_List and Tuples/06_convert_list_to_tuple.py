cars_list =[]                                       #For list use rectangular bracket
cars_list.append(input("Enter 1st car name:"))
cars_list.append(input("Enter 2nd car name:"))
cars_list.append(input("Enter 3rd car name:"))
cars_list.append(input("Enter 4th car name:"))
cars_list.append(input("Enter 5th car name:"))
cars_list.append(input("Enter 6th car name:"))
print(tuple(cars_list))                              #This line converts the list to a tuple and prints it. 
                                                     #NOTE: list can stil be manipulated as given below.
                                                     #But cannot use methods like pop(),pull(,etc)
cars_list.append(input("Enter:"))
print(cars_list)
car_tuple=tuple(cars_list)                           #Converting lists to tuple permanently #For tuple use paranthesis()
print(car_tuple)                                     #Prints the tuple
                                                     #But if you write :
                                                     #cars_tuple.append(input("Enter:"))
                                                     #it will show error as tuples are immutable and cannot be manipulated