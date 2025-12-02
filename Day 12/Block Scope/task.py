# There is no Block Scope in Python!
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]

    #It works; it does not exist block scope like other languages like Java or C#
    print(new_enemy)

#Can´t access the variable because it is inside the function
# print(new_enemy)

def is_prime(num):
    base_numbers = [2, 3, 5, 7]
    if num == 1:
        return False

    for bn in base_numbers:
        if num ==  bn:
            return True
        if num % bn == 0:
            return False
    return True


print(is_prime(2))
print(is_prime(4))
print(is_prime(5))
print(is_prime(7))
print(is_prime(9))
print(is_prime(10))
print(is_prime(13))
print(is_prime(17))
print(is_prime(21))
print(is_prime(23))
print(is_prime(53))