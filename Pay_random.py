import random
name_string = input()
# sujan, sutapa, pradip, apurba, minati
name = name_string.split(",")
num_item = len(name)
random_choice = random.randint(0, num_item - 1)
perosn_who_pay = name[random_choice]
print(perosn_who_pay + " Will Pay The Today Bill")
