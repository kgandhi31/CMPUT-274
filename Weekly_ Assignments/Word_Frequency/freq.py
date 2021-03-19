# ------------------------------------------------------------
# Name: Krish Gandhi
# ID: 1621641
# CMPUT 274, Fall 2020
#
# Weekly Exercise #3: Word Frequency
# ------------------------------------------------------------

import sys

# to check if a filename exists
import os.path


def get_filename():
    """ Use the command-line to return the name of the input file, otherwise
        print an error message along with the correct usage of the program
        and an empty string.

    Arguments:
        None

    Return:
        filename: name of the input file (if incorrect syntax, return empty
        string as filename)
    """

    filename = ""

    # print an error message (and correct usage of the program) if the syntax
    # of the command-line (argument) is incorrect
    if len(sys.argv) < 2:
        print("ERROR: Too few command-line arguments")
        print("USAGE: python3 freq.py <input_file_name>")
        return filename
    elif len(sys.argv) > 2:
        print("ERROR: Too many command-line arguments")
        print("USAGE: python3 freq.py <input_file_name>")
        return filename

    # check if filename exists in the current directory
    elif (not os.path.exists(sys.argv[1])):
        print("ERROR: Filename does not exist")
        return filename
    else:
        filename = sys.argv[1]
        return filename


def dict(filename):
    """ Create a dictionary where keys are unique words found in the input
        file and values are the corresponding frequencies.

    Arguments:
        filename: name of the input file

    Return:
        dictionary: dictionary containing unique words and their frequencies
        counter: total number of words in the input file
    """

    # use context manager to open the file and close it after reading the file
    # and adding words to dictionary along with their corresponding frequency
    with open(filename, "r") as fin:

        dictionary = {}
        counter = 0

        # iterate over each line in the file
        for line in fin:
            line = line.strip("\n").split()

            # iterate over each word in the line (line is a list)
            for word in line:
                # increase total number of words found in the input file by 1
                # on every iteration
                counter += 1

                # increase the frequency of the word if it already exits in
                # the dictionary, otherwise create a new key
                if word in dictionary:
                    dictionary[word] += 1
                else:
                    dictionary[word] = 1

    return (dictionary, counter)


def frequency_table(dictionary, counter, filename):
    """ Write a frequency table of each word, its count, and its relative
        frequency rounded to 3 decimal places to an output file (sorted
        alphabetically).

    Arguments:
        dictionary: dictionary containing unique words and their frequencies
        counter: total number of words in the input file
        filename: name of the input file

    Return:
        None (write a frequency table to an output file)
    """

    # use context manager to create an output file and close it after writing
    # to it the frequency table
    with open(filename+".out", "w") as fout:

        # sort the dictionary in lexicographic order and write each word,
        # its count, and relative frequency to the ouput file
        for word, count in sorted(dictionary.items()):
            fout.write(word + " " + str(count) + " " +
                       str(round(count/counter, 3)) + "\n")


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to
    # this exercise, so you should call your code from here.

    filename = get_filename()

    # exit the program if an error was found with the command-line (argument)
    # error checking was performed in get_filename()
    if filename == "":
        exit()
    else:
        dictionary, counter = dict(filename)

        # print error message if the file does not contain any words
        if counter == 0:
            print("ERROR: No words in {}".format(filename))
        else:
            frequency_table(dictionary, counter, filename)
