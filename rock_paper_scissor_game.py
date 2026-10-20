import random

print("=" * 50)
print("Rock - Paper - Scissor".center(50))
print("=" * 50)

element = ['Rock', 'Paper', 'Scissor']


while True:
    choice = input("Rock\nPaper\nScissor\nExit\nEnter your choice - ").title()

    if choice == "Rock" and random.choice(element) == "Paper":
        print("=" * 50, "\n", "Opponent Win".center(50))
        print("=" * 50, end="\n")
    elif choice == "Paper" and random.choice(element) == "Rock":
        print("=" * 50, "\n", "You Win".center(50))
        print("=" * 50, end="\n")
    elif choice == "Paper" and random.choice(element) == "Scissor":
        print("=" * 50, "\n", "Opponent Win".center(50))
        print("=" * 50, end="\n")
    elif choice == "Scissor" and random.choice(element) == "Paper":
        print("=" * 50, "\n", "You Win".center(50))
        print("=" * 50, end="\n")
    elif choice == "Scissor" and random.choice(element) == "Rock":
        print("=" * 50, "\n", "Opponent Win".center(50))
        print("=" * 50, end="\n")
    elif choice == "Rock" and random.choice(element) == "Scissor":
        print("=" * 50, "\n", "You Win".center(50))
        print("=" * 50, end="\n")
    elif choice == "Rock" and random.choice(element) == "Rock":
        print("=" * 50, "\n", "Draw".center(50))
        print("=" * 50, end="\n")
    elif choice == "Paper" and random.choice(element) == "Paper":
        print("=" * 50, "\n", "Draw".center(50))
        print("=" * 50, end="\n")
    elif choice == "Scrissor" and random.choice(element) == "Scrissor":
        print("=" * 50, "\n", "Draw".center(50))
        print("=" * 50, end="\n")
    elif choice == "Exit":
        break


    
