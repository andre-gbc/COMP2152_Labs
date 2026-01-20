# Week 02 Lab

# RPS Game

choices = ['rock', 'paper', 'scissors']
user_choice = input("Enter your choice (1-rock, 2-paper, 3-scissors): ").lower()

user_choice = int(user_choice)

if user_choice < 1 or user_choice > 3:
    print("Invalid choice! Please select a number between 1 and 3.")
else:
    computer_choice = random.randint(1, 3)