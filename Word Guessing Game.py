import random

name = input("Enter your name: ")
print("Good luck!", name)

words = []
# Here we are taking the list of words from the user itself to play the game
no = int(input("Enter the number of words: "))
for i in range(no):
    word = input("Enter the word: ")
    words.append(word)

# Here the system or program chooses a random word from the list
cho = random.choice(words)

guesses = ''
turns = 12

while turns > 0:
    failed = 0

    for char in cho:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\nYou win!!")
        print("The word is:", cho)
        break

    print()
    guess = input("Enter the guessed character: ")

    guesses += guess

    if guess not in cho:
        turns -= 1
        print("Wrong")
        print("You have", turns, "turns left")

        if turns == 0:
            print("You lose")
