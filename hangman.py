import random
from words import words
#contains the list of the words that will be guessed
import string

def get_valid_word(words):  
    #eliminates the words containing dashes or spaces
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    
    return word.upper()

def hangman():
    word=get_valid_word(words)
    word_letters=set(word)    #converts the string to a set of lettters
    alphabet=set(string.ascii_uppercase)
    used_letters=set()       #used to store the letters the user has typed
    
    lives=10  #number of tries a user can try to guess the word
    
    #to set up the REPL for the user to contnually guess the wor
    #takes input from user and checks if the letter was typed
    while len(word_letters)>0 and lives>0:
        print('You have ',lives,' lives and you have used these letters ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word :', ' '.join(word_list))

        user_letter=input('Guess a letter: ').upper()
        if user_letter in alphabet  - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives-1
                print('letter is not in word')

        elif user_letter in used_letters:
            print('Try again you have already used that character')
        
        else:        
            print('Invalid')
    
    if lives == 0:
        print('You died SORRY! the word was ',word)
    else:
        print('You guessed the word ',word,' !!!!')


hangman()