import random

from art import logo

attempts_dic = {"easy": 10, "hard": 5}
difficulty = "easy"

def begin_message():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")

def ask_difficulty():
    return input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def get_attempts(difficulty):
    return attempts_dic[difficulty]

def check_answer(user_number, number_to_guess, attempts):
    if user_number > number_to_guess:
        if user_number - number_to_guess > 5:
            print("To high.")
        else:
            print("High.")
        attempts -= 1
    elif user_number < number_to_guess:
        if number_to_guess - user_number > 5:
            print("To low.")
        else:
            print("Low.")
        attempts -= 1
    else:
        print(f"You got it! The answer was {number_to_guess}.")
        attempts = -1
    return attempts

def start_guessing(attempts):
    number_to_guess = random.randint(1,100)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        user_number = int(input("Make a guess: "))

        attempts = check_answer(user_number, number_to_guess, attempts)

        if attempts > 0:
            print("Guess again.")

    if attempts == 0:
        print("You've run out of guesses. Refresh the page to run again.")
#Main
begin_message()
difficulty = ask_difficulty()
attempts = get_attempts(difficulty)
start_guessing(attempts)

