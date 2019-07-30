import random
import time
# A list of words that
potential_words = ["girls", "empower", "coding","variable", "python"]

word = random.choice(potential_words)
print(word)
# Use to test your code:
# Converts the word to lowercase
word = word.lower()
lengthofword = len(word)
# Make it a list of letters for someone to guess
 # TIP: the number of letters should match the word
storeguess = []
for letter in word:
	storeguess.append("_")

possible_guesses = ["a", "b", "c", "d","e","f", "g", "h","i" "j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

print("Welcome to Hangman!")
print(storeguess)
# Some useful variables
#iter = 0
guesses = []
maxfails = 5
fails = 0
correct_guess = 0

while fails < maxfails:
	iter = 0
	guess = input("Guess a single letter. It has " + str(len(word)) + " letters in it:")
	if guess in storeguess:
		print(storeguess)
		print("You already guessed this letter!")
	elif not guess.isalpha():
		print("""This is not a letter! Guess again!""")
	elif guess not in word:
		print(storeguess)
		fails = fails+1
		print("Nope! That letter is not in the word! You have " + str(maxfails - fails) + " tries left!")
		if int(maxfails - fails) == 0:
			print("""GAMEOVER""")
			time.sleep(1)
			print("""The word was """ + word)
	for let in word:
		if guess == let:
			storeguess[iter] = guess
			correct_guess += 1
			print(storeguess)
			print("Great! Guess another letter!")
		iter += 1
	if correct_guess == len(word):
		print("""Yay you guessed the word!""")
		break
	#elif guess in word:
		#position = word.index(guess)
		#storeguess = [item.replace(position, guess) for item in storeguess]
		#print(storeguess)



	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!
