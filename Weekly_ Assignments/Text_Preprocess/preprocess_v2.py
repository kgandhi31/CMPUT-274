# ------------------------------------------------------------
# Name: Krish Gandhi
# ID: 1621641
# CMPUT 274, Fall 2020
#
# Weekly Exercise #4: Text Preprocessor
# ------------------------------------------------------------

import sys


def symbol_process(text):
    """ Remove punctuation and symbols (any non-alphanumeric characeter)
        in a list of words.

    Arguments:
        text: a list of words in lowercase

    Return:
        new_text: a list of words with removed punctuation and symbols
    """

    new_text = []

    for word in text:
        # append alphanumeric words to new_text
        if word.isalnum():
            new_text.append(word)
        else:
            # remove punctuation and symbols by appending alphanumeric
            # characters to a temporary variable and appending the changed
            # word to new_text
            temp = ""
            for char in word:
                if char.isalnum():
                    temp += char

            # do not append empty strings in new_text
            if (temp == "") is False:
                new_text.append(temp)

    return new_text


def number_process(text):
    """ Remove all numbers in a list of words, unless a word consists
        of only numbers.

    Arguments:
        text: a list of words in lowercase

    Return:
        new_text: a list of words with removed numbers for words consisting
        of other characters besides digits
    """

    new_text = []

    for word in text:
        # append words consisting of only numbers or only alphabets or
        # only symbols to new_text
        if word.isnumeric():
            new_text.append(word)
        else:
            # remove numbers by appending non-numeric characters to a
            # temporary variable and appending the changed word to new_text
            temp = ""
            for char in word:
                if char.isdigit() is False:
                    temp += char

            # temp cannot be empty here
            new_text.append(temp)

    return new_text


def stopword_process(text):
    """ Remove all stopwords from a list of words.

    Arguments:
        text: a list of words in lowercase

    Return:
        new_text: a list of words with removed stopwords
    """

    stop_words = ["i", "me", "my", "myself", "we", "our", "ours",
                  "ourselves", "you", "your", "yours", "yourself",
                  "yourselves", "he", "him", "his", "himself", "she",
                  "her", "hers", "herself", "it", "its", "itself",
                  "they", "them", "their", "theirs", "themselves",
                  "what", "which", "who", "whom", "this", "that",
                  "these", "those", "am", "is", "are", "was", "were",
                  "be", "been", "being", "have", "has", "had", "having",
                  "do", "does", "did", "doing", "a", "an", "the", "and",
                  "but", "if", "or", "because", "as", "until", "while",
                  "of", "at", "by", "for", "with", "about", "against",
                  "between", "into", "through", "during", "before",
                  "after", "above", "below", "to", "from", "up", "down",
                  "in", "out", "on", "off", "over", "under", "again",
                  "further", "then", "once", "here", "there", "when",
                  "where", "why", "how", "all", "any", "both", "each",
                  "few", "more", "most", "other", "some", "such", "no",
                  "nor", "not", "only", "own", "same", "so", "than",
                  "too", "very", "s", "t", "can", "will", "just", "don",
                  "should", "now"]

    new_text = []

    for word in text:
        # append non-stopwords to new_text
        if (word in stop_words) is False:
            new_text.append(word)

    return new_text


def main():
    """ Use the command-line argument to recognize if mode is present, error
        handle incorrect command-line arguments along with printing proper
        usage of the program, and perform the user requested preprocessing
        steps for the single-line input string.

    Arguments:
        None

    Return:
        None (print the preprocessed_text as a space-separated string)
    """

    # assume full preprocessing
    keep_symbols = keep_digits = keep_stops = False

    usage = ("USAGE: python3 preprocess.py <mode>, where mode can be " +
             "<keep-symbols>, <keep-digits>, <keep-stops>, or <>")

    # print error message and correct usage of the program if the syntax
    # of the command-line (argument) is incorrect
    if len(sys.argv) > 2:
        print("ERROR: Too many command-line arguments\n" + usage)
        exit()
    # if mode is present, change the corresponding mode value to True
    elif len(sys.argv) == 2:
        if sys.argv[1] == "keep-symbols":
            keep_symbols = True
        elif sys.argv[1] == "keep-digits":
            keep_digits = True
        elif sys.argv[1] == "keep-stops":
            keep_stops = True
        else:
            print("ERROR: Incorrect mode value\n" + usage)
            exit()

    # exit the program if Ctrl+D is pressed
    try:
        # split input text into tokens by whitespace,
        # and convert all words to lowercase
        text = [str(word).lower() for word in input().split()]
    except EOFError:
        exit()

    # complete remaining preprocessing steps for the text;
    # a True mode value will ignore its corresponding preprocessing step;
    # text may change during a preprocess;
    # 'changed' text is used in the next preprocess
    if keep_symbols is False:
        text = symbol_process(text)
    if keep_digits is False:
        text = number_process(text)
    if keep_stops is False:
        text = stopword_process(text)

    preprocessed_text = text

    print(*preprocessed_text)


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 preprocess.py". This is directly relevant
    # to this exercise, so you should call your code from here.

    main()
