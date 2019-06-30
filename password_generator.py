import json
import random

file = open("words_dictionary.json", "r")

words = json.load(file)

counter = 0
password = ""

# The 3 can be any number, just depends on how long you want you passwords
while counter <= 1:
    word = random.choice(list(words))
    # word length can be easily changed to make stronger passwords
    if(len(word) == 7):
        password = password + word
        counter += 1

print(password + str(random.randint(1, 11)))
