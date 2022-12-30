class ScrabbleDict:
    """
    A class to store data from a file of words and perform operations to access them
    """
    def __init__(self, size, filename):
        """
        Initialize a ScrabbleDict by creating a dicitionary full of words.

        Args:
            size (int): The length of the words in the dictionary.
            filename (str): The name of the file that contains the words.
        """
        self.dct = {}
        self.size = size
        file = open(filename, 'r')
        for line in file.readlines():
            lineList = line.split()
            if len(lineList[0]) == size:
                self.dct[lineList[0]] = lineList[0]
        file.close()
        

    def check(self, word):
        """
        Returns True if word is in the dictionary and False otherwise.

        Args:
            word (str): The word that should be checked.
        Returns:
            (Bool) True or False depending on whether the word is in the dictionary.
        """
        return word in self.dct

    def getSize(self):
        """
        Gets the number of words in the dictionary.

        Returns:
            The number of words in the diction (int)
        """
        return len(self.dct)

    def getWords(self, letter):
        """
        Returns a sorted list of words in the dictionary starting with the character letter.

        Args:
            letter (str): The letter that the word should start with.
        Returns:
            A (list) of all the words in the dictionary starting with the letter in alphabetical order.
        """
        wordList = []
        for key in list(self.dct.keys()):
            if key[0] == letter:
                wordList.append(key)
        return sorted(wordList)

    def getWordSize(self):
        """
        Get the length of the words in the dictionary.

        Returns:
            The length of the words stored in the dictionary. (int)
        """
        return self.size

    def getMaskedWords(self, template):
        """
        Get a list of words that could fit the given template.

        Args:
            Template (str): A sequence of letters and unknown characters that are used to narrow down possible words.

        Returns:
            A (list) list of words that could fit the given template.
        """
        assert len(template) >= self.size, "{0} is too short".format(template)
        assert len(template) == self.size, "{0} is too long".format(template)
        template = template.lower()
        options = [word for word in self.dct]
        for i in range(len(template)):
            assert template[i] in "abcdefghijklmnopqrstuvwxyz*", "Invalid input"
            if template[i] != '*':
                for word in range(len(options)):
                    if options[word] != None:
                        if template[i] != options[word][i]:
                            options[word] = None
        return list(filter(None, options))

    def getConstrainedWords(self, template, letters):
        """
        Get a list of words that could fit the given template and the extra letters given.

        Args:
            Template (str): A sequence of letters and unknown characters that are used to narrow down the possible words.
            Letters (str): Extra letters that are part of the word in an unknown location

        Returns:
            A (list) of words that fit the given template and extra letters. 
        """
        words = self.getMaskedWords(template)
        template = list(template)
        blanks = []
        for i in range(len(template)):
            if template[i] == '*':
                blanks.append(i)
        letters = letters.lower()
        assert len(letters) <= len(blanks), "Too many letters"
        for letter in letters:
            assert letter in "abcdefghijklmnopqrstuvwxyz", "Invalid letters"
        for i in range(len(words)):
            valid = True
            options = []
            for index in blanks:
                options.append(words[i][index])
            for letter in letters:
                if letter not in options:
                    valid = False
                else:
                    options.remove(letter)
            if not valid:
                words[i] = None
        return list(filter(None, words))



if __name__ == "__main__":
    # create the dictionary
    dictionary = ScrabbleDict(5, 'scrabble5.txt')

    # The first four tests test the check method in various ways.
    print("See if apple is in the dictionary:")
    print(dictionary.check('apple'),"\n")

    print("See if apples (too long) is in the dictionary:")
    print(dictionary.check('apples'), "\n")

    print("See if feel (too short) is in the dictionary:")
    print(dictionary.check('feel'), "\n")

    print("See if dsfhk (not a word) is in the dictionary:")
    print(dictionary.check('dsfhk'), "\n")
    #######################################################

    # Test the getSize method
    print("Get the size of the dictionary:")
    print(dictionary.getSize(), "\n")

    # test the getWords method
    print("Get all words starting with f:")
    print(dictionary.getWords('f'), "\n")

    # test the getWordSize method
    print("Get the length of the words in the dictionary:")
    print(dictionary.getWordSize(), "\n")

    # test the getMaskedWords method
    print("Get all words that fit the format **t*s")
    print(dictionary.getMaskedWords("**t*s"), "\n")

    # test the getConstrainedWords method
    print("Get the list of words that fit the format th*** with the letter oe:")
    print(dictionary.getConstrainedWords('th***', 'oe'))