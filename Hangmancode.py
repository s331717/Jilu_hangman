import random
from wordslist import words

def get_word():
    word =random.choice(words)
    return word.upper()

def hangman():
    word = get_word()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    guessed_letter=[]
    lives =6
    guessed = False
    print(len(word),'letters in the word')
    print(len(word)*'_')

    while guessed == False and lives > 0:
        print(lives,'lives left')
        guess = input('guess a letter:').upper()
        if len (guess) == 1:
            if guess not in alphabet:
                print('Invalid character')
                lives -=1
            elif guess in guessed_letter:
                print('you have already guessed the letter')
            elif guess not in word:
                print('Guessed letter not present in the word')
                guessed_letter.append(guess)
                lives -=1
            elif guess in word:
                print('your guess is present in the word')
                guessed_letter.append(guess)
        status = ''
        if guessed == False:
            for letter in word:
                if letter in guessed_letter:
                    status += letter
                    if status == word:
                        lives = 0
                        print('you win the game')
                elif letter not in guessed_letter:
                    status += '_'
            print(status)
    print('You run out of guesses')    
hangman()