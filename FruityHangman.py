import random
from nltk.corpus import wordnet 
import time

# A drawing of hangman depenednt on number of guesses
def draw_hangman(num_guesses):
    if num_guesses == 0:
        print(" _________     ")
        print("|         |    ")
        print("|              ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif num_guesses == 1:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|              ")
        print("|              ")
        print("|              ")
    elif num_guesses == 2:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|         |    ")
        print("|              ")
        print("|              ")
    elif num_guesses == 3:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|    ")
        print("|              ")
        print("|              ")
    elif num_guesses == 4:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\   ")
        print("|              ")
        print("|              ")
    elif num_guesses == 5:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\   ")
        print("|        /     ")
        print("|              ")
    else:
        print(" _________     ")
        print("|         |    ")
        print("|         0    ")
        print("|        /|\   ")
        print("|        / \   ")
        print("|              ")

# Define the list of valid words
words = ['Abiu'
    ,'Acai'
    ,'Acerola'
    ,'Akebi'
    ,'Ackee'
    ,'Mayapple'
    ,'Apple'
    ,'Apricot'
    ,'Araza'
    ,'Avocado'
    ,'Banana'
    ,'Bilberry'
    ,'Blackberry'
    ,'Blackcurrant'
    ,'Blueberry'
    ,'Boysenberry'
    ,'Breadfruit'
    ,'Canistel'
    ,'Cempedak'
    ,'Cherimoya'
    ,'Cherry'
    ,'Chico'
    ,'Cloudberry'
    ,'Coconut'
    ,'Cranberry'
    ,'Currant'
    ,'Damson'
    ,'Date'
    ,'Dragonfruit'
    ,'Durian'
    ,'Elderberry'
    ,'Feijoa'
    ,'Fig'
    ,'Gooseberry'
    ,'Grape'
    ,'Raisin'
    ,'Grapefruit'
    ,'Guava'
    ,'Hala'
    ,'Honeyberry'
    ,'Huckleberry'
    ,'Jabuticaba'
    ,'Jackfruit'
    ,'Jambul'
    ,'Jostaberry'
    ,'Jujube'
    ,'Juniper'
    ,'Kiwano'
    ,'Kiwifruit'
    ,'Kumquat'
    ,'Lemon'
    ,'Lime'
    ,'Loganberry'
    ,'Longan'
    ,'Loquat'
    ,'Lulo'
    ,'Lychee'
    ,'Mango'
    ,'Mangosteen'
    ,'Marionberry'
    ,'Melon'
    ,'Cantaloupe'
    ,'Galia'
    ,'Honeydew'
    ,'Watermelon'
    ,'Momordica' 
    ,'Mulberry'
    ,'Nance'
    ,'Nectarine'
    ,'Orange'
    ,'Clementine'
    ,'Mandarine'
    ,'Tangerine'
    ,'Papaya'
    ,'Passionfruit'
    ,'Pawpaw'
    ,'Peach'
    ,'Pear'
    ,'Persimmon'
    ,'Plantain'
    ,'Plum'
    ,'Prune'
    ,'Pineapple'
    ,'Pineberry'
    ,'Plumcot'
    ,'Pomegranate'
    ,'Pomelo'
    ,'Mangosteen'
    ,'Quince'
    ,'Raspberry'
    ,'Salmonberry'
    ,'Rambutan'
    ,'Redcurrant'
    ,'Salal'
    ,'Salak'
    ,'Sapodilla'
    ,'Sapote'
    ,'Satsuma'
    ,'Soursop'
    ,'Strawberry'
    ,'Tamarillo'
    ,'Tamarind'
    ,'Tangelo'
    ,'Tayberry'
    ,'Ugli'
    ,'Whitecurrant'
    ,'Sapote'
    ,'Ximenia'
    ,'Yuzu'
    ,'Cucumber'
    ,'Eggplant'
    ,'Jalapeno'
    ,'Olive'
    ,'Pea'
    ,'Pumpkin'
    ,'Squash'
    ,'Tomato'
    ,'Zucchini']


# choose a random word from the list
word = random.choice(words).lower()

# create a list to store the letters guessed by the user
guesses = []
total_guesses = []

# create a variable to store the number of attempts left
attempts_left = 6

count = 0

syns = wordnet.synsets(word)
definition = str(syns[0].definition())

print('''==============================
== Welcome to FruityHangman ==
==============================''')

intro = 'Here is your first word:\n\n'
for char in intro:
    print(char, end='')
    time.sleep(.1)

# loop until the player wins or loses
while True:
    # display the current status of the word with underscores for unguessed letters
    display_word = ''
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += '_'
    print(display_word)

    # check if the player has guessed all the letters
    if set(word) == set(guesses):
        print(f'''\nCongratulations, you won!
{word.capitalize()}: {definition.capitalize()}\n''')
             
        apple = '  ,--./,-.   \n / #      \  \n|          | \n \        /  \n  `._,._,\'   '

        for char in apple:
            print(char, end='')
            time.sleep(.1)
                   
        break

    # check if the player has run out of attempts
    if attempts_left == 0:
        result = f'''\nSorry, you lost. The word was: {word.capitalize()}
{definition.capitalize()}.\n'''
        print(result)
        break

    # prompt the player to guess a letter
    guess = input('\nGuess a letter: ').lower()

    # check if the player has already guessed this letter
    if guess in total_guesses:
        print('\nYou already guessed that letter!')
    # check if the letter is in the word
    elif guess in word:
        print('\nCorrect!')
        guesses.append(guess)
        total_guesses.append(guess)
    # if the letter is not in the word
    else:
        total_guesses.append(guess)
        count += 1
        print('\nIncorrect :(')
        attempts_left -= 1
        draw_hangman(count)

    # display the number of attempts left
    print('\nAttempts left:', attempts_left)