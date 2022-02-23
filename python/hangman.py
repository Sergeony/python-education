import os.path
import sys
import random

def main():
    """Show main menu with commands to action."""

    os.system("clear")

    print("To view past games press 0\n"
          "To start game press      1\n"
          "To exit press            2:"
          )

    command_number = int(input("Enter a number from 0 to 2:"))

    #Validation of input
    while command_number not in (0, 1, 2):
        print("Enter correct number, please")
        command_number = int(input("Enter a number from 0 to 2:"))

    command_list = [view_past_games, start_game, exit]

    command_list[command_number]()


def view_past_games():
    """Show a log of words from past games."""

    os.system("clear")

    if os.path.exists('words.log') and os.path.getsize("words.log") > 0:
        with open("words.log", 'r') as words:
            for word in words.read().splitlines():
                print(word)
    else:
        print("Nothing to see here yet")

    back_to_menu()


def exit():
    """Close game."""

    sys.exit()


def back_to_menu():
    """Offer to return to the menu."""
    
    input("To return to the menu, enter any button: ")
    main()


def start_game():
    
    os.system("clear")

    #Initialisation
    picture = [
        r"  ___   ",
        r" /   |  ",
        r" |      ",
        r" |      ",
        r" |      ",
        r"_|___   ",
        ]
    word = generate_word()
    guessed_letters = []
    missed_letters = []
    misses = 0

    #Game loop
    while True:
        os.system("clear")
        show_picture(picture)
        show_word(guessed_letters, word)
        show_missed_letters(missed_letters)

        #Exit the loop when all letters are guessed
        if len(set(word)) == len(guessed_letters) or misses == 6:
            break

        letter = input("Enter letter: ")
      
        if letter in word:
            guessed_letters.append(letter)
        else:
            missed_letters.append(letter)
            misses += 1
            update_picture(misses, picture)
    
    show_game_over(misses)


def generate_word():
    """Return a randomly selected word from a file and log it."""

    words = open("word_base.txt", "r")    
    word = random.choice(words.read().splitlines())
    words.close()

    with open("words.log", "a") as used_words:
        used_words.write(word + "\n")

    return word


def update_picture(misses, picture):
    """Change picture list but DON'T SHOW it."""

    if misses == 1:
        picture[2] = r" |   o  "

    if misses == 2:
        picture[3] = r" |   |  "
    if misses == 3:
        picture[3] = r" |  /|  "
    if misses == 4:
        picture[3] = r" |  /|\ "

    if misses == 5:
        picture[4] = r" |  /   "
    if misses == 6:
        picture[4] = r" |  / \ "


def show_picture(picture):
    """Output picture by lines."""

    for line in picture:
        print(line)


def show_word(guessed_letters, word):
    """Output the letters in the word if they are guessed, and "-" if not."""

    print("Guessed: ", end="")
    for letter in word:
        print(letter.upper(), end="") if letter in guessed_letters else print("-", end="")  
    print()


def show_missed_letters(missed_letters):
    """Output the entered letters that are not in the word."""

    print("Misses: ", end="")
    for letter in missed_letters:
        print(letter.upper(), end=", ")
    print()


def show_game_over(misses):
    """Output a message with the result of the game."""

    if misses < 6:
        print("Winner winner chicken dinner!")
    else:
        print("Better luck next time!")

    back_to_menu()


if __name__ == "__main__":
    main()