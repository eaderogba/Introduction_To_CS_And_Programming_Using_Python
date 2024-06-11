# Problem Set 2, hangman.py
# Name: Adebowale Aderogba
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------
WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    check = ""
    for letter in secret_word:
      if letter in letters_guessed:
        check += letter
      else:
        check += "*"
    return check

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ""
    for letter in string.ascii_lowercase:
      if letter not in letters_guessed:
        available_letters += letter
    return available_letters
  

def helper_function(secret_word, available_letters):
    """
    Reveals a random letter from the secret_word that has not been guessed yet
    """
    choose_from = ""
    for char in secret_word:
      if char in available_letters:
        choose_from += char
    if choose_from:
      revealed_letter = random.choice(choose_from)
      return revealed_letter
    return revealed_letter

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # let the user know how many letters the secret_word contains and how many guesses they start with
    letters_guessed = []
    number_guess_left = 10
    vowels = "aeiou"
    unique = ""
    
    # Let the user know how many letters the secret_word contains
    print(f"Welcome to Hangman! \nI am thinking of a word that is {len(secret_word)} letters long.")
    print(secret_word)
    
    while not has_player_won(secret_word, letters_guessed) and number_guess_left > 0:
      print("-"*10)
      print(f"You have {number_guess_left} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      user_input = input("Please guess a letter: ").lower()
      
      if len(user_input) != 1 or (not user_input.isalpha() and user_input != '!'):
        print("Invalid input. Please enter a single letter or '!' for help.")
        continue
        
      if user_input in letters_guessed and user_input != '!':
        print("You have already guessed that letter. Please try again.")
        continue
      
      if with_help and user_input == '!':
        if number_guess_left < 3:
          print("Not enough guesses left for help.")
        else:
          number_guess_left -= 3
          revealed_letter = helper_function(secret_word, get_available_letters(letters_guessed))
          if revealed_letter:
            letters_guessed.append(revealed_letter)
            print(f"Help used! The letter '{revealed_letter}' has been revealed")
            print(f"Letter revealed: {get_word_progress(secret_word, letters_guessed)}")
          else:
            print("No more letters to reveal.")
        continue
      
      letters_guessed.append(user_input)
      
      # Checkpoint
      print(letters_guessed)
    
      if user_input in secret_word:
        print(f"Good guess: {get_word_progress(secret_word, letters_guessed)}")
        number_guess_left -= 1
      else:
        if user_input in vowels:
          number_guess_left -= 2
        else:
          number_guess_left -= 1
        print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
        
      if has_player_won(secret_word, letters_guessed):
        print("Congratulations, you won!")
        for char in secret_word:
          if char not in unique:
            unique += char
        total_score = ((number_guess_left + 4) * len(unique)) + (3 * len(secret_word))
        print(f"Your total score for this game is: {total_score}")
        break
      if number_guess_left == 0:
        print(f"Sorry, you ran out of guesses. The word was '{secret_word}'")
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.
    
    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

