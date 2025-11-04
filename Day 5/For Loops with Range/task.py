#Range function

# Range function to form a range of numbers between giving numbers
# It iterates one by one
for number in range(0, 5):
    print(number)

# We can set the step of iteration
# In this case we set that it returns every 2 numbers
for number in range(0, 5, 2):
    print(number)

sum_num= 0
for number in range(1, 100 + 1):
    sum_num +=  number

print(sum_num)

sum_num = sum_num * 2
print(sum_num)

for number in range(1, 100 + 1):
    phrase = ""

    if number % 3 == 0:
        phrase = "Fizz"

    if number % 5 == 0:
        phrase += "Buzz"

    if phrase == "":
        print(number)
    else:
        print(phrase)