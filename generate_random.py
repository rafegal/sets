import names
from datetime import datetime
import string
import random

def generate_names():
    print(datetime.now())
    with open('names_b.txt', 'w') as file:
        for i in range(100000):
            file.write(names.get_full_name() + '\n')
    print(datetime.now())


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def generate_random_string():
    print(datetime.now())
    with open('random_string_b.txt', 'w') as file:
        for i in range(10000000):
            file.write(randomString() + '\n')
    print(datetime.now())

if __name__ == "__main__":
    generate_random_string()
    #generate_random_string()