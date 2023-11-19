import random

fav_fruits = ["Apple","Grapes", "Mango", "Orange", "Strawberry" ]

word_list = fav_fruits

word = random.choice(word_list)

print("Favourite Fruits List : ", word_list)

print("Random Fruit : " , word)

guess = input("Enter a single letter : ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")




