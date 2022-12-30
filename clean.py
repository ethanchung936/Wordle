def main():
    """
    The main function of the file.
    """
    def readFile(filename):
        """
        Reads the given file lines.

        Args:
            filename (str): The name of the file to read.

        Returns:
            A (list) of the lines of the file.
        """
        file = open(filename, 'r')
        contents = file.read()
        lines = contents.splitlines()
        file.close()
        return lines

    def writeFile(filename, lines):
        """
        Write words to a new file based on the lines given.

        Args:
            filename (str): The name of the file to write
            lines (list): A list of the lines of words seperated by a #.
        """
        newFile = open(filename, 'w')
        for line in lines:
            lineList = line.split('#')
            for element in lineList:
                if not element == '':
                    newFile.write("{}\n".format(element))
        newFile.close()
    
    lines = readFile('word5Dict.txt')
    writeFile('Scrabble5.txt', lines)

main()