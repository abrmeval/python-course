import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer_choice = random.randint(0,2)

if user_choice < 0 or user_choice > 2:
    print("Invalid number. You loose!")
else:
    # User
    print(user_choice)
    print(choices[user_choice])

    # Computer
    print("Computer choice:")
    print(choices[computer_choice])

    # Winner decision
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (
            user_choice == 2 and computer_choice == 0):
        print("You lose!")
    else:
        print("You win!")






