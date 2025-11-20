#!/usr/bin/env python3
# Created by: Patrick
# Created on: 10/18/2025
# This program is a number guessing game using a loop using a break statement

import random


def main():
    # Generate a random number between 0 and 9
    random_number = random.randint(0, 9)

    while True:
        try:
            # Ask user for a number between 0 and 9
            user_guess = int(input("Guess a number between 0 and 9: "))

            # Check if the guess is correct
            if user_guess == random_number:
                print("Congratulations! You guessed the correct number.")
                break
            else:
                print("Incorrect guess. Try again.")

        # If the input is not an integer
        except ValueError:
            print("Please enter a valid integer between 0 and 9.")


if __name__ == "__main__":
    main()
