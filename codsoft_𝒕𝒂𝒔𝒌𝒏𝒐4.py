# 1 for rock
# -1 for paper
# 0 for scissor
import random

computer = random.choice([-1, 0, 1])
you = input("Enter your choice: ")
choices_dict = {"rock": 1, "paper": -1, "scissor": 0}
revdec = {1: "rock", -1: "paper", 0: "scissor"}

if you not in choices_dict:
    print("Enter correct choice")
else:
    younum = choices_dict[you]
    print(f" You chose {revdec[younum]} \n Computer chose {revdec[computer]}")

    if computer == younum:
        print("drew")
    else:
        if computer == -1 and younum == 1:  # Paper vs Rock
            print("You win")
        elif computer == -1 and younum == 0:  # Paper vs Scissors
            print("You lose")
        elif computer == 1 and younum == -1:  # Rock vs Paper
            print("You win")
        elif computer == 1 and younum == 0:  # Rock vs Scissors
            print("You lose")
        elif computer == 0 and younum == -1:  # Scissors vs Paper
            print("You lose")
        elif computer == 0 and younum == 1:  # Scissors vs Rock
            print("You win")
