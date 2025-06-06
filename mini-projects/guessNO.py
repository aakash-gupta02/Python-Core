import random


target = random.randint(1,100)
print(target)


while True:
    num = int(input("Guess a Number, between 1-100:- "))
    if target == num:
        print("You Won!!")
        break
    else:
         print("Too High" if num > target else "Too Low")
        # print(["Too high " if num  ])
