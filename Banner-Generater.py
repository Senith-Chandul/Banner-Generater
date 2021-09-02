import os
from art import *
import sys
from time import sleep

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

Banner = f'''

   [[red]]  ## ###
   [[red]] ##    #[[green]] ####### [[blue]] ##   ## [[yellow]]  ###### [[magenta]] #######[[cyan]]  ##   ##
   [[red]] ###   [[green]]  ##   [[blue]]    ###  ##  [[yellow]]   ##     [[magenta]]  ##  [[cyan]]  ##   ##
   [[red]]  #####  [[green]]###### [[blue]]  ## # ##  [[yellow]]   ##    [[magenta]]   ## [[cyan]]   #######
 [[red]]      ####[[green]] ## [[blue]]      ##  ###  [[yellow]]   ##  [[magenta]]     ##   [[cyan]] ##   ##
   [[red]] #    ## [[green]]####### [[blue]] ##   ##  [[yellow]] ######   [[magenta]]  ##   [[cyan]] ##   ##
   [[red]] ### ##

   [[red]]     _____ [[green]] _     [[blue]]       [[yellow]]       [[magenta]]     _ [[cyan]]       [[Bright Red]] _
   [[red]]    /  __ \[[green]]| |    [[blue]]       [[yellow]]       [[magenta]]    | |[[cyan]]       [[Bright Red]]| |
   [[red]]    | /  \/[[green]]| |__  [[blue]]  __ _ [[yellow]] _ __  [[magenta]]  __| |[[cyan]] _   _ [[Bright Red]]| |
   [[red]]    | |    [[green]]| '_ \ [[blue]] / _` |[[yellow]]| '_ \ [[magenta]] / _` |[[cyan]]| | | |[[Bright Red]]| |
   [[red]]    | \__/\[[green]]| | | |[[blue]]| (_| |[[yellow]]| | | |[[magenta]]| (_| |[[cyan]]| |_| |[[Bright Red]]| |
   [[red]]     \____/[[green]]|_| |_|[[blue]] \__,_|[[yellow]]|_| |_|[[magenta]] \__,_|[[cyan]] \__,_|[[Bright Red]]|_|

'''
Author = '''                [[red]]   Banner [[green]]Generater


'''


Anime(colorText(Banner))
AnimeText(colorText(Author))


def Art(a):
    tprint(a, font='rnd-medium')


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
