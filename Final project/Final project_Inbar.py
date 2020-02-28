## Final project ##
## Benjamin Inbar ##
"Hangman"

print("""

Welcome to Hangman!""")

input("\nTo begin, press enter\n")

print("""\nType a letter. If the letter is in the word, the letter is revealed and you get another guess.

But, you only have 10 incorrect guesses until you're HANGED.""")

import random, os

file = open("Random_Words.rtf").read().splitlines()     #file found via Google

#Pick a word and turn it into a list, get rid of the comma
word = random.choice(file)
word = word.lower()
word = list(word)
word.pop(-1)

#Simplify word by eliminating contractions
for nonletter in word:
        if nonletter not in 'abcdefghijklmnopqrstuvwxyz':
            word.remove(nonletter)

wordlength = len(word)

yourlength = ("""

Your word is {} letters long. Type a letter for your first guess.
    """)
print(yourlength.format(wordlength))

#Print the template of the word
for i in word:
    print('_ ', end='')

print('\n')

print(os.getcwd())

hangman = ["""
                                            Beware the noose




                                                ____
                                                        """,
        """
                                              But really                               

                                               |
                                               |
                                               |
                                               |
                                               |
                                               |____
                                                        """,
        """
                                              It's a comin
                                                ____
                                               |
                                               |
                                               |
                                               |
                                               |
                                               |____
                                                       """,
        """
                                               No lie
                                                ____
                                               |    |
                                               |
                                               |
                                               |
                                               |
                                               |____
                                                       """,
        """
                                               ...yikes
                                                ____
                                               |    |
                                               |    O
                                               |
                                               |
                                               |
                                               |____
                                                       """,
        """
                                         You're looking thin
                                                ____
                                               |    |
                                               |    O
                                               |    |
                                               |
                                               |
                                               |____
                                                       """,
        """
                                              Hi there
                                                ____
                                               |    |
                                               |    O
                                               |   \|
                                               |
                                               |
                                               |____
                                                       """,
        """
                                     Blink twice if you need help
                                                ____
                                               |    |
                                               |    O
                                               |   \|/
                                               |
                                               |
                                               |____
                                                       """,
        """
                                          It's make or break
                                                ____
                                               |    |
                                               |    O
                                               |   \|/
                                               |   /
                                               |
                                               |____
                                                       """,
        """
                                                 RIP
                                                ____
                                               |    |
                                               |    O
                                               |   \|/
                                               |   / \\
                                               |
                                               |____
                                                       """,]

guessnumber = 1         #User guess
guessedletters = []     #Storage of all guesses
acceptedletters = ''    #Storage of acceptable guesses (e.g. no symbols)
attempt = 0             #Counter to track hangman output in case of bad guess

#Function to print the word as guessed so far for user
def printingword():
        for letter in word:
                if letter in acceptedletters:
                        print(letter + ' ', end='')
                else:
                        print('_ ', end='')


#Loop to test guesses and accept or reject, and win or lose
while guessnumber < 11:
    userguess = input('')
    userguess = userguess.lower()
    if userguess in 'abcdefghijklmnopqrstuvwxyz':
        if userguess not in guessedletters:
            if userguess in word:
                acceptedletters = acceptedletters + userguess
                print('\n')
                printingword()
                wincheckletters = set(acceptedletters)
                wincheckword = set(word)
                if wincheckletters == wincheckword:
                    print('\n\n\nCongratulations!! You won!')
                    break   
                print("\n\nGood job!")
                guessedletters.append(userguess)
                for value in guessedletters:
                        if value not in 'abcdefghijklmnopqrstuvwxyz':
                            guessedletters.pop(value)
                guessedletterstoshow = set(guessedletters)
                stringguessedletterstoshow = ' '.join(guessedletterstoshow)
                print("\nLetters you've guessed: ", stringguessedletterstoshow)
                print("Guess again: ", end='')
                continue
            else:
                print("\nSorry, that letter's not in the word.", end='')
                print('\n')
                printingword()
                print('\n')
                print(hangman[attempt])
                attempt += 1
        else:
            print("\nSorry, you already guessed that letter.", end='')
            print('\n')
            printingword()
            print('\n')
            print(hangman[attempt])
            attempt += 1
    else:
        print("\nMust enter a single letter only.", end='')
        print('\n')
        printingword()
        print('\n')
        print(hangman[attempt])
        attempt += 1
    guessedletters.append(userguess)
    guessnumber += 1
    for value in guessedletters:
        if value not in 'abcdefghijklmnopqrstuvwxyz':
            guessedletters.remove(value)
    guessedletterstoshow = set(guessedletters)
    stringguessedletterstoshow = ' '.join(guessedletterstoshow)
    if guessnumber == 11:
        print("\nYou're hanged! Sorry, you lost.")
        originalword = ''.join(word)
        print("\nThe word was:", originalword)
        break
    else:
        print("Letters you've guessed: ", stringguessedletterstoshow)
        print("Incorrect guess number: ", guessnumber)
        print("Guess again: ", end='')
