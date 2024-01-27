import random

def choose_word():
    words = ['mango', 'apple', 'tomato', 'orange', 'pineapple', 'custardapple', 'banana', 'strawberry']
    return random.choice(words)

def display(word, guessed_letters):
    display_str = ""

    for char in word:
        if char in guessed_letters:
            display_str += char
        else:
            display_str += '_'

    return display_str

def hangman():
    print("Welcome to Hangman!\nGood luck!")

    word = choose_word()
    guessed_letters = []
    failed_attempts = 0
    turns = len(word) + 2

    while failed_attempts < turns:
        print("Current word:", display(word, guessed_letters))
        guess = input("Enter a single character: ")

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already guessed this letter.")
                continue
            elif guess in word:
                print("You guessed the correct letter.")
                turns -= 1
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                failed_attempts += 1
                turns -= 1
                print("Attempts left:", turns)
        else:
            print("Enter a single character.")

        if '_' not in display(word, guessed_letters):
         print("Congratulations! You guessed the word:", word)
        else:
         print("Oops! Turns are over. The word was:", word)

if __name__ == "__main__":
    hangman()
