import random
import math

print("Lets play a game !")
lower_bound = int(input("Enter the lower bound of the range : "))
upper_bound = int(input("Enter the upper bound of the range : "))

no = random.randint(lower_bound, upper_bound)
print("You have only",round(math.log(upper_bound-lower_bound+1,2)),"chances to guess the correct answer")

count = 0

while (count< math.log(upper_bound-lower_bound+1,2)) :
    count +=1

    guess = int(input("Enter the guess : "))
    
    if guess == no :
        print("You guessed the correct number ")
        break

    elif guess < no :
        print("You guessed too small ")

    elif guess > no :
        print("You guessed too high ")


if count >= math.log(upper_bound-lower_bound+1,2):
    print(f"The corect answer was {no} ")
    print("Better luck next time ! ")

