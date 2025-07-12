from abc import ABC, abstractmethod

class RentCalculatorBase(ABC):
    
    @abstractmethod
    def calculate_per_person_rent(self):
        pass

    @abstractmethod
    def print_summary(self):
        pass

class RentCalculator(RentCalculatorBase):

    def __init__(self):
        self.__total_rent = 0
        self.__no_of_roommates = 1
        self.__utilities = {}
        self.__include_utilities = False

    def get_input(self):
        try :
             self.__total_rent = int(input("Enter the total amount of rent : "))
             self.__no_of_roommates = int(input("Enter the number of roommates : "))
        except ValueError:
             print(f"Please enter a valid numeric value for amount and roommates!")
             return False

        choice = str(input("Do you want to add utilities?(Yes/No)\nAns :")).lower()
        if choice == "yes":
                self.__include_utilities = True
                self.add_utilities()
        return True
        

    def add_utilities(self):
        while True:
             utililty_name = input("Enter utility name or type 'Done' if finished:").lower()
             if utililty_name == 'done':
                  break
             try:
                  amount = float(input(f"Enter the amount of {utililty_name} :"))
                  self.__utilities[utililty_name] = amount
             except ValueError:
                print("❌ Please enter a valid numeric amount!")


    def calculate_total_utilities(self):
         return sum(self.__utilities.values())
    
    def calculate_per_person_rent(self):
         total_amount= self.__total_rent
         if self.__include_utilities:
              total_amount += self.calculate_total_utilities()
         return total_amount / self.__no_of_roommates
    
    def print_summary(self):
         print("\n-----Rent Summary-----")
         print(f"Total Rent :{self.__total_rent} Rs")
         if self.__include_utilities:
              print("Utilities:")
              for utility_name, amount in self.__utilities.items():
                   print(f"{utility_name} : {amount} Rs")
              print("Total amount of utilities : ", self.calculate_total_utilities() ,"Rs")
         total_payable = self.__total_rent + (self.calculate_total_utilities() if self.__include_utilities else 0)
         print(f"Total payable amount:", total_payable,"Rs")
         print(f"Each roommate should pay : {self.calculate_per_person_rent():.2f} Rs")
               


calculator = RentCalculator()
if calculator.get_input():
    calculator.print_summary()
else:
    print("Program ended due to invalid input.")