# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

def check_word(word):
    if wordlist.count(word) > 0:
        return 1
    else:
        for words in wordlist:
            if words.startswith(word):
                return 2
    return 0

# TO DO: your code begins here!
def ghost():
    counter = 0
    word_frag = ''
    print 'Welcome to Ghost!'
    while True:
        if counter != 0:
            print 'Current word fragment is:',word_frag
            print 'Player', (counter % 2)+1,'\'s turn.'
        else:
            print 'The current word fragment is None'
            print 'Player 1 goes first.'
        print 'Player',(counter % 2)+1,'says letter: ',
        letter = raw_input().lower()
        if letter not in string.ascii_letters:
            print 'Only single alphabets are accepted. Try again.'
            continue
        word_frag += letter
        if check_word(word_frag) <= 0:
            if counter % 2 == 0:
                print 'Player 2 wins the game',
            else:
                print 'Player 1 wins the game',
            print 'because there are no words that are/can be formed from:',word_frag,'!'
            break
        if len(word_frag) > 3:
            if check_word(word_frag) == 1:
                if (counter % 2) == 0:
                    print 'Player 2 wins the game',
                else:
                    print 'Player 1 wins the game',
                print 'because',word_frag,'is a word!'
                break
        counter += 1
        
        
        
