# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)

bids = {}
more_bidders = True

while more_bidders:
    name = input("What is youe name?: ")
    bid = float(input("What is your bid? $ "))
    add_more = input("Are there any other bidders? Type 'yes' or  'no'.\n").lower()
    bids[name] = bid

    #Built in function to get the max value of a dictionary
    # max(bids, bids.get)

    if add_more == "no":
        more_bidders = False
        temp_key = ""

        for key in bids:
            if temp_key == "":
                temp_key = key
            elif bids[key] > bids[temp_key]:
                temp_key = key

        print(f"The winner is {temp_key} with a bid of {round(bids[temp_key])}")
    else:
        print("\n" * 20)


