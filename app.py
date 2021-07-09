import random

# keep track of words already used before, so that they user doesn't get the same word again
used_words = []


# Generate a random word at the start of each game
# I created a function for it just for the sake of readability
def randomize():
    return random.choice(open("data.txt").read().splitlines())


def hangman():
    print('''
    Welcome to Hangman
    You have 7 attempts until your defeat is declared
    You cannot guess a letter more than once''')

    # word which the user has to guess
    word = randomize()

    # check if the randomised word was already used in a previous game
    if word in used_words:
        word = randomize()

    # keeps track of the letters guessed by the user to display on the screen
    tracker = list(map(lambda x: '_', word))

    # keep track of guessed letters - using a set so that there won't be duplicates
    guesses = set()

    game_running = True
    attempts = 7

    while game_running:
        print(f'\nLives: {attempts}')
        prompt = input('Guess a letter:  ').lower()

        if prompt in word and prompt not in guesses:
            guesses.add(prompt)
            for idx, letter in enumerate(word):
                if letter == prompt:
                    tracker[idx] = letter
            print(' '.join(tracker))
            print(f'Your guesses: {guesses}')

        elif len(prompt) > 1 or not prompt or not prompt.isalpha():
            print('Invalid entry')

        elif prompt not in guesses:
            attempts -= 1
            guesses.add(prompt)
            print(' '.join(tracker))
            print(f'Your guesses: {guesses}')

        else:
            print(f'You\'ve already guessed \'{prompt}\'')

        # declares win or defeat
        if attempts == 0:
            print(f'\nYou lose!\n'
                  f'The word was: {word}')
            break
        elif ''.join(tracker) == word:
            print('\nCongrats! You have won!\n'
                  f'The word was indeed \'{word}\'')
            break

    # prompt to play again
    prompt = input('Play again? (Y/N):  ').lower()
    if prompt == 'y':
        hangman()
    else:
        print('Goodbye! :)')


hangman()
