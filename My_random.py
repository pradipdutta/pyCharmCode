import random
random_int = random.randint(1, 50)
print(random_int)
random_flot = random.random()
print(random_flot)


random_tos = random.randint(0, 1)
if random_tos == 0:
    print("Head")
else:
    print("Tail")
