# Copyright 2020 Paul Lu
# ------------------------------------------------------------
# Name: Krish Gandhi
# ID: 1621641
# CMPUT 274, Fall 2020
#
# Assignment #1: OO Classifier
# ------------------------------------------------------------

import sys
import copy     # for deepcopy()

Debug = False   # Sometimes, print for debugging
InputFilename = "file.input.txt"
TargetWords = [
        'outside', 'today', 'weather', 'raining', 'nice', 'rain', 'snow',
        'day', 'winter', 'cold', 'warm', 'snowing', 'out', 'hope', 'boots',
        'sunny', 'windy', 'coming', 'perfect', 'need', 'sun', 'on', 'was',
        '-40', 'jackets', 'wish', 'fog', 'pretty', 'summer'
        ]


def open_file(filename=InputFilename):
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if Debug:
            print("File Not Found")
        return(sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return(sys.stdin)


def safe_input(f=None, prompt=""):
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            assert not (f is None)
            assert (f is not None)
            line = f.readline()
            if Debug:
                print("readline: ", line, end='')
            if line == "":  # Check EOF before strip()
                if Debug:
                    print("EOF")
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)


class C274:
    def __init__(self):
        self.type = str(self.__class__)
        return

    def __str__(self):
        return(self.type)

    def __repr__(self):
        s = "<%d> %s" % (id(self), self.type)
        return(s)


class ClassifyByTarget(C274):
    def __init__(self, lw=[]):
        # FIXME:  Call superclass, here and for all classes
        self.type = str(self.__class__)
        self.allWords = 0
        self.theCount = 0
        self.nonTarget = []
        self.set_target_words(lw)
        self.initTF()
        return

    def initTF(self):
        self.TP = 0
        self.FP = 0
        self.TN = 0
        self.FN = 0
        return

    def get_TF(self):
        return(self.TP, self.FP, self.TN, self.FN)

    # FIXME:  Use Python properties
    #     https://www.python-course.eu/python3_properties.php
    def set_target_words(self, lw):
        # Could also do self.targetWords = lw.copy().  Thanks, TA Jason Cannon
        self.targetWords = copy.deepcopy(lw)
        return

    def get_target_words(self):
        return(self.targetWords)

    def get_allWords(self):
        return(self.allWords)

    def incr_allWords(self):
        self.allWords += 1
        return

    def get_theCount(self):
        return(self.theCount)

    def incr_theCount(self):
        self.theCount += 1
        return

    def get_nonTarget(self):
        return(self.nonTarget)

    def add_nonTarget(self, w):
        self.nonTarget.append(w)
        return

    def print_config(self):
        print("-------- Print Config --------")
        ln = len(self.get_target_words())
        print("TargetWords Hardcoded (%d): " % ln, end='')
        print(self.get_target_words())
        return

    def print_run_info(self):
        print("-------- Print Run Info --------")
        print("All words:%3s. " % self.get_allWords(), end='')
        print(" Target words:%3s" % self.get_theCount())
        print("Non-Target words (%d): " % len(self.get_nonTarget()), end='')
        print(self.get_nonTarget())
        return

    def print_confusion_matrix(self, targetLabel, doKey=False, tag=""):
        assert (self.TP + self.TP + self.FP + self.TN) > 0
        print(tag+"-------- Confusion Matrix --------")
        print(tag+"%10s | %13s" % ('Predict', 'Label'))
        print(tag+"-----------+----------------------")
        print(tag+"%10s | %10s %10s" % (' ', targetLabel, 'not'))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'TP   ', 'FP   '))
        print(tag+"%10s | %10d %10d" % (targetLabel, self.TP, self.FP))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'FN   ', 'TN   '))
        print(tag+"%10s | %10d %10d" % ('not', self.FN, self.TN))
        return

    def eval_training_set(self, tset, targetLabel):
        print("-------- Evaluate Training Set --------")
        self.initTF()
        z = zip(tset.get_instances(), tset.get_lines())
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class()
            if lb == targetLabel:
                if cl:
                    self.TP += 1
                    outcome = "TP"
                else:
                    self.FN += 1
                    outcome = "FN"
            else:
                if cl:
                    self.FP += 1
                    outcome = "FP"
                else:
                    self.TN += 1
                    outcome = "TN"
            explain = ti.get_explain()
            print("TW %s: ( %10s) %s" % (outcome, explain, w))
            if Debug:
                print("-->", ti.get_words())
        self.print_confusion_matrix(targetLabel)
        return

    def classify_by_words(self, ti, update=False, tlabel="last"):
        inClass = False
        evidence = ''
        lw = ti.get_words()
        for w in lw:
            if update:
                self.incr_allWords()
            if w in self.get_target_words():    # FIXME Write predicate
                inClass = True
                if update:
                    self.incr_theCount()
                if evidence == '':
                    evidence = w            # FIXME Use first word, but change
            elif w != '':
                if update and (w not in self.get_nonTarget()):
                    self.add_nonTarget(w)
        if evidence == '':
            evidence = '#negative'
        if update:
            ti.set_class(inClass, tlabel, evidence)
        return(inClass, evidence)

    # Could use a decorator, but not now
    def classify(self, ti, update=False, tlabel="last"):
        cl, e = self.classify_by_words(ti, update, tlabel)
        return(cl, e)


