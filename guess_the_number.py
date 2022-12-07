#!/usr/bin/env python

import random

from colorama import Fore

TOTAL_NUMBER = 4
GUESS_TIMES = 10

answer = ""
for i in random.sample([i for i in range(10)], TOTAL_NUMBER):
    answer += str(i)


def check_guess_number(answer, guess_number):
    a = 0
    b = 0
    for i in range(TOTAL_NUMBER):
        if list(answer)[i] == list(guess_number)[i]:
            a += 1
        elif list(answer)[i] in list(guess_number):
            b += 1
    return a, b


def show_history(history):
    for index, h in enumerate(history):
        print(Fore.RED + f"{index + 1}st " + h)


def run_game():
    print(
        f"Please input {TOTAL_NUMBER} numbers. In result, A indicates a correct value and position, B indicates a "
        f"correct value but an incorrect position.")
    history = []
    guess_times = 0
    while guess_times <= GUESS_TIMES:
        guess_number = input(Fore.GREEN + "Please input your guess number: ")
        result = check_guess_number(answer, guess_number)
        if result == (TOTAL_NUMBER, 0):
            print(Fore.GREEN + "Correct!")
            break
        else:
            history.append(f"input number:{guess_number} result:{result[0]}A{result[1]}B")
            show_history(history)
        guess_times += 1
        print(Fore.BLUE + f"You have {GUESS_TIMES - guess_times} chance left.")


if __name__ == "__main__":
    run_game()
