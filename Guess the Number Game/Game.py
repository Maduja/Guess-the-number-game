import random

num=random.randint(1,20)

guess = int(input("Can you guess the number I am thinking? It's less than 20: "))

while num!=guess:
    if guess>num:
        print("your number is too high")
    else:
        print("your number is too low")
    guess = int(input("try again: "))

print("You Won! Thank you for playing")