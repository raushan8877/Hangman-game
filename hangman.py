import random

# ====== HANGMAN LOGO ======
logo = """
 _                                            
| |                                           
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __ 
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""
print(logo)

# ====== HANGMAN STAGES ======
stages = [
    """
       _______
      |/      |
      |      ( )
      |      /|\\
      |       |
      |      / \\
      |
    __|___
    """,
    """
       _______
      |/      |
      |      ( )
      |      /|\\
      |       |
      |      / 
      |
    __|___
    """,
    """
       _______
      |/      |
      |      ( )
      |      /|\\
      |       |
      |      
      |
    __|___
    """,
    """
       _______
      |/      |
      |      ( )
      |      /|
      |       |
      |      
      |
    __|___
    """,
    """
       _______
      |/      |
      |      ( )
      |       |
      |       |
      |      
      |
    __|___
    """,
    """
       _______
      |/      |
      |      ( )
      |      
      |      
      |      
      |
    __|___
    """,
    """
       _______
      |/      |
      |      
      |      
      |      
      |      
      |
    __|___
    """
]

# ====== WORD LIST ======
word_list = [
    'python', 'hangman', 'developer', 'programming',
    'machine', 'learning', 'data', 'science', 'computer', 'artificial'
]

# ====== GAME START ======
lives = 6
chosen_word = random.choice(word_list)
print(f"(Hint) The word is: {chosen_word}\n")

placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
corrected_letters = []
display = placeholder

# ====== MAIN GAME LOOP ======
while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in corrected_letters:
        print(f"You already guessed '{guess}'. Try again.")
        continue

    display = ''
    for letter in chosen_word:
        if letter == guess:
            display += letter
            corrected_letters.append(guess)
        elif letter in corrected_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that is not in the word. You lose a life.")
        print(stages[lives])
        if lives == 0:
            game_over = True
            print("You lose! The word was:", chosen_word)

    if "_" not in display:
        game_over = True
        print("Booyah.. You win!")
        print(stages[lives])  
