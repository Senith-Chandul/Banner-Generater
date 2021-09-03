import os
from art import *
import sys
from time import sleep
from termcolor import colored

COLORS = {
    "black": "\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34;1m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "Bright Red": "\u001b[31;1m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m",
}
# You can add more colors and backgrounds to the dictionary if you like.


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text


def Anime(a):
    for char in a:
        sleep(0.005)
        print(char, end='')
        sys.stdout.flush()


def AnimeText(a):
    for char in a:
        sleep(0.05)
        print(char, end='')
        sys.stdout.flush()


os.system('clear')
Banner = '''
             [[red]] ___    [[blue]]            [[green]]        [[yellow]]
             [[red]]| _ ) __ [[blue]]_  _ _   [[green]]_ _   __[[yellow]]_  _ _
             [[red]]| _ \/ _[[blue]]` || ' \ [[green]]| ' \ / [[yellow]]-_)| '_|
             [[red]]|___/\_[[blue]]_,_||_||[[green]]_||_||_|\_[[yellow]]__||_|
    [[red]]   ___         [[blue]]         [[green]]          [[yellow]] _          [[magenta]]
    [[red]]  / __| ___ [[blue]] _ _   ___[[green]]  _ _  __ _[[yellow]] | |_  ___ [[magenta]] _ _
    [[red]] | (_ |/ -[[blue]]_)| ' \ / [[green]]-_)| '_|/ _[[yellow]]` ||  _|/ [[magenta]]-_)| '_|
    [[red]]  \___|\_[[blue]]__||_||_|\[[green]]___||_|  \_[[yellow]]_,_| \__|\[[magenta]]___||_|

'''

Author = '''                [[red]]   By :[[green]] Senith[[blue]] Chandul


'''


Anime(colorText(Banner))
AnimeText(colorText(Author))


def Art(a):
    ArtText = text2art(a, 'rnd-medium')
    Anime(colored(ArtText, 'yellow'))


while True:
    AnimeText(colorText('''[[blue]]Enter your Banner's text. [[red]] Enter 'exit' to exit..
'''))
    text = input(colorText('''[[green]]Enter your text : >> '''))
    if(text == 'exit'):
        break
    else:
        Art(text)
        AnimeText(colorText('''[[yellow]]Not Interested.. Regenerate...
'''))
        AnimeText(colorText('''[[blue]]Leave empty or enter 'y' to regenerate. [[red]] Enter 'n' to stop.
'''))
        while True:
            Regenerate = input(
                colorText("[[green]]Enter your choice : >> "))
            if (Regenerate == 'n' or Regenerate == 'N'):
                break
            elif (Regenerate == '' or Regenerate == 'y' or Regenerate == 'Y'):
                Art(text)
            else:
                print("Wrong Choice...")
                break
