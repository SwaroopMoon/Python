num1 = int(input("Enter your 1st number:"))
num2 = int(input("Enter your 2nd number:"))
num3 = int(input("Enter your 3rd number:"))
if(num1 == num2 == num3):
    print("All three numbers are equal:", num1)
elif(num1 >= num2 and num1 >= num3):
    print("Greatest number is:", num1)
elif(num2 >= num1 and num2 >= num3):
    print("Greatest number is:", num2)
else:
    print("Greatest number is:", num3)