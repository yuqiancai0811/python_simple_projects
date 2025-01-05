import random
ran_num = random.randint(1,100)
while True:
    try:
        input_num = int(input("Guess the number between 1 and 100 "))
        if input_num < ran_num:
            print("Too low!")
        elif input_num > ran_num:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number")


