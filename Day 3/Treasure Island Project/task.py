print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
decision = input("You're at a cross road. Where do you want to go?\n  Type \"left\" or \"right\"\n")

if decision == "Right" or decision == "right":
    print("Fall into a hole.\nGame over.")
elif decision == "Left" or decision == "left":
    decision = input(f"You've come to a lake. There is an island in the middle of the lake.\nType \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if decision == "Swim" or decision == "swim":
        print("Attacked by trout.\nGame over.")
    elif decision == "Wait" or decision == "wait":
        decision = input(f"You are in front of a door.\nType \"red\", \"yellow\", \"blue\" for a door or any key if you want another path.\n")
        if decision == "Yellow" or decision == "yellow":
            print("You Win!")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")

# We can use lower() function for the strings