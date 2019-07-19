import random


def generate(words, num_words, num_letters):
    random_int = random.randint(0, 9)

    counter = 0
    password = ""

    while counter <= num_words:
        word = random.choice(words)
        if(len(word) == num_letters):
            password += word
            counter += 1

    return(password + str(random_int))


def randomPassword(words):
    random_int = random.randint(3, 7)

    counter = 0
    password = ""

    while counter <= random_int:
        word = random.choice(words)
        if(len(word) == random_int):
            password += word
            counter += 1

    return(password + str(random_int))
