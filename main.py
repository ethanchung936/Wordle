# Play the game 'Wordle'
import random
from wordle import ScrabbleDict

def main():
    """
    The main function of the file.
    """

    # Create a dictionary of all valid 5 letter words
    wordLength = 5
    dictionary = ScrabbleDict(wordLength, 'scrabble5.txt')

    def randWord(dictionary):
        """
        Select a random word to be the solution to the puzzle

        Args:
            dictionary (ScrabbleDict): This contains all valid 5 letter words.

        Returns:
            The random word solution (str)
        """
        randLetter = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        word = random.choice(dictionary.getWords(randLetter)).upper()
        return word

    def inputWord(dictionary, attempt, guesses):
        """
        Get a guess from the user and varify it is a valid 5 letter word.

        Args:
            dictionary (ScrabbleDict): This contains all valid 5 letter words.
            attempt (int): The number of attempts the player has use.
            guesses (list): The previous guesses of the player.
        """
        guess = input('Attempt {0}: Please enter a 5 five-letter word: '.format(attempt)).upper()
        assert len(guess) >= dictionary.getWordSize(), "{0} is too short".format(guess)
        assert len(guess) == dictionary.getWordSize(), "{0} is too long".format(guess)
        assert guess.lower() in dictionary.getWords(guess[0].lower()), "{0} is not a recognized word".format(guess)
        assert guess not in guesses, "{0} was already entered".format(guess)
        return guess

    def checkLetters(guess):
        """
        Check if there are any duplicate letter in the word and add numbers to differentiate them

        Args:
            guess (str): The word the user input to try and match the solution

        Returns:
            A list of the characters in the word with any necessary number annotations
        """
        word = list(guess)
        characters = {}
        for letter in word:
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1
        for key in characters.keys():
            if characters[key] > 1:
                characters[key] += 1

        word.reverse()
        for i in range(len(word)):
            if characters[word[i]] > 1:
                characters[word[i]] -= 1
                word[i] = word[i] + str(characters[word[i]])
        word.reverse()
        return word
        


    def checkWord(guess, solution):
        """
        Check if the guessed has any matching letters to the solution in the correct postion or in it at all.

        Args:
            guess (str): The word the user input to try and match the solution
            solution (str): The word that the user is trying to guess

        Returns:
            Three lists containing letters in the word. Green indicates a correct position, yellow a letter in the solution, and red not in the solution.
        """
        green = []
        orange = []
        red = []
        solution = list(solution)
        for i in range(len(guess)):
            if guess[i][0] == solution[i]:
                green.append(guess[i])
                solution[i] = None
                guess[i] = None
        for i in range(len(solution)):
            if guess[i] != None:
                if guess[i][0] in solution:
                    orange.append(guess[i])
                    solution[solution.index(guess[i][0])] = None
                else:
                    red.append(guess[i])
        return sorted(green), sorted(orange), sorted(red)

    def gameLoop(dictionary):
        """
        A loop of the user guessing words until either the word is guessed or the number of attempts runs out.

        Args:
            dictionary (ScrabbleDict): This contains all valid 5 letter words.
        """
        attempt = 1
        maxAttempts = 6
        guesses = []
        solved = False
        solution = randWord(dictionary)
        while attempt <= maxAttempts and not solved:
            try:
                guess = inputWord(dictionary, attempt, guesses)
            except Exception as e:
                print(e.args[0])
            else:
                guesses.append(guess)
                for word in guesses:
                    wordList = checkLetters(word)
                    green, orange, red = checkWord(wordList, solution)
                    print("{0} Green={{{1}}} - Orange={{{2}}} - Red={{{3}}}".format(word, ", ".join(green), ", ".join(orange), ", ".join(red)))
                if len(green) == dictionary.getWordSize():
                    solved = True
                    attempt -= 1
                attempt += 1
        if solved:
            print("Found in {0} attempts. Well done. The Word is {1}".format(attempt, solution))
        else:
            print("Sorry you lose. The Word is {0}".format(solution))

    gameLoop(dictionary)
main()