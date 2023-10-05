import random  # making random choice
import shutil  # Import the shutil module to get the terminal width
import sys  # typewriter effect using sys module
import time  # time
import datetime
from game_details import *  # import game_details file

import colorama  # for color
from colorama import Fore, Back, Style
"""
color, background color, style
https://www.youtube.com/watch?v=u51Zjlnui4Y
"""
colorama.init(autoreset=True)  # for auto reset color

# For typewritter effect


def typewriter_effect(text, delay=0.2, color=Fore.WHITE, bg_color=Back.BLACK):
    """
    Welcome message in typewriter effect
    https://www.youtube.com/watch?v=2h8e0tXHfk
    """

    for char in text:
        sys.stdout.write(bg_color + color + char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')  # Add a newline character at the end


# Get the width of the terminal window
terminal_width, _ = shutil.get_terminal_size()

# Calculate the number of spaces needed to center horizontally
spaces_to_center = (terminal_width - len("WELCOME TO MATH CHALLENGE")) // 2

welcome_message = (' ' * spaces_to_center + "WELCOME TO MATH CHALLENGE\n\n"
                   + ' '*spaces_to_center + "*" * 25)

# Heading
print(f"{Fore.CYAN}{Style.BRIGHT} {Back.MAGENTA}{game_details[1]}")

# calling typewriter function to print the welcome message

typewriter_effect(welcome_message, delay=0.02,
                  color=Fore.RED, bg_color=Back.WHITE)


OPERATORS = ["+", "-", "*"]  # operators
"""
OPERATOR_COLORS is a dictionary mapping operators to
different colors.
"""
OPERATOR_COLORS = {
    "+": Fore.RED,   # for red color
    "-": Fore.GREEN,  # for green color
    "*": Fore.YELLOW   # for yellow color
}

min_value = 3  # minimum value
max_value = 15  # maximum value
total_questions = 10  # total questions to be answered


def generate_questions():
    # define 10 randomly selected questions
    # randomly selected left side and right side value
    left = random.randint(min_value, max_value)
    right = random.randint(min_value, max_value)
    operator = random.choice(OPERATORS)  # randomly selected operators
    # Apply color to the operator, right and left values
    expr = (
        f"{Fore.MAGENTA}{str(left)} "
        f"{OPERATOR_COLORS[operator]}{operator} "
        f"{Fore.MAGENTA}{str(right)}"
    )

    answer = eval(f"{str(left)} {operator} {str(right)}")
    """
    eval() is a built-in function that is used to evaluate a string
    containing a Python expression or statement as code. It takes a
    single argument, which is a string, and interprets it as a
    Python expression.
    """
    return expr, answer


def get_username():
    # getting username and check it has the correct format
    while True:

        username = input(f"""\n{Fore.YELLOW}
        Enter your username : \n        >>>""").strip().upper()

        if len(username) < 3 or ' ' in username or \
           not any(char.isalpha() for char in username):
            """
            Check if the username has less than 3 characters
            or does not contain any letters or contain space
            """
            print(f"""{Fore.RED}\tInvalid username. Please enter at least 3 
            characters with at least one letter without space!""")

        else:
            print(f"\tHello, {username}, Welcome to Math Challenge !\n")
            return username


def main():
    username = get_username()
    print(f"{Fore.GREEN}{game_details[0]}")
    input(f"""\n{Fore.YELLOW}
    {username}, Press ENTER to start the game.\n    >>>""")
    # Record the start time for first question
    ques_start_time = time.time()

    for i in range(total_questions):
        expr, answer = generate_questions()
        # Record the start time of current question
        curr_ques_start_time = time.time()

        while True:
            guess = input(f"""{Fore.CYAN}
         Question #{str(i+1)} : {expr} = """)
            # if want to exit from in between type exit
            if guess.lower() == 'exit':
                print(f"{Fore.RED}\t Exiting the game...")
                return

            #if guess is non integer error message
            try:
                guess = int(guess)
            except ValueError:
                print(f"{Fore.RED}\t Invalid input. Please enter an integer.")
                continue

            # answer will be an int. So changing to a string
            if guess == str(answer):
                current_time = time.time()  # current time
                curr_ques_end_time = current_time - curr_ques_start_time
                print(f"""{Fore.GREEN}
         Correct! You took {curr_ques_end_time:.2f} seconds to answer.""")
                break
            else:
                print(f"{Fore.RED}\n\t Wrong Answer")
        # Pause before the next question
        time.sleep(.5)

    ques_end_time = time.time()  # total question end time
    total_time = ques_end_time - ques_start_time  # Calculate elapsed time
    print("\n\tGame Over!")
    print(f"\tYou answered in {total_time:.2f} Seconds.")
    play_again = input("Do you want to play again? (yes/no): ")
    if (play_again.lower()) != 'yes':
        print("Thank you for playing Math Challenge!")


if __name__ == "__main__":
    main()
