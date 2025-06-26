# Que : You are given a list of subjects for students. 
# Assume one classroom is required for 1 subjest. 
# How many classroom are needed by all students.
# "Python","java","C++","javascript","java","python","java","C++","C"

#Program :

subjects = {"Python","java","C++","javascript","java","python","java","C++","C"}
print("The subjects are :",subjects)
subjects_lower= {sub.lower() for sub in subjects}
count=len(subjects_lower)
print("Classrooms that are required are:",count)