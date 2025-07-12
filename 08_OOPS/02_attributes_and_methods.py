#Que : Create Account class with 2 attributes : balance and account number.
#Create methods for debit, credit and printing the balance/

#I/P :

class Account:
    
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc

    def debit(self, amount):
        self.bal-=amount
        print("Debited amount:", amount)
        self.total_bal()

    def credit(self, amount):
        self.bal+=amount
        print("Credited amount:", amount)
        self.total_bal()

    def total_bal(self):
        print("Total balance:", self.bal)


user = Account(1000 , 12345)
user.credit(500)
user.debit(300)