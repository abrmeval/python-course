#Try and except similar to try catch in C#
try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed and invalid number. Please try again with numerical response.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
