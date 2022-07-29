import random
import os

from Word_list import word_list
chosen_word = random.choice(word_list)


from stages import Stages,logo

print(logo)


stages = []
display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)
print("\n")


lives = 6


end = False


while not end:
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    if guess in display:
        print(f"you have already entered the {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if guess not in chosen_word:
        print("You guessed the wrong word, you  lost a life")
        lives -= 1
        if lives == 0:
            end = True
            print("you have lost")
            print(f"The answer is {chosen_word}")


    if "_" not in display:  
        end = True
        print("You won the game")
    
    print(Stages[lives])