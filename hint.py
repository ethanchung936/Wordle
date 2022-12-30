# Give hints and statistics to help try and guess a wordle word
from wordle import ScrabbleDict

def main():
    """
    The main function of the file.
    """

    # Create a ScrabbleDict of all the 5 letter words
    wordLength = 5
    dictionary = ScrabbleDict(wordLength, 'scrabble5.txt')

    def getTemplate():
        """
        Ask the user to input a template to provide a hint for.
        Verify that the input is valid.

        Returns:
            The template the user entered.
        """
        template = input("Input a template: ")
        assert len(template) >= dictionary.getWordSize(), "{0} is too short".format(template)
        assert len(template) == dictionary.getWordSize(), "{0} is too long".format(template)
        template = template.lower()
        for character in template:
            assert character in "abcdefghijklmnopqrstuvwxyz*", "Invalid input"
        return template

    def getWords(dictionary):
        """
        Get all of the words that match the template given and the letters that the user inputs.

        Args:
            dictionary (ScrabbleDict): This contains all valid 5 letter words.

        Returns:
            A (list) of all the matching words.
        """
        validTemplate = False
        while not validTemplate:
            try:
                template = getTemplate()
            except Exception as e:
                print(e.args[0])
            else:
                validTemplate = True
        validLetters = False   
        while not validLetters:
            try:
                letters = input("Input letters: ")
                validWords = dictionary.getConstrainedWords(template, letters)
            except Exception as e:
                print(e.args[0])
            else:
                validLetters = True
                return validWords

    def countLetters(dictionary):
        """
        Detemine how many times each letter appears in 5 letter words.

        Args:
            dictionary (ScrabbleDict): This contains all valid 5 letter words.

        Returns:
            A (dict) containing the number of instances of each letter.
        """
        letterCount = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for letter in alphabet:
            for word in dictionary.getWords(letter):
                for character in word:
                    if character in letterCount:
                        letterCount[character] += 1
                    else:
                        letterCount[character] = 1
        return letterCount

    def letterPercent(letterCount):
        """
        Determine the percent that each letter comprises in 5 letter words.

        Args:
            letterCount (dict): Contains the number of instances of each letter.

        Returns:
            A (dict) that contains the percent of each letter.
        """
        total = 0
        percent = {}
        for letter in letterCount:
            total += letterCount[letter]
        for letter in letterCount:
            percent[letter] =  (letterCount[letter] / total) * 100
        return percent
        
    def letterFrequency(dictionary):
        """
        Print the information about the frequency of letters in 5 letter words.

        Args:
            dictionary (ScrabbleDict): This contains all valid 5 letter words.
        """
        count = countLetters(dictionary)
        percent = letterPercent(count)
        for letter in sorted(count):
            print("{0}:{1:>5}{2:6.2f}%  {3}".format(letter.upper(), count[letter], percent[letter], "*" * round(percent[letter])))

    def wordHint(dictionary):
        """
        Output the hint for the word in the form of multiple lines rather than a list.

        Args:
            dictionary (ScrabbleDict): This contains all valid 5 letter words.
        """
        ValidWords = getWords(dictionary)
        if len(ValidWords) == 0:
            print("No valid words")
        else:    
            for word in ValidWords:
                print(word)

    # Run the functions to produce an output
    letterFrequency(dictionary)
    print()
    wordHint(dictionary)

main()