
#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")
stripped_pass = test_password.strip()
lower_pass = stripped_pass.lower()

for line in f:
    strip_line = line.strip()
    if lower_pass == strip_line:
        print("Your password is too weak!")


f = open("dictionary.txt","r")
turnoff = False
for word1 in f:
    strip_word1 = word1.strip()
    f = open("dictionary.txt","r")
    for word2 in f:
        strip_word2 = word2.strip()
        compound = strip_word1 + strip_word2
        #print(compound)
        if lower_pass in compound:
            #print("i did it")
            print("Your password is too weak!")
            turnoff = True

            break
    if turnoff:
        break








            #Write logic to see if the password is in the dictionary file below here:
