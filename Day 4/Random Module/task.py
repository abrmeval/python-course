# Random module for generating random numebers
import random

#Custom module
import my_module

#Generate random integer numbers bewtween 1 and 10
random_integer = random.randint(1,10)

print(random_integer)
print(my_module.my_favourite_number)

# Generate a random float number between 0 and 1 exclusive
random_float = random.random()

print(random_float)

# Bewteen 0 and 10 excluxive
random_float = random.random() * 10
print(random_float)


#Generate a random number between 1 and 10 both inclusive
# The range it is not so sure, the end value may or may not be included in the range depending on floating-point rounding
random_float = random.uniform(1, 10)
print(random_float)

random_number = random.randint(1,2)

if random_number == 1:
    print("Heads")
else:
    print("Tails")