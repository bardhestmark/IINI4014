import string
from collections import Counter
from pathlib import Path


# recursive function for finding a file's path given a directory and a file name.
def find_file_path(directory, filename):
    filepath = None

    for x in directory.iterdir():
        if x.name == filename:
            filepath = Path(x)
        elif x.is_dir():
            filepath = find_file_path(x, filename)
        if filepath:
            break
    if filepath:
        return filepath
    raise Exception("Unable to find requested file")


# helper function, reads every word from file into a list while removing punctuation and making
# everything lowercase
def make_words_list(path):
    wordlist = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                wordlist.append(word.translate(str.maketrans('', '', string.punctuation)).lower())
    return wordlist


# makes a list of words and uses a Counter to count the frequency of each word
def getwordfreqs(filename):
    path = find_file_path(Path(), filename)

    wordlist = make_words_list(path)
    if wordlist:
        return Counter(wordlist)


# finds the line numbers of which a specified word is found within a file
def getwordsline(filename, word):
    path = find_file_path(Path(), filename)

    with open(path, "r", encoding="utf-8") as f:
        line_counter = 1
        line_numbers = []
        for line in f:
            for w in line.split():
                if word.lower() == w.translate(str.maketrans('', '', string.punctuation)).lower():
                    line_numbers.append(line_counter)
            line_counter += 1
        if line_numbers:
            return line_numbers
        else:
            return 'Unable to find word in file'


if __name__ == '__main__':
    filename = 'pg27827.txt'
    word = 'cucumber'

    print(getwordfreqs(filename))
    print(getwordsline(filename, word))