# TASK 2.1
class ClassifyByTopN(ClassifyByTarget):
    def __init__(self, lw=[]):
        self.type = str(self.__class__)
        super().__init__(lw)
        return

    #   Compare with classify_all() in class TrainingSet
    def classify_all(self, ts, update=True, tlabel="classify_all"):
        for ti in ts.get_instances():
            cl, e = self.classify(ti, update=update, tlabel=tlabel)
        return

    # TASK 2.2
    def target_top_n(self, tset, num=5, label=''):
        word_dictionary = {}

        training_instances = tset.inObjHash

        for i in range(len(training_instances)):
            # get words for a training instance if the instance label
            # matches the label parameter
            if training_instances[i].get_label() == label:
                word_list = training_instances[i].get_words()

                # increase the frequency of a word if it already exits in
                # the dictionary, otherwise create a new (word) key
                for word in word_list:
                    if word in word_dictionary:
                        word_dictionary[word] += 1
                    else:
                        word_dictionary[word] = 1

        new_target_words = []

        # find max frequency of all words in word_dictionary
        max_frequency = max(word_dictionary.values())

        # minimum of num words will be added to new_target_words
        while len(new_target_words) < num:
            # adding words starting from the most frequent word;
            # handles tie occurrences, especially at the num-th rank by
            # including all words with the same max_frequency
            for word in word_dictionary:
                if word_dictionary[word] == max_frequency:
                    new_target_words.append(word)

            max_frequency -= 1

        # ensure new_target_words does not contain a label word
        if label in new_target_words:
            new_target_words.remove(label)

        self.set_target_words(new_target_words)
        return


class TrainingInstance(C274):
    def __init__(self):
        self.type = str(self.__class__)
        self.inst = dict()
        # FIXME:  Get rid of dict, and use attributes
        self.inst["label"] = "N/A"      # Class, given by oracle
        self.inst["words"] = []         # Bag of words
        self.inst["class"] = ""         # Class, by classifier
        self.inst["explain"] = ""       # Explanation for classification
        self.inst["experiments"] = dict()   # Previous classifier runs
        return

    def get_label(self):
        return(self.inst["label"])

    def get_words(self):
        return(self.inst["words"])

    def set_class(self, theClass, tlabel="last", explain=""):
        # tlabel = tag label
        self.inst["class"] = theClass
        self.inst["experiments"][tlabel] = theClass
        self.inst["explain"] = explain
        return

    def get_class_by_tag(self, tlabel):             # tlabel = tag label
        cl = self.inst["experiments"].get(tlabel)
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_explain(self):
        cl = self.inst.get("explain")
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_class(self):
        return self.inst["class"]

    def process_input_line(
                self, line, run=None,
                tlabel="read", inclLabel=True
            ):
        for w in line.split():
            if w[0] == "#":
                self.inst["label"] = w
                # FIXME: For testing only.  Compare to previous version.
                if inclLabel:
                    self.inst["words"].append(w)
            else:
                self.inst["words"].append(w)

        if not (run is None):
            cl, e = run.classify(self, update=True, tlabel=tlabel)
        return(self)

    # TASK 1.1
    def preprocess_words(self, mode=''):

        def symbol_process(text):
            """ Remove punctuation and symbols (any non-alphanumeric
                characeter) in a list of words.

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
                    # characters to a temporary variable and appending the
                    # changed word to new_text
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
                new_text: a list of words with removed numbers for words
                consisting of other characters besides digits
            """
            new_text = []

            for word in text:
                # append words consisting of only numbers or only alphabets or
                # only symbols to new_text
                if word.isnumeric():
                    new_text.append(word)
                else:
                    # remove numbers by appending non-numeric characters to a
                    # temporary variable and appending the changed word to
                    # new_text
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
                          "be", "been", "being", "have", "has", "had",
                          "having", "do", "does", "did", "doing", "a", "an",
                          "the", "and", "but", "if", "or", "because", "as",
                          "until", "while", "of", "at", "by", "for", "with",
                          "about", "against", "between", "into", "through",
                          "during", "before", "after", "above", "below",
                          "to", "from", "up", "down", "in", "out", "on",
                          "off", "over", "under", "again", "further", "then",
                          "once", "here", "there", "when", "where", "why",
                          "how", "all", "any", "both", "each", "few", "more",
                          "most", "other", "some", "such", "no", "nor",
                          "not", "only", "own", "same", "so", "than", "too",
                          "very", "s", "t", "can", "will", "just", "don",
                          "should", "now"]

            new_text = []

            for word in text:
                # append non-stopwords to new_text
                if (word in stop_words) is False:
                    new_text.append(word)

            return new_text

        def preprocess_words_main():
            # assume full preprocessing
            keep_symbols = keep_digits = keep_stops = False

            # if mode is present, change the corresponding mode value to True
            if mode == "keep-symbols":
                keep_symbols = True
            elif mode == "keep-digits":
                keep_digits = True
            elif mode == "keep-stops":
                keep_stops = True

            # text contains all the words of the training instance that
            # need to be preprocessed
            text = self.inst['words']

            text = [str(word).lower() for word in text]

            # a True mode value will ignore its corresponding
            # preprocessing step
            if keep_symbols is False:
                text = symbol_process(text)
            if keep_digits is False:
                text = number_process(text)
            if keep_stops is False:
                text = stopword_process(text)

            # update the words in inObjHash
            self.inst['words'] = text
            return

        preprocess_words_main()


