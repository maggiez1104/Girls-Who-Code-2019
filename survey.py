import json
spanish_english = {"hola": "hello", "gato": "cat", "mujer": "woman"}

word = spanish_english["hola"]

users = {}

users["Diana"] = 30
#print(users)

colors_things = {"yellow": "trumpet", "blue": "bird", "red": "car"}
#print(colors_things)

#print(colors_things["red"])

#create an empty dictionary
#create a list of survery questions
questions = ["What is your name?", "How old are you?", "What is your favorite color?"]
#create a list of keys
keys = ["name", "age", "color"]
allanswers = []

anothersurvey = "yes"
while anothersurvey == "yes":
    i = 0
    answers = {}
#loop through
    for question in questions:
        print(question)
        userInput = input()
        answers[keys[i]] = userInput
        i += 1

    print(answers)
    allanswers.append(answers)
    anothersurvey = input("Submit another survey? (yes or no)")

print(allanswers)

with open("jsonfile.json") as f:
    try:
        olddata = json.load(f)
    except ValueError:
        olddata = []
allanswers.extend(olddata)
f.close()

f = open("jsonfile.json", "w")
json.dump(allanswers, f)
f.close()
