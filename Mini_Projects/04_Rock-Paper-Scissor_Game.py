'''
QUE :
INPUT ROCK-PAPER-SCISSOR FROM THE USER
INPUT RANDOM FOR COMPUTER


CASE-1 :
ROCK-ROCK = TIE
ROCK-PAPER = PAPER WON
ROCK-SCISSOR = ROCK WON

CASE-2 :
PAPER-PAPER = TIE
PAPER-SCISSOR = SCISSOR WON
PAPER-ROCK = ROCK WON

CASE-3 :
SCISSOR-SCISSOR = TIE
SCISSOR-PAPER = SCISSOR WON
SCISSOR-ROCK = ROCK WON
'''

#I/P :
'''
import random
move = ["ROCK", "PAPER", "SCISSOR"]
user_input = str(input("Enter your move [ROCK/PAPER/SCISSOR] :")).upper()
computer_input =random.choice(move)

if user_input==computer_input:
    print(f"You and Computer both made same move i.e {user_input}.\nIt's a TIE!")
elif user_input == 'ROCK' and computer_input == 'PAPER':
    print(f"Your move : ROCK and Computer's move : PAPER \nCOMPUTER WON!")
elif user_input == 'ROCK' and computer_input == 'SCISSOR':
    print(f"Your move : ROCK and Computer's move : SCISSOR \nYOU WON!")
elif user_input == 'PAPER' and computer_input == 'SCISSOR':
    print(f"Your move : PAPER and Computer's move : SCISSOR \nCOMPUTER WON!")
elif user_input == 'PAPER' and computer_input == 'ROCK':
    print(f"Your move : PAPER and Computer's move : ROCK \nYOU WON!")
elif user_input == 'SCISSOR' and computer_input == 'PAPER':
    print(f"Your move : SCISSOR and Computer's move : PAPER \nYOU WON!")
elif user_input == 'SCISSOR' and computer_input == 'ROCK':
    print(f"Your move : SCISSOR and Computer's move : ROCK \nCOMPUTER WON!")
else:
    print("Please enter a valid move!")
'''
#---------------------------------OR-----------------------------------------#


import random

def play_game():

    move = ["ROCK", "PAPER", "SCISSORS"]
    user_input = str(input("Enter your move [ROCK/PAPER/SCISSORS] :")).upper()
    while user_input not in move:
        user_input = str(input("Invalid Move! \nPlease enter a valid move [ROCK/PAPER/SCISSORS] :")).upper()
    
    winning_map = {
        "ROCK" : "SCISSORS",
        "SCISSORS" : "PAPER",
        "PAPER" : "ROCK"
        }
    
    computer_input =random.choice(move)
    print(f"Your move : {user_input} | Computers's move : {computer_input}")

    if user_input == computer_input:
        print("It's a TIE!")
    elif winning_map[user_input] == computer_input:
        print("YOU WON!")
    else :
        print("COMPUTER WON!")


def main():
    print("----WELCOME TO THE ROCK-PAPER-SCISSORS Game----")
    while True:
        play_game()
        try:
            again = str(input("Do you want to play again? (Yes/No): \nAns :")).strip().upper()
            while again not in ['YES','NO']:
                again = str(input("Invalid Value! Please enter value in Yes/No :")).strip().upper()
            if again == 'NO':
                print("Thanks for playing the game.\nClosing the game...")
                break
        except Exception as e :
            print(f"Unexpected input error : {e}. Exiting the game...")
            break

if __name__ == "__main__" :
    main()
