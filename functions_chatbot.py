# --- Define your functions below! ---
import random
import time

def intro():
    print("""
    Hi! I am chatbot! What is the magic word?
    (the magic word is maggie)
    """)

def process_input(answer):
    if answer == "maggie":
        print("Good job. Welcome Maggie.")
        welcome()
    else:
        intruder()

def welcome():
    print("""
In this chat, we like to play games!
Do you want to play...
    HANGMAN         or        Rock, Paper, Scisscors?
    """)
    answer2 = input("What will you say? Enter 'Hangman' or 'RPS':")
    process_input_VIP(answer2)

def intruder():
    print("Wrong. Guess again.")

def process_input_VIP(answer2):
    while True:
        if answer2 == "RPS":
            RPS()
            time.sleep(1)
            print("""
            Play again!
            or...
            if you would like to switch to Hangman, Ctrl+z and re-enter the magic word.
            """)
        elif answer2 == "hangman":
            hangman()
            time.sleep(1)
            print("""
            Play again!
            or...
            if you would like to switch to Rock, Paper, Scisscors, Ctrl+z and re-enter the magic word. 
            """)
        else:
            welcome()

def RPS():
    print("Welcome to ROCK, PAPER, SCISSCORS, SHOOT!")
    list = ["rock", "paper", "scisscors"]
    shoot = input("""Enter 'rock', 'paper', or 'scisscors!
User choice: """)
    computer_shoot = random.choice(list)
    time.sleep(1)
    print("Computer's choice was: " +computer_shoot)
    time.sleep(1)
    if shoot == "rock":
        if computer_shoot == "rock":
            print("It's a tie!")
        elif computer_shoot == "scisscors":
            print("You win!")
        elif computer_shoot == "paper":
            print("You lose!")
    elif shoot == "paper":
        if computer_shoot == "paper":
            print("It's a tie!")
        elif computer_shoot == "rock":
            print("You win!")
        elif computer_shoot == "scisscors":
            print("You lose!")
    elif shoot == "scisscors":
        if computer_shoot == "scisscors":
            print("It's a tie!")
        elif computer_shoot == "paper":
            print("You win!")
        elif computer_shoot == "rock":
            print("You lose!")
    else:
        print("That's not an option! Try Again!")
        RPS()

def hangman():
    import random
    import time
    # A list of words that
    potential_words = ["girls", "empower", "coding","variable", "python"]

    word = random.choice(potential_words)
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


#def userchoice(shoot):

# --- Put your main program below! ---
def main():
  for i in range(1):
    intro()
    answer = input("Enter magic word: ")
    process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
