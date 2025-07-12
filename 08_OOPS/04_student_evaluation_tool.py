#Que :
# Create a Student class with attributes: name, roll_number, and marks.
# Add methods to:

# 1. Display student details
# 2. Update marks
# 3. Check if the student has passed (pass mark is 40)

# Print the grade of the student based on their marks using the following criteria:
# Marks >= 90: Grade A
# Marks >= 75 and < 90: Grade B
# Marks >= 60 and < 75: Grade C
# Marks >= 40 and < 60: Grade D
# Marks < 40: Grade F
# NOTE : TAKE ALL INPUTS (NAME, ROLL_NO. AND MARKS) FROM USER.
#AFTER DISPLAYING THE DETAILS, ASK THE USER IF THEY WANT TO UPDATE THEIR MARKS.
#IF YES, UPDATE AND DISPLAY THE NEW MARKS, THEN SHOW THE PASS/FAIL STATUS AND GRADE.


# I/P :


# Define the Student class to store and manage student details and performance

class Student:

    def __init__(self, name, roll_number, marks):
        """ Constructor to initialize student attributes: name, roll number, and marks"""
        self.name = name
        self.roll_number = roll_number
        self.marks = marks


    def display_details(self):
        """Display the student's details"""
        print(f"Name : {self.name}")
        print(f"Roll number : {self.roll_number}")
        print(f"Marks : {self.marks}")


    def update_marks(self, new_marks):
        """Update the student's marks with a new value"""
        self.marks= new_marks 
        print(f"Marks updated to : {new_marks}")


    # Check whether the student has passed or failed based on marks
    def pass_or_fail(self):
        if self.marks >= 40 :
            print("Congratulations. You have passed the exam.")
        else:
            print("You are failed in the exam.\nBetter luck next time.")


    # Determine and display the student's grade based on marks
    def grade(self):
        if self.marks >=90:
            return "Your grade is : A"
        elif self.marks >= 75 and self.marks < 90 :
            return "Your grade is : B"
        elif self.marks >= 60 and self.marks < 75 :
            return "Your grade is : C"
        elif self.marks >= 40 and self.marks < 60 :
            return "Your grade is : D"
        else:
            return "Your grade is : F"
            

# Input student information from user
name = input("Enter your name :")
roll_number= int(input("Enter your roll number :"))

while True:
    try:
        marks = float(input("Enter your marks(0-100) :"))
        if 0 <= marks <= 100:
            break
        else:
            print("Marks should be between 0-100.Please try again!")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")



# Create an instance of Student with the provided input
stud= Student(name, roll_number, marks)
print("\nFinal Student Summary:")
stud.display_details()

# Ask if the user wants to update the marks and proceed accordingly
ask = input("Do you want to update your marks? (Yes/No)\nAns :").strip().lower()
if ask == "yes":
    new_marks = float(input("Enter marks to update :"))
    stud.update_marks(new_marks)

# Show pass/fail status and the grade based on current marks
stud.pass_or_fail()
print(stud.grade())