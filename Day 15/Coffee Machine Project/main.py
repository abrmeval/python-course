from data import MENU, QUARTER, DIME, NICKLE, PENNIE, resources

machine_money = 0
change = 0

def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${machine_money}")


def check_resources(coffee_type):
    ingredients =  MENU[coffee_type]["ingredients"]

    if resources["water"] < ingredients["water"]:
        print("Sorry there is not enough water.")
        return False

    if resources["milk"] < ingredients["milk"]:
        print("Sorry there is not enough milk.")
        return False

    if resources["coffee"] < ingredients["coffee"]:
        print("Sorry there is not enough coffee.")
        return False

    return True

def calculate_money(quarters, dimes, nickles, pennies):
    return quarters * QUARTER + dimes * DIME + nickles * NICKLE + pennies * PENNIE

def check_client_money(money, coffee_type):
    cost = MENU[coffee_type]["cost"]
    if money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    return True

def get_profit(money, coffee_type):
    cost = MENU[coffee_type]["cost"]

    if money > cost:
        change = round(money - cost, 2)
        print(f"Here is ${change} dollars in change.")
        return cost

    return money

def deduct_resources(coffee_type):
    ingredients =  MENU[coffee_type]["ingredients"]
    return {
        "water": resources["water"] - ingredients["water"],
        "milk": resources["milk"] - ingredients["milk"],
        "coffee": resources["coffee"] - ingredients["coffee"]
     }

is_on = True
while is_on:
    action = input("What would you like? (espresso/latte/cappuccino):")
    if action == "espresso" or  action == "latte" or  action == "cappuccino":
        enough_resources = check_resources(action)

        if enough_resources:
            print("Please insert coins: ")
            money = calculate_money(input("How many quarters?: "), input("How many dimes?: "), input("How many nickles?: "), input("How many pennies?: "))
            enough_money = check_client_money(money, action)

            if enough_money:
                profit = get_profit(money, action)
                machine_money += profit
                resources = deduct_resources(action)
                print(f"Here is your {action}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        continue
    elif action == "report":
        print_report()
    elif action == "off":
        is_on = False

