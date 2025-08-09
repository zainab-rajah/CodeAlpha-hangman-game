import random
import hangman_stages

word_list = ["apple", "beautiful", "potato", "orange", "pear"]
SELECTED_word = random.choice(word_list)
print(SELECTED_word)
lives = 6
display = []
for i in range(len(SELECTED_word)):  #chosen letter is beautiful
    display += '_'
print(display)
game_over = False
while not game_over:
    assumed_letter = input("guess a letter:").lower()
    for position in range(len(SELECTED_word)):
        letter = SELECTED_word[position]
        if letter == assumed_letter:
          display[position]= assumed_letter
    print(display)
    if assumed_letter not in SELECTED_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you lose")
    if '_' not in display:
        game_over=True
        print("you won!!")
    print(hangman_stages.stages[lives])


