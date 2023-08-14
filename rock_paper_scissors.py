import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors/Q ").lower()
    print()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)

    computer_pick = options[random_number]
    
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won! 🥳 ")
        print()
        user_win += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won! 🥳 ")
        print()
        user_win += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won! 🥳 ")
        print()
        user_win += 1
    else:
        print("You Lost! 😢 ")
        print()
        computer_win += 1

print("You Won", user_win, " times. ")
print("The computer won", computer_win, " times ")
print("Goodbye! 👋 ")
