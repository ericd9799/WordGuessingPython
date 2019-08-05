#! /usr/bin/python3

import random as rd
import pandas as pd

'''
    Word guessing game.
'''
def ReadWordsFromFile(filename):
    #Reading file not using panda
    '''
    f = open(filename, "r")
    TupleOfWords = tuple(f.read().split(", "))
    print(TupleOfWords)
    '''

    #Reading file using panda
    data = pd.read_csv(filename, header=None)
    #print(data)
    #print(f"Length of {data[5][0]} is {len(data[5][0])}.")
    return data

def SelectWordToGuess(w):
    #Generate a random # to randomize word selected
    rint = rd.randint(0, 6)
    WordToGuess = w[rint][0]
    #Below is used for testing. It will keep the word to be constant.
    #WordToGuess = w[0][0]
    Game(WordToGuess)

def Game(w):
    Letters = list(w.upper())
    Temp = ["_"] *len(w)
    Guesses = []
    a = 0

    while True:
        if a <= len(Letters):
            #print(f"Guess count {a}")
            print(f"This word is {len(w)} characters long. ")
            print(" ".join(Temp))
            guess = input("What is your guess: ").upper()
            if guess not in Guesses:
                #List of letters user has guessed. Will be used to notify if user has already guessed letter.
                Guesses.append(guess)
                #print(Guesses)

                for i in range(len(Letters)):
                    if guess == Letters[i]:
                        Temp[i] = guess

                if "_" not in Temp:
                    print(f"Winner! You guessed the word, {w.upper()}!")
                    return True
                    break

                a += 1
            else:
                print("You already guessed that letter!")
        else:
            print(f"Too many guesses! The word is {w.upper()}.")
            return False
            break


def main():
    intro = '''
        Welcome! You are about to play the word guessing game.
        The word selected will be random, and the length of the
        word is the number of guesses you have. For example, if
        the word is "apple", then you have 5 guess to correctly
        guess the word!

        If you are ready to play, input Y: '''

    if input(intro).upper() == 'Y':
        while True:
            w = ReadWordsFromFile("WordsToGuess.txt")
            SelectWordToGuess(w)

            if input("Play again (Y/N): ").upper() != 'Y':
                print("Thank you for playing!")
                break
    else:
        print("Not a problem! We will be here waiting for you!")

if __name__ == "__main__":
    main()
