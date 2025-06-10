import time
import sys
from colorama import init, Fore, Back, Style
import keyboard

init()
FORE = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]    # Sets the Foreground Colours
BACK = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]    # Sets the Background Colours
BRIG = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]                                                            # Sets the brightness styles

TYPE_SPEED = 0.00                                                                                          # Sets the slow typing speed
DELAY = 0.2                                                                                                # Sets the text delay speed

keyboard.on_press_key("backspace", lambda _:skip())
keyboard.on_release_key("backspace", lambda _:unskip())

def skip():
    global TYPE_SPEED
    TYPE_SPEED = 0

def unskip():
    global TYPE_SPEED
    TYPE_SPEED = 0.00

def print_s(str):                                                                                           # Defines a slow print
    for char in str:
            time.sleep(TYPE_SPEED)
            sys.stdout.write(char)
            sys.stdout.flush()
    print()

def print_c(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):                                        # Defines a colour print
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

def print_s_c(str, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):                                    # Defines a slow colour print
    for char in str:
            time.sleep(TYPE_SPEED)
            sys.stdout.write(f"{brightness}{color}{char}{Style.RESET_ALL}", **kwargs)
            sys.stdout.flush()
    print()

def s_print(text, colour):                                                                # Defines a standard print with colour, speed and space
    print_s_c(text, colour, brightness=Style.NORMAL)
    time.sleep(DELAY)
    print()
     