import random
from art import logo

#Deals the cards
def deal_cards(cards, n):
    table_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(0, n):
        index = random.randint(0, 13)
        number = table_cards[index]
        cards.append(number)

#Deals the cards for the user
def deal_for_user(deck, user_cards, computer_cards):
    decision = "y"
    score = 0
    while decision == "y":
        deal_cards(user_cards, deck)
        score = sum(user_cards)
        decision = input("Type 'y' to get another card, type 'n' to pass").lower()
        print(f"Your cards: {user_cards}, current score: {score}")
        print(f"Computer's first card: {computer_cards[0]}")
        deck = 1
    return score

#Deals the cards for the computer
def deal_for_computer(deck, computer_cards):
    deal_cards(computer_cards, deck)
    return sum(computer_cards)

#Recalculate score if there is an Ace and score is above 21
def validate_score(cards, score):
    if 11 in cards and score > 21:
        return score - 10
    return score

#First play of the game
def first_play(computer_cards, user_cards):
    computer_score = deal_for_computer(2,computer_cards)
    user_score = deal_for_user(2, user_cards, computer_cards)

    #Helper function
    def stop():
        return {
            "user_score": user_score,
            "computer_score": computer_score,
            "continue": False
        }

    #Validate score whether there is an Ace to recalculate score
    computer_score = validate_score(computer_cards, computer_score)
    user_score = validate_score(user_cards, user_score)

    #if user gets above 21
    if user_score > 21:
        print("You lose 😤")
        return stop()

    #If computer gets a blackjack (Ace + 10 value card).
    if computer_score == 21:
        print("You lose 😤")
        return stop()

    #If user gets a blackjack (Ace + 10 value card).
    if len(user_cards) and user_score == 21:
        print("You win 😁")
        return stop()

    return {
        "user_score": user_score,
        "computer_score": computer_score,
        "continue": True
    }

#Second play of the game
def second_play(turn, computer_cards):
    user_score = turn["user_score"]
    #While computer score is less than 17 draws cards
    while computer_score < 17:
        computer_score = deal_for_computer(1, computer_cards)

    #If user score above 21
    if computer_score > 21:
        print("You win 😁")
        return
    # If user score greater than computer score
    if user_score > computer_score:
        print("You win 😁")
        return
    #If equal scores
    if user_score == computer_score:
        print("It is a draw")
        return

    print("You lose 😤")
    return


continue_playing = "y"
while continue_playing == "y":
    user_cards = []
    computer_cards = []
    print("\n" * 20)
    print(logo)

    turn = first_play(computer_cards, user_cards)
    if turn["continue"]:
        second_play(turn, computer_cards)

    continue_playing = input("Do you wany to play a game of Blackjack? Type 'y' or 'n': ")