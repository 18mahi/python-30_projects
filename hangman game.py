import random

HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ==='''
]

WORDS = [
    'aesthetic', 'creative', 'exciting', 'beautiful', 'unique',
    'python', 'hangman', 'challenge', 'imagination', 'artistic'
]

def get_random_word(word_list):
    return random.choice(word_list).upper()

def display_board(hangman_pics, missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)])
    print("\nMissed letters:", ' '.join(missed_letters))
    blanks = ['_' if letter not in correct_letters else letter for letter in secret_word]
    print(' '.join(blanks))
    print()

def play_hangman():
    print("🌟 Welcome to the Aesthetic Hangman! 🌟")
    print("Guess the secret word, one letter at a time.")
    print("Each mistake brings the hangman closer to completion. Good luck!\n")

    secret_word = get_random_word(WORDS)
    missed_letters = []
    correct_letters = []
    game_over = False

    while not game_over:
        display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
        guess = input("Enter a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.\n")
            continue
        if guess in missed_letters + correct_letters:
            print("You already guessed that letter. Try again.\n")
            continue

        if guess in secret_word:
            correct_letters.append(guess)
            if all(letter in correct_letters for letter in set(secret_word)):
                display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
                print("🎉 Congratulations! You guessed the word:", secret_word)
                game_over = True
        else:
            missed_letters.append(guess)
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_board(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
                print("💀 Game Over! The word was:", secret_word)
                game_over = True

    print("\nThanks for playing the Aesthetic Hangman! 🌈")

if __name__ == "__main__":
    play_hangman()