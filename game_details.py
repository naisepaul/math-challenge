import colorama  # for color
from colorama import Fore, Back, Style
"""
color, background color, style
https://www.youtube.com/watch?v=u51Zjlnui4Y
"""
colorama.init(autoreset=True)  # for auto reset color

game_details = [
   # game rules
   """
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
   """,

   # heading

   """
                ╔╦╗┌─┐┌┬┐┬ ┬  ╔═╗┬ ┬┌─┐┬  ┬  ┌─┐┌┐┌┌─┐┌─┐
                ║║║├─┤ │ ├─┤  ║  ├─┤├─┤│  │  ├┤ ││││ ┬├┤
                ╩ ╩┴ ┴ ┴ ┴ ┴  ╚═╝┴ ┴┴ ┴┴─┘┴─┘└─┘┘└┘└─┘└─┘

   """
]