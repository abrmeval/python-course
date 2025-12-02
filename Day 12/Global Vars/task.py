# Modifying Global Scope

enemies = 1


def increase_enemies():
    #To modify a global variable we need to indicate it with th keyword global
    #It is not necessary if we want to read it only
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


