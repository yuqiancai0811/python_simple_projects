import random
while True:
    answer = input("Roll the dice? (y/n) ")
    if answer.upper() == "Y":
        print("("+str(random.randint(1, 6)) + ","+str(random.randint(1, 6)) + ")")
    elif answer.upper() == "N":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice")

