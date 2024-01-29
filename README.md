# Wordle
An adaptation of the popular puzzle game Wordle created in Python. Created for CMPUT 175 Winter 2022.

To play wordle run the main.py file. You will then be prompted to guess a five letter word, and feedback will be provided showing how closely your guess matches the 
mystery word. The player gets six guesses to guess the word, if guessed correctly a victory message will be shown, if not correctly guessed within 6 tries the player
will lose and the word will be revealed.

wordle.py contains functions that are used in main file and serve to organize and analyze the data from the list of words in scrabble5.txt. scrabble5.txt is the list of possible words that can be guessed and can potentially be the mystery word.

hint.py is a file that is used to provide the user with statistics about possible words and give a list of possible words based on what the user has input.
to use this, run hint.py and enter a five character word template where the * character is unknown letters and an alphabetical character is a letter in a known spot. Next enter any letters that are in the word but in unknown places and a list of possible words will be returned.
