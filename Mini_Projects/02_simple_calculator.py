def calc(a,op,b):
    try:
        if op == '+':
            return a+b
        elif op == '-':
            return a-b
        elif op == '*':
            return a*b
        elif op == '/':
            return a/b
        else:
            return "Invalid Operator"
    except ZeroDivisionError:
        return "Division by zero is not allowed!"
    except Exception as e :
        return f"Something went wrong : {e}"
# Take input in single line
#user_input.strip().split()
# .strip() removes any leading/trailing spaces.
# .split() breaks the input string into a list using spaces:
# "5 + 2" → ["5", "+", "2"]

try:
    user_input=input()
    a1,op1,b1 = user_input.strip().split()
    a1= float(a1)
    b1= float(b1)
    print(calc(a1,op1,b1))
except ValueError:
    print("Please input value in correct format : Number Operator Number")