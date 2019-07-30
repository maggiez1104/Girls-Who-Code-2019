import random

animal = ["platypus","koala", "sloth", "anteater", "zebra","chinchilla"]
print("list:" +str(animal))
choose = random.choice(animal)
print("random choice: " + choose)
print("index is " + str(animal.index(choose)))
guess = input("Name an animal and we will check if it's in the list: ")
print(guess in animal)
if guess in animal:
    print(guess + "'s index is " + str(animal.index(guess)))
adjectives = ["happy", "sad", "blue", "jumpy", "sleepy"]
print(animal.append(adjectives))
print(animal.extend(adjectives))
