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
   |  |                ===============================                    |  |
   |  |                | |                         | |                    |  |
   |  |                | |   G A M E   R U L E S   | |                    |  |
   |  |                | |                         | |                    |  |
   |  |                ===============================                    |  |
   |  |  1 - Its a simple maths challenge game.                           |  |
   |  |  2 - Randomly generate 10 math questions, each involving          |  |
   |  |      multiplication, addition, or subtraction, with numbers       |  |
   |  |      ranging between 3 and 15. Here's an example of how to        |  |
   |  |      generate questions:                                          |  |
   |  |         Question 1: 6 * 9                                         |  |
   |  |         Question 2: 11 + 4                                        |  |
   |  |         Question 3: 8 - 15                                        |  |
   |  |         ...and so on.                                             |  |
   |  |  3 - Players must solve each math question as quickly as          |  |
   |  |      possible. There is no specific time limit for individual     |  |
   |  |      questions. Only 3 chance for each question, after that it    |  |
   |  |      jump to the next question. Each correct answer has 10 score  |  |
   |  |      and wrong one has -2. Points will calculate by dividing      |  |
   |  |      score by total time.                                         |  |
   |  |  4 - The top 15 best points will be saved on a scoreboard.        |  |
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
