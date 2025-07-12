#Que : Create a student class that takes name and marks of 3 subjects as arguments in constructor.
#Then create a method to print the average.

#I/P :

class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum+=val
        print("Hi", self.name ,"your average score is :", sum / 3)


std1 = Student("Swaroop" , [98, 99, 97])
std1.get_avg()