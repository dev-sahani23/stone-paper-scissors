"""Stone = -1
Paper = 0
Scissors = 1"""

import random
option = [-1, 0, 1]
computer = random.choice(option)
print("Stone: s    Paper: p    Scissors: c")
youstr = input("Enter your choice: ")
youDict = {"s": -1, "p": 0, "c": 1}
if(youstr not in youDict):
    print("❌ Something went wrong! Invalid input.")
else:
    you = youDict[youstr]
    reversedDict = {-1: "Stone", 0: "Paper", 1: "Scissors"}
    print(f"You chose: {reversedDict[you]}\nComputer chose: {reversedDict[computer]}")
    if computer == you:
        print("Its a draw!")
    else:
        if computer == -1 and you == 0:
            print("You Win!")
        elif computer == -1 and you == 1:
            print("You lose!")
        elif computer == 0 and you == -1:
            print("You lose!")
        elif computer == 0 and you == 1:
            print("You win!")
        elif computer == 1 and you == -1:
            print("You win!")
        elif computer == 1 and you == 0:
            print("You lose!")
        else:
            print("Something went wrong!")