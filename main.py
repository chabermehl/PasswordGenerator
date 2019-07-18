import sys
import json
import random
import argparse
import pyperclip


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


def main():
    file = open("words_dictionary.json", "r")
    word_list = list(json.load(file))

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "words", nargs="?", help="number of words, requires letters", type=int)
    parser.add_argument(
        "letters", nargs="?", help="number of letters, requires words", type=int)
    parser.add_argument(
        "-r", "--random", help="produce a random password", action="store_true")
    parser.add_argument(
        "-p", "--private", help="do not print password to console", action='store_true')

    args = parser.parse_args()

    if(args.random):
        generated_password = randomPassword(word_list)
    else:
        generated_password = generate(word_list, args.words, args.letters)

    if args.private == False:
        print("Your password has been copied to your clipboard!")
        print("Password: " + generated_password)
        pyperclip.copy(generated_password)
    else:
        print("Your password has been copied to your clipboard!")
        pyperclip.copy(generated_password)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
