import json
import random


def generate(num_words, num_letters):
    file = open("words_dictionary.json", "r")

    words = json.load(file)

    counter = 0
    password = ""

    # change the counter max to be any number, just depends on how long you want you passwords
    while counter <= num_words:
        word = random.choice(list(words))
        # word length can be easily changed to make different passwords
        if(len(word) == num_letters):
            password += word
            counter += 1

    random_int = random.randint(0, 9)

    print(password + str(random_int))


generate(1, 7)
