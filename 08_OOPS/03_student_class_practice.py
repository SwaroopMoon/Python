#Que : Create a Student class with attributes: name, roll_number, and marks.
# Add methods to:

# 1. Display student details
# 2. Update marks
# 3. Check if the student has passed (pass mark is 40)

# I/P :


class Student:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def stud_details(self):
        print(f"Name : {self.name}")
        print(f"Roll number : {self.roll_number}")
        print(f"Marks : {self.marks}")


    def update_marks(self, new_marks):
        self.marks= new_marks
        print(f"Marks updated to : {new_marks}")

    def pass_or_fail(self):
        if self.marks >= 40 :
            print("You have passed the exam.")
        else:
            print("You are failed in the exam.")



stud= Student("Swaroop", 63, 90)
stud.stud_details()
stud.update_marks(98)
stud.pass_or_fail()