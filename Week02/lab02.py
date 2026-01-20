# Week 02 Lab
# RPS Game

import random
choices = ['rock', 'paper', 'scissors']
user_choice = input("Enter your choice (1-rock, 2-paper, 3-scissors): ").lower()

user_choice = int(user_choice)

if user_choice < 1 or user_choice > 3:
    print("Invalid choice! Please select a number between 1 and 3.")
else:
    computer_choice = random.randint(1, 3)

    userChoiceIndex = choices[user_choice - 1]
    computerChoiceIndex = choices[computer_choice - 1]
    print(f"You chose: {userChoiceIndex}")
    print(f"Computer chose: {computerChoiceIndex}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("Computer wins!")