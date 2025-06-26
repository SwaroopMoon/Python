#.split(',') splits input string into a list using commas
car_list1=(input("Enter first car list(comma-separated):")).split(',')    
car_list2=(input("Enter second car list(comma-separated):")).split(',') 
print("First car list is:",car_list1)                                      #prints first tuple list
print("Second car list is:",car_list2)                                     #prints second tuple list
print("Result:",car_list1==car_list2)                                      #compares both tuples and prints True if they are equal