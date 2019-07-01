import sys
import json
import random

# TODO add validity checks
# TODO add more command line options, -help etc
# TODO make a simple GUI


def main():
    generated_password = generate(int(sys.argv[1]), int(sys.argv[2]))
    print(generated_password)


def generate(num_words, num_letters):
    file = open("words_dictionary.json", "r")

    words = json.load(file)

    random_int = random.randint(0, 9)
    counter = 0
    password = ""

    while counter <= num_words:
        word = random.choice(list(words))
        if(len(word) == num_letters):
            password += word
            counter += 1

    return(password + str(random_int))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
