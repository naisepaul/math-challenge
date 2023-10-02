import random  # making random choice
import shutil  # Import the shutil module to get the terminal width
import sys  # typewriter effect using sys module
import time  # time
import colorama  # for color
from colorama import Fore, Back, Style
"""
color, background, style
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
print(f"""
     {Fore.CYAN}{Style.BRIGHT}{Back.MAGENTA}
                        ╔╦╗┌─┐┌┬┐┬ ┬  ╔═╗┬ ┬┌─┐┬  ┬  ┌─┐┌┐┌┌─┐┌─┐
                        ║║║├─┤ │ ├─┤  ║  ├─┤├─┤│  │  ├┤ ││││ ┬├┤ 
                        ╩ ╩┴ ┴ ┴ ┴ ┴  ╚═╝┴ ┴┴ ┴┴─┘┴─┘└─┘┘└┘└─┘└─┘
                        """)

# calling typewriter function to print the welcome message

typewriter_effect(welcome_message, delay=0.02,
                  color=Fore.RED, bg_color=Back.WHITE)

print(f""" {Fore.GREEN}

    _________________________________________________________________________
   |   ___________________________________________________________________   |
   |  |                                                                   |  |
   |  |                ===============================                    |  |
   |  |                | |                         | |                    |  |
   |  |                | |   G A M E   R U L E S   | |                    |  |
   |  |                | |                         | |                    |  |
   |  |                ===============================                    |  |
   |  |                                                                   |  |
   |  |  1 - Its a simple maths challenge game.                           |  |
   |  |                                                                   |  |
   |  |  2 - Randomly generate 10 math questions, each involving          |  |
   |  |      multiplication, addition, or subtraction, with numbers       |  |
   |  |      ranging between 3 and 15. Here's an example of how to        |  |
   |  |      generate questions:                                          |  |
   |  |                                                                   |  |
   |  |         Question 1: Multiply 6 by 9                               |  |
   |  |         Question 2: Add 11 to 4                                   |  |
   |  |         Question 3: Subtract 8 from 15                            |  |
   |  |         ...and so on.                                             |  |
   |  |                                                                   |  |
   |  |  3 - Players must solve each math question as quickly as          |  |
   |  |      possible. There is no specific time limit for individual     |  |
   |  |      questions                                                    |  |
   |  |                                                                   |  |
   |  |  4 - The top 10 fastest times will be saved on a leaderboard.     |  |
   |  |___________________________________________________________________|  |
   |_________________________________________________________________________|
    """)
   

OPERATORS = ["+", "-", "*"]  # operators
"""
OPERATOR_COLORS is a dictionary mapping operators to 
their respective ANSI escape codes for different colors.
"""
OPERATOR_COLORS = {
    "+": "\033[91m",  # ANSI escape code for red color
    "-": "\033[92m",  # ANSI escape code for green color
    "*": "\033[93m"   # ANSI escape code for yellow color
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
    # expr = f"{str(left)} {operator} {str(right)}"
    expr = f"{left} {OPERATOR_COLORS[operator]}{operator} {Fore.MAGENTA}{right}"  # Apply color to the operator
    answer = eval(f"{left} {operator} {right}")
    """
    eval() is a built-in function that is used to evaluate a string
    containing a Python expression or statement as code. It takes a
    single argument, which is a string, and interprets it as a 
    Python expression.
    """
    return expr, answer


for i in range(total_questions):
    expr, answer = generate_questions()
    print(f"{Fore.CYAN}Question #{str(i+1)} : {Fore.MAGENTA}{expr} =  {answer}")
    
