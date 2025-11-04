import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#Option 1
index = random.randint(0, len(friends) - 1)
print(friends[index])

#Option 2
#radom.choice returns randomly a value from a collection
random_value = random.choice(friends)
print(random_value)