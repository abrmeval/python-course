#Import logo
#import data
#Print First logo
#Get randomly an item to compare
#Print second logo
#Get second name randomly making sure it is not the same as the first one
#Ask the user to compare
#Read the value
#Compare the values (followers_count)
#If user is right accumulate points,
# Then we move the second item to the first place and generate randomly another item to compare
# repeat steps before
#If user is wrong, we print the result and final message
import random
from  art import logo, vs
from game_data import data

def print_start_comparison(first_msg, second_msg, include_msg_score):
    print(logo)
    print(first_msg)

    if include_msg_score:
        print(f"You're right! Current score: {score}")

    print(vs)
    print(second_msg)

def print_game_over():
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

def get_user_index(letter):
    if letter == "A":
        return 0
    if letter == "B":
        return 1
    return -1

def get_random_index(indexes):
    idx = -1
    while idx < 0 or idx in indexes:
        idx = random.randint(0, len(data) - 1)
    return idx

def get_item(idx):
    return data[idx]

def compare(first_item, second_item, user_idx):
    if user_idx == 0:
     if first_item["follower_count"] > second_item["follower_count"]:
         return True
     return False

    if user_idx == 1:
        if second_item["follower_count"] > first_item["follower_count"]:
            return True
        return False

    return False

def get_item_message(item, isFirstOne):
    prefix = "Compare A"
    if not isFirstOne:
        prefix = "Against B"
    return f"{prefix}: {item["name"]}, a {item["description"]}, from {item["country"]}."

indexes = []
score = 0
isRight = True
is_first_round = True
include_msg_score = False

while isRight:
    if is_first_round:
        indexes.append(get_random_index(indexes))
        indexes.append(get_random_index(indexes))
        is_first_round = False
    else:
        indexes[0] = indexes[1]
        indexes[1] = get_random_index(indexes)
        include_msg_score = True

    first_item = get_item(indexes[0])
    second_item = get_item(indexes[1])

    print_start_comparison(get_item_message(first_item, True), get_item_message(second_item, False), include_msg_score)
    user_idx = get_user_index(input("Who has more followers? Type 'A' or 'B': ").upper())
    isRight = compare(first_item, second_item, user_idx)

    if not isRight:
        print_game_over()
    else:
        score += 1
        print("\n"*20)
