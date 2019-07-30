import json

myDictionary = {"hola": "hello", "gato": "cat", "mujer": "woman"}


json.dump(myDictionary, f)

f.close()
