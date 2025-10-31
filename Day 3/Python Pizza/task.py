print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

price: int

if size == "S":
    price = 15
    # print("Small pizza (S): $15")
elif size == "M":
    price = 20
    # print("Medium pizza (M): $20")
elif size == "L":
    price = 25
    # print("Large pizza (L): $25")
else:
    print("You typed the wrong input.")

if pepperoni == "Y":
    if size == "S":
        price += 2
        # print("Add pepperoni for small pizza (Y or N): +$2")
    else:
        price += 3
        # print("Add pepperoni for small pizza (Y or N): +$2")

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")


