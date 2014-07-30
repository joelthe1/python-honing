# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
#

import random
import string
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

points_dict = {}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...
    score = 0
    if len(word) > n or len(word) <= 0:
        assert 'Invalid word formed. '
    if len(word) == n:
        score = 50
    for i in word:
        score = score + SCRABBLE_LETTER_VALUES[i]
    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    for letter in word:
        if hand.get(letter,0) > 0:
            if hand[letter] == 1:
                hand.pop(letter)
            else:
                hand[letter] = hand[letter] - 1
    return hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    if points_dict.get(word,-1) < 0:
        return False
    for letter in word:
        if word.count(letter) > hand.get(letter,0):
            return False
    return True

#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    #print "play_hand not implemented." # replace this with your code...
    score = 0.0
    while True:
        print 'Current hand:',display_hand(hand)
        start = time.time()
        word = raw_input('Enter word or a . to finish: ')
        end = time.time()
        if word == '.':
            print 'Your total score is %.2f' % score
            print 'Exiting Game!'
            break
        elif not is_valid_word(word,hand,word_list):
            print word,'is an invalid word. Try again.'
        else:
            time_taken = end - start
            if time_taken <= 0:
                time_taken = 1
                print 'You took no time to answer. You\'ve won yourself a 1000 point bonus!'
                score += 1000.0
            else:
                print 'It took %.2f seconds to provide an answer.' % time_taken
            score += (get_word_score(word,HAND_SIZE)/time_taken)
            print word,'earned {:.2f} points. Total score is: {:.2f} points'.format(score, get_word_score(word,HAND_SIZE)/time_taken)
            hand = update_hand(hand,word)
            if len(hand) <= 0:
                print 'Your Total score is %.2f' % score
                print 'Game over.'
                break
            
#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
#    print "play_game not implemented."         # delete this once you've completed Problem #4
#    play_hand(deal_hand(HAND_SIZE), word_list) # delete this once you've completed Problem #4
    
    ## uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand2(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand2(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."


#
# Problem #4: Playing a hand
#
def play_hand3(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    score = 0.0
    total_time =  0.0
    time_limit = float(raw_input('Enter time limit, in seconds, for players: '))
    while time_limit < 0:
        print 'Invalid value of time entered. Please enter a positive value.'
        time_limit = raw_input('Enter time limit, in seconds, for players: ')        
    while True:
        print 'Current hand:',display_hand(hand)
        start = time.time()
        word = raw_input('Enter word or a . to finish: ')
        end = time.time()
        if word == '.':
            print 'Your total score is %.2f' % score
            print 'Exiting Game!'
            break
        elif not is_valid_word(word,hand,word_list):
            print word,'is an invalid word. Try again.'
        else:
            time_taken = end - start
            total_time += time_taken
            print 'It took %.2f seconds to provide an answer.' % time_taken
            if time_taken <= 0:
                time_taken = 1
                print 'You took no time to answer. You\'ve won yourself a 1000 point bonus!'
                score += 1000.0
            elif total_time <= time_limit:
                score += (get_word_score(word,HAND_SIZE)/time_taken)
                hand = update_hand(hand,word)
                print word,'earned {:.2f} points. Total score is: {:.2f} points'.format(score, get_word_score(word,HAND_SIZE)/time_taken)
                print 'You have %.2f seconds remaining.' % (time_limit - total_time)
            elif total_time > time_limit:
                print 'Total time exceeds {:.2f} seconds. You scored {:.2f} points.'.format(time_limit,score)
                break
            if len(hand) <= 0:
                print 'Your Total score is %.2f' % score
                print 'Game over.'
                break

def pick_best_word(hand):
    """ Return the highest scoring word from points_dict that can be made with the
    given hand.
     Return '.' if no words can be made with the given hand.
    """ 
    


def get_words_to_points(word_list):
    """ Return a dict that maps every word in word_list to its point value.  """
    for words in word_list:
        score = 0
        for letters in words:
            score += SCRABBLE_LETTER_VALUES[letters]
        global points_dict
        points_dict[words] = score
        
def play_hand2(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    
    score = 0.0
    total_time =  0.0
    time_limit = float(raw_input('Enter time limit, in seconds, for players: '))
    while time_limit < 0:
        print 'Invalid value of time entered. Please enter a positive value.'
        time_limit = raw_input('Enter time limit, in seconds, for players: ')        
    while True:
        print 'Current hand:',display_hand(hand)
        start = time.time()
        word = raw_input('Enter word or a . to finish: ')
        end = time.time()
        if word == '.':
            print 'Your total score is %.2f' % score
            print 'Exiting Game!'
            break
        elif not is_valid_word(word,hand):
            print word,'is an invalid word. Try again.'
        else:
            time_taken = end - start
            total_time += time_taken
            print 'It took %.2f seconds to provide an answer.' % time_taken
            if time_taken <= 0:
                time_taken = 1
                print 'You took no time to answer. You\'ve won yourself a 1000 point bonus!'
                score += 1000.0
            elif total_time <= time_limit:
                score += (get_word_score(word,HAND_SIZE)/time_taken)
                hand = update_hand(hand,word)
                print word,'earned {:.2f} points. Total score is: {:.2f} points'.format(score, get_word_score(word,HAND_SIZE)/time_taken)
                print 'You have %.2f seconds remaining.' % (time_limit - total_time)
            elif total_time > time_limit:
                print 'Total time exceeds {:.2f} seconds. You scored {:.2f} points.'.format(time_limit,score)
                break
            if len(hand) <= 0:
                print 'Your Total score is %.2f' % score
                print 'Game over.'
                break



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
