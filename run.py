import gspread
from google.oauth2.service_account import Credentials
import random  # making random choice
import shutil  # Import the shutil module to get the terminal width
import sys  # typewriter effect using sys module
import time  # time
import os
import datetime
from game_details import *  # import game_details file

import colorama  # for color
from colorama import Fore, Back, Style
"""
color, background color, style
https://www.youtube.com/watch?v=u51Zjlnui4Y
"""
colorama.init(autoreset=True)  # for auto reset color

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('math_challenge')

scoreboard = SHEET.worksheet("scoreboard")

data = scoreboard.get_all_values()

# For typewritter effect


def typewriter_effect(text, delay=0.2, color=Fore.WHITE, bg_color=Back.BLACK):
    """
    Welcome message in typewriter effect
    https://www.youtube.com/watch?v=2h8e0tXHfk
    """

    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')  # Add a newline character at the end


# Get the width of the terminal window
terminal_width, _ = shutil.get_terminal_size()

# Calculate the number of spaces needed to center horizontally
spaces_to_center = (terminal_width - len("WELCOME TO MATH CHALLENGE")) // 2

welcome_message = (' ' * spaces_to_center + "WELCOME TO MATH CHALLENGE\n\n"
                   + ' ' * spaces_to_center + "*" * 25)

# Heading from game_details.py
print(f"{Fore.CYAN}{Style.BRIGHT}{game_details[1]}")

# calling typewriter function to print the welcome message

