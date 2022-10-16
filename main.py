import random

number_of_dice = int(input("How many dice would you like to roll? "))
number_of_sides = int(input("How many sides would you like to have on your dice? "))

for i in range(number_of_dice):
    number = random.randint(1, number_of_sides)

    print(number)
