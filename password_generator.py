import sys
import json
import random
import argparse
import pyperclip

# Arg parser to simplify using command line args. -h help is provided automatically.
parser = argparse.ArgumentParser()

parser.add_argument("-w", "--words", help="number of words", type=int)
parser.add_argument("-l", "--letters", help="number of letters", type=int)
parser.add_argument(
    "-p", "--private", help="do not print password to console", action='store_true')
args = parser.parse_args()


def main():
    generated_password = generate(args.words, args.letters)

    # Still prints out stars if in private mode, just so that it's clear that the script executed.
    if args.private == False:
        print(generated_password)
    else:
        print("**************")
        pyperclip.copy(generated_password)


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
