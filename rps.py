import random
import os
import re

# Comment
def check_play_status():
    # valid_responses = ['yes', 'no', 'y']
    while True:
        try:
            response = input('Do you wish to play again? (Yes or No): ')
            if response.lower() not in ['yes', 'no', 'y']:
                raise ValueError('Yes or No only')

            if response.lower() in ['yes', 'y']:
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Thanks for playing!')
                exit()

        except ValueError as err:
            print(err)


def play_rps():
    play = check_play_status()

play_rps()

