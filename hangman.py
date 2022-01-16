import string
from random import choice
from algos import bruteForce, doDecreasebyConstant, avl
import sys


class Game():
    maxGuess = 6
    hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    def __init__(self):
        self.word = self.random_word()
        self.wrongGuess = []
        self.correct = []
        self.progress = self.get_progress()
        self.gameover = False

    def random_word(self):
        dictionary = open('dictionary.txt', 'r').readlines()
        words = [word.strip() for word in dictionary]
        return choice(words)

    def get_progress(self):
        return "".join([let if let in self.correct else "_" for let in self.word])

    def already_guessed(self, guess):
        return guess in self.correct + self.wrongGuess

    def guess_letter(self, guess):
        if guess in self.word:
            self.correct.append(guess)
        else:
            self.wrongGuess.append(guess)

    def status(self):
        if len(self.wrongGuess) >= Game.maxGuess:
            self.gameover = True
            return "\nYou lost. The word was %r." % self.word
        if set(self.correct) == set(self.word):
            self.gameover = True
            return "\nYou won!"
        return "" 

    def __str__(self):
        result = "\n" + "-" * 30 + "\n"
        result += Game.hangman[len(self.wrongGuess)]
        result += "\nProgress: %s" % self.get_progress()
        result += "\nIncorrect guesses: %s" % ", ".join(self.wrongGuess)
        result += self.status()
        return result
   
    def setWord(self,word, tree, root):
        print("Hangman needs to validate your word. ")
        print("Type the following algorithm you'd like to use. \nBrute Force, Decrease and Conqure, Binary tree")
        algo = input("\"brute\", \"decrease\",\"tree\"\n")
        if(algo == "tree"):
            self.word = avl(word, tree, root)
        elif(algo == "decrease"):
            self.word = doDecreasebyConstant(word)
        else:
            self.word = bruteForce(word) 


#------------------------------------------------------------------------------
def valid_guess(game):
    while True:
        guess = input("Guess a letter: ").lower()        
        if len(guess) > 1:
                if guess == 'quit':
                    return 'quit'
                else:
                    print ("Please guess a letter.")
        elif game.already_guessed(guess):
            print ("You've already guessed %r." , guess)
        else:
            return guess


