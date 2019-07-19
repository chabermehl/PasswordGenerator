import random
import string


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


def random_password(words):
    random_int = random.randint(3, 7)

    counter = 0
    password = ""

    while counter <= random_int:
        word = random.choice(words)
        if(len(word) == random_int):
            password += word
            counter += 1

    return(password + str(random_int))


def alpha_numeric():
    random_int = random.randint(8, 16)

    characters = string.ascii_letters + string.digits
    if(random_int >= 10):
        password = ''.join(random.choice(characters)
                           for i in range(random_int - 2))
    else:
        password = ''.join(random.choice(characters)
                           for i in range(random_int - 1))

    return(password + str(random_int))
