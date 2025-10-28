bmi = 84 / 1.65 ** 2
print(bmi)

# Rounds the number to the  largest integer less than or equal to the given number
print(int(bmi))

# Rounds the number to the nearest integer.
print(round(bmi))


# Rounds the number to the nearest integer.
print(round(bmi))

# Rounds the number to the nearest integer indicating te decimals to be included in the result
print(round(bmi, 2))


# Assignment operators
score = 2

# User scores a point
score += 1
print(score)

score -= 1
print(score)

score *= 2
print(score)

score /= 2
print(score)

print("Your score is " + str(score))

#f-string
score = 0
height = 1.8
is_winning = True

# It is like string interpolation in C#
print(f"Your score is  = {score}, your height is  {height}, you are winning is {is_winning}")