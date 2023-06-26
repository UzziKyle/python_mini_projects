import pyjokes as pj
import random as rand
from os import system as sys

jokes = pj.get_jokes()

def makeMeLaugh(jokes=list) -> str:
    return jokes[rand.randint(0, len(jokes))]

while True:
    sys('cls')

    print(makeMeLaugh(jokes))

    option_input = input("\nWould you like another joke? (y/n)\n>").strip().lower()

    if option_input == 'y':
        continue

    else: 
        sys('cls')
        print('Bye!')
        break