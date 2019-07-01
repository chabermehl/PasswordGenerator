import sys
import json
import random


def main():
    generated_password = generate(int(sys.argv[1]), int(sys.argv[2]))
    print(generated_password)


def generate(num_words, num_letters):
    file = open("words_dictionary.json", "r")

    words = json.load(file)

    random_int = random.randint(0, 9)
    counter = 0
    password = ""

   # change the counter max to be any number, just depends on how long you want you passwords
    while counter <= num_words:
        word = random.choice(list(words))
        # word length can be easily changed to make different passwords
        if(len(word) == num_letters):
            password += word
            counter += 1

    return(password + str(random_int))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
