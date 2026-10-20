import random

rock = '🪨'
paper = '📃'
scissor = '✂️'

game_icons = [rock, paper, scissor]

user_choice = int(input("0 - Rock, 1 - Paper, 2 - Scissor | Enter your choice :\n"))

if user_choice >= 0 and user_choice < 3:
    print(f"User choose : \n{game_icons[user_choice]}")
else:
    print("Please choose valid number.")


computer_choice = random.randint(0, 2)
print(f"Computer choose : \n{game_icons[computer_choice]}")


if user_choice > 2 or user_choice < 0:
    print("Please enter the valid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")