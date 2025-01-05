import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {ROCK: '✊️', PAPER: '📄', SCISSORS: '✂'}
valid_members = tuple(emojis.keys())


def get_user_choices():
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if user_choice in valid_members:
            return user_choice
        else:
            print("invalid choice!")


def display_choices(user_choice, computer_choice):
    print(f'You choose: {emojis[user_choice]}')
    print(f'Computer choose: {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print("You win!")
    else:
        print("You lose!")


def play_game():
    while True:
        user_choice = get_user_choices()

        computer_choice = random.choice(valid_members)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        continue_choice = str(input("Continue? (y/n) "))
        if continue_choice == 'n':
            break


play_game()