class TrainingSet(C274):
    def __init__(self):
        self.type = str(self.__class__)
        self.inObjList = []     # Unparsed lines, from training set
        self.inObjHash = []     # Parsed lines, in dictionary/hash
        return

    def get_instances(self):
        return(self.inObjHash)      # FIXME Should protect this more

    def get_lines(self):
        return(self.inObjList)      # FIXME Should protect this more

    def print_training_set(self):
        print("-------- Print Training Set --------")
        z = zip(self.inObjHash, self.inObjList)
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class_by_tag("last")     # Not used
            explain = ti.get_explain()
            print("( %s) (%s) %s" % (lb, explain, w))
            if Debug:
                print("-->", ti.get_words())
        return

    def process_input_stream(self, inFile, run=None):
        assert not (inFile is None), "Assume valid file object"
        cFlag = True
        while cFlag:
            line, cFlag = safe_input(inFile)
            if not cFlag:
                break
            assert cFlag, "Assume valid input hereafter"

            # Check for comments
            if line[0] == '%':  # Comments must start with %
                continue

            # Save the training data input, by line
            self.inObjList.append(line)
            # Save the training data input, after parsing
            ti = TrainingInstance()
            ti.process_input_line(line, run=run)
            self.inObjHash.append(ti)
        return

    # TASK 1.2
    def preprocess(self, mode=''):
        # iterate through all training instances
        for i in range(len(self.get_instances())):
            ti = self.get_instances()[i]
            # preprocessing a training instance
            ti.preprocess_words(mode)
        return

    # TASK 3.1
    def return_nfolds(self, num=3):
        nfolds = []

        for i in range(num):
            ts = TrainingSet()
            counter = i
            # round robin strategy is used to create num folds of the
            # original training dataset
            # counter chooses instances at num increments until there are
            # no more training instances in that counter loop
            while counter < len(self.inObjHash):
                # inObjHash and inObjList are appended with the data
                # for that specific training instance
                ts.inObjHash.append(copy.deepcopy(self.inObjHash[counter]))
                ts.inObjList.append(copy.deepcopy(self.inObjList[counter]))
                counter += num

            # add training set to nfolds
            nfolds.append(ts)
        return(nfolds)

    # TASK 3.2
    def copy(self):
        # create a deepcopy of the training set (contains the same attributes
        # as class TrainingSet) and return it
        ts = copy.deepcopy(self)
        return(ts)

    # TASK 3.3
    def add_fold(self, tset):
        # iterate through each training instance and append a deepcopy of all
        # the attributes to inObjHash and inObjList
        for i in range(len(tset.inObjHash)):
            self.inObjHash.append(copy.deepcopy(tset.inObjHash[i]))
            self.inObjList.append(copy.deepcopy(tset.inObjList[i]))
        return


def basemain():
    tset = TrainingSet()
    run1 = ClassifyByTarget(TargetWords)
    print(run1)     # Just to show __str__
    lr = [run1]
    print(lr)       # Just to show __repr__

    argc = len(sys.argv)
    if argc == 1:   # Use stdin, or default filename
        inFile = open_file()
        assert not (inFile is None), "Assume valid file object"
        tset.process_input_stream(inFile, run1)
        inFile.close()
    else:
        for f in sys.argv[1:]:
            inFile = open_file(f)
            assert not (inFile is None), "Assume valid file object"
            tset.process_input_stream(inFile, run1)
            inFile.close()

    if Debug:
        tset.print_training_set()
    run1.print_config()
    run1.print_run_info()
    run1.eval_training_set(tset, '#weather')

    return


if __name__ == "__main__":
    basemain()
