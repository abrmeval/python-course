# enemies = 1
#
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

#Local Scope
# def drink_potion():
#     # variables created inside a function are accesible only inside the function
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()

#Global Scope
#Available in the whole file
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)
