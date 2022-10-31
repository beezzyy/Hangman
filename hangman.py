import random
import hangman_art
import hangman_words
import os

stages = hangman_art.stages
logo = hangman_art.logo

print(logo)

word_list = hangman_words.word_list
display = []
lives = 6

chosen_word = random.choice(word_list)

for x in range(len(chosen_word)):
    display.append("_")

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    if guess in display:
        print(f"You've already guessed {guess}")

    count = 0
    for letter in chosen_word:
        if guess == letter:
            display[count] = guess
            count += 1
        else:
            count += 1

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
    print(f"{' '.join(display)}")

    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("YOU WIN!")

if lives == 0:
    print("YOU LOST")
    print(f"The word was: {chosen_word}")
k = input("press enter to exit")
