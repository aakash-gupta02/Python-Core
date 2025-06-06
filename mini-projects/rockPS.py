import random


choices = ["Rock", "Paper", "Scissor"]

comp = random.choice(choices).lower()


print("Choose any one Option\n Rock\n Paper\n  Scissor")


user = input("Enter your Choice ").lower()
print(f"Computer Choice: {comp}")
if user == comp:
    print("Tie")

elif (user == "rock" and comp =="scissor" or user == "paper" and comp == "rock" or user == "scissor" and comp == "paper" ):
    print("You Win!!")

else:
    print("You Lose")