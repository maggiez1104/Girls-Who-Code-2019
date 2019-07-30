#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
consonant = ["b", "c", "d","f", "g", "h", "j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
vowel = ["a", "e", "i","o","u","y"]
#Generates a random integer.
print("How many letters in the name?")
userInput = input()
for i in range(int(userInput)/2):
    ConsonantRandInt = randint(0, len(consonant)-1)
    print(consonant[int(ConsonantRandInt)])
    VowelRandInt = randint(0, len(vowel)-1)
    print(vowel[int(VowelRandInt)])


letters = 0
while letters <= userInput
    if
