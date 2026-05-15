# CSCI110 Final Project
# Program: Number Quest
# Programmer: Gabe Reek
# Description: A simple number guessing game with a menu, file I/O, and testable functions.

import random

SCORE_FILE = "number_quest_score.txt"


def read_high_score(filename):
    try:
        score_file = open(filename, "r")
        score = score_file.read()
        score_file.close()

        if score == "":
            return 0
        else:
            return int(score)

    except:
        return 0


def save_high_score(filename, score):
    score_file = open(filename, "w")
    score_file.write(str(score))
    score_file.close()


def get_hint(secret_number, guess):
    if guess < secret_number:
        return "Too low."
    elif guess > secret_number:
        return "Too high."
    else:
        return "Correct!"


def calculate_score(number_of_guesses):
    score = 110 - number_of_guesses * 10

    if score < 10:
        score = 10

    return score


def is_valid_guess(text, lowest_number, highest_number):
    try:
        guess = int(text)

        if guess >= lowest_number and guess <= highest_number:
            return True
        else:
            return False

    except:
        return False


def show_menu():
    print()
    print("Number Quest")
    print("1. Play game")
    print("2. View high score")
    print("3. Quit")


def play_game():
    lowest_number = 1
    highest_number = 20
    secret_number = random.randint(lowest_number, highest_number)
    number_of_guesses = 0
    game_over = False

    print()
    print("I am thinking of a number from 1 to 20.")
    print("Try to guess it!")

    while game_over == False:
        guess_text = input("Enter your guess: ")

        if is_valid_guess(guess_text, lowest_number, highest_number):
            guess = int(guess_text)
            number_of_guesses = number_of_guesses + 1

            hint = get_hint(secret_number, guess)
            print(hint)

            if guess == secret_number:
                score = calculate_score(number_of_guesses)
                high_score = read_high_score(SCORE_FILE)

                print("You guessed it in", number_of_guesses, "tries.")
                print("Your score is", score)

                if score > high_score:
                    print("New high score!")
                    save_high_score(SCORE_FILE, score)

                game_over = True

        else:
            print("Please enter a whole number from 1 to 20.")


def view_high_score():
    high_score = read_high_score(SCORE_FILE)
    print()
    print("The current high score is", high_score)


def main():
    keep_playing = True

    while keep_playing == True:
        show_menu()
        choice = input("Choose 1, 2, or 3: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            view_high_score()
        elif choice == "3":
            print("Thanks for playing Number Quest!")
            keep_playing = False
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
