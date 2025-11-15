programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "loop": "The auction pf doing somethong over and over again"
}

print(programming_dictionary["Bug"])

#This is how to add a new item in the dict
programming_dictionary["Loop2"] ="New item in doct"

empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit  an item in a dictionary
programming_dictionary["Bug"] = "New bug value"


#Loop through a dictionary:
# It gives you the key
for key  in programming_dictionary:
    #Print key
    print(key)
    #Print value
    print(programming_dictionary[key])