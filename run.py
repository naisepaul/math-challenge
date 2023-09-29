import random  # making random choice
import sys  # typewriter effect using sys module
import time  # time


def typewriter_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write('\n')  # Add a newline character at the end


welcome_text = "*" * 30 + "\n WELCOME TO MATH CHALLENGE \n\n" + "*" * 30
typewriter_effect(welcome_text)
