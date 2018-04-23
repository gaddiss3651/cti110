# CTI-110 
# P5HW2 - Guessing Game
# Shannon Gaddis
# April 22, 2018

import random

def main():
    play = True    
    while play:
        guessNum = 0 
        number = random.randint(1, 100)
        print('Guess the secret number between 1 and 100.')

        while guessNum != number:
            print('Take a guess.')
            guess = input()
            guess = int(guess)

            guessNum = guessNum + 1

            if guess < number:
                print('Too low, try again.')                    

            if guess > number:
                print('Too high, try again.')

            if guess == number:
                break

        if guess == number:
            guessNum = str(guessNum)
            print('WELL DONE! You guessed the secret number in ' + guessNum + ' guesses!')
            again= input('Guess again? (y = yes): ')

            if again != 'y':
                print('Thanks for playing. Bye!')
                play = False

main()


