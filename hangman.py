import random

word_list = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward']
game_is_finished = False
lives = 5

#Choose a random word from list of words
chosen_word = random.choice(word_list)
print(chosen_word)
# Lenght of word
word_length = len(chosen_word)

display = []

# Show underlines based on lenght of word
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
        print(f"Your lives: {lives}")

    if not "_" in display:
        game_is_finished = True
        print("You win.")