typewriter_effect(welcome_message, delay=0.03,
                  color=Fore.RED)

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
    """
     define 10 randomly selected questions
    randomly selected left side and right side value
    """
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
        Enter your username (3 to 6 characters) >>> """).strip().upper()

        if len(username) < 3 or ' ' in username or len(username) > 6 or \
           not any(char.isalpha() for char in username):
            """
            Check if the username has less than 3 and not greater than
            6 characters or does not contain any letters or contain space
            """
            print(f"{Fore.RED}\tInvalid username. Please enter at least 3"
                  f" and not greater than 6 characters with at least"
                  f" one letter without space!")

        else:
            os.system('clear')  # clear the screen
            return username


def main():
    """
    Main function take the players username and setting the game enviornment
    Each question in the game, the function manages the presentation of
    the mathematical expression, handles players input, evaluate the answer
    and time taken  for each question.
    Scoring system allowing the player to earn score for each correct answers
    and deducted score for wrong answers and invalid input.
    Each question have 3 attempt for correct answer after that jump to
    next question
    """

    username = get_username()
    score = 0  # initialize the player score to zero
    corrent_answer_score = 10  # correct answer score
    wrong_answer_score = -2  # wrong answer score

    while True:
        # importing game rules from the file game_details
        print(f"\n{Fore.GREEN}{game_details[0]}")
        print(f"\t\t {Fore.YELLOW} Hello, {username},"
              f" Welcome to Math Challenge !")
        input(f"""{Fore.YELLOW}
        {username}, Press ENTER to start the game.\n\t>>>""")
        os.system('clear')  # clear the screen
        # type writer effect for loading the game
        typewriter_effect("\tLoading the game...", delay=0.02,
                          color=Fore.GREEN)
        # type 'exit' to quit the game
        print(f"\n{Fore.YELLOW}\tType{Fore.RED}{Style.BRIGHT} "
              f"'exit'{Style.RESET_ALL}{Fore.YELLOW} for quit the game\n")

        # Record the start time for first question
        ques_start_time = time.time()

        for i in range(total_questions):
            expr, answer = generate_questions()
            # Record the start time of current question
            curr_ques_start_time = time.time()
            wrong_attempt = 0  # counting wrong attempt for current question
            invalid_input_attempt = 0
            # allow 3 attempt for each question
            while wrong_attempt < 3 and invalid_input_attempt < 3:
                guess = input(f"""{Fore.CYAN}
            Question #{str(i+1)} : {expr} = """)

                # answer will be an int. So changing to a string
                if guess == str(answer):
                    current_time = time.time()  # current time
                    curr_ques_end_time = current_time - curr_ques_start_time
                    print(f"""{Fore.GREEN}
            Correct! You took {curr_ques_end_time:.2f} seconds to answer.""")
                    score += corrent_answer_score
                    break

                # if want to exit from the game in between type 'exit'
                elif guess.lower() == 'exit':
                    # type writer effect for exiting the game
                    typewriter_effect("\n\tExiting the game...\n", delay=0.05,
                                      color=Fore.RED)
                    return

                # if guess is non integer error message
                try:
                    guess = int(guess)
                except ValueError:
                    print(f"{Fore.RED}\n\t Invalid input. Please"
                          f" enter an integer.")
                    invalid_input_attempt += 1
                    score += wrong_answer_score
                else:
                    score += wrong_answer_score
                    print(f"{Fore.RED}\n\t Wrong Answer")
                    wrong_attempt += 1
            # Pause before the next question
            time.sleep(.5)
        ques_end_time = time.time()  # total question end time
        total_time = ques_end_time - ques_start_time  # Calculate elapsed time
        points = score / total_time  # calculating points to get best player
        print("\n\tGame Over!")
        typewriter_effect(f"\tYou answered in {total_time:.2f} Seconds\n"
                          f"\tYour score is {score}\n"
                          f"\tYour points is {points:.2f}\n",
                          delay=0.02, color=Fore.YELLOW)
        scoreboard_data(username, score, total_time, points)

        # offer choice to the player
        print(f"\n\t{Fore.BLUE}What would you like to do next ?\n")
        print(f"\t1. Play Again\n"
              f"\t2. Scoreboard\n"
              f"\t3. Exit\n"
              f"\t4. FeedBack\n")

        # Reset the score for the next game
        score = 0

        while True:
            choice = input(f"\tEnter Your choice (1/2/3/4)"
                           f" {Fore.RED} >>>{Style.RESET_ALL} ")

            if choice == '1':
                typewriter_effect("\tLoading the game...", delay=0.02,
                                  color=Fore.GREEN)
                break  # Break the inner loop and go back to the main loop
            elif choice == '2':
                os.system('clear')  # clear the screen
                display_top_15_best_player()  # scoreboard
                continue  # continue to the choices
            elif choice == '3':
                print(f"{Fore.RED}\n\tExiting the game...")
                print(f"""{Fore.CYAN}
                \n\tThanks for playing, {username}.
                \n\tSee you again!\n""")
                return  # Exit the game
            elif choice == '4':
                input(f"\n\tEnter your valuable Feedback"
                      f"{Fore.RED} >>>{Style.RESET_ALL} ")
                print(f"""{Fore.CYAN}\n\tThank you for the feedback {username}
                       \n\tSee you again!\n""")
                return   # Exit the game
            else:
                print(f"""{Fore.RED}\n
                That is not a valid choice. Please try again.\n""")
                continue  # continue to the choices


def scoreboard_data(username, score, total_time, points):
    """
    scoreboard saves the details of username, total_time, score and date.
    """
    # get todays date
    date = datetime.date.today()
    current_date = date.strftime("%d/%m/%Y")

    print(f"\t{Fore.GREEN}Updating scoreboard...\n")
    scoreboard_to_update = SHEET.worksheet("scoreboard")
    scoreboard_to_update.append_row([
        str(username), str(current_date), f"{score}",
        f"{total_time:.2f} Seconds", f"{points:.2f}"])
    print(f"\t{Fore.GREEN}scoreboard Update successful..\n")


def display_top_15_best_player():
    # Display top 15 best times

    scoreboard_worksheet = SHEET.worksheet('scoreboard').get_all_values()[1:]

    scoreboard_worksheet.sort(key=lambda x: x[4], reverse=True)
    print(f"{Fore.RED}\tUsername\tDate\t\tScore\tBest Time\tPoints")
    print(f"""{Fore.YELLOW}
       ===============================================================\n""")
    for index, row in enumerate(scoreboard_worksheet[:15], start=1):
        username, date, score, total_time, points = row
        print(f"{Fore.BLUE}{index}.\t {username}\t\t{date}\t{score}"
              f"\t{total_time}\t{points}")
    print(f"""{Fore.YELLOW}
       ===============================================================\n""")


if __name__ == "__main__":
    main()
