marks = int(input("Enter your marks:"))
if(marks<=90 and marks>=100):
    print("You have obtained 'A+' grade.")
elif(marks<=80 and marks>=89):
    print("You have obtained 'A' grade.")
elif(marks<=70 and marks>=79):
    print("You have obtained 'B+' grade.")
elif(marks<=60 and marks>=69):
    print("You have obtained 'B' grade.")
elif(marks<=50 and marks>=59):
    print("You have obtained 'C+' grade.")
else:
    print("Sorry, you are Failed.")
