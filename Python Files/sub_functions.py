from printing import *

def multiple_choice(text, options):
    acceptable_answer = False
    while acceptable_answer == False:
        answer = input(text)
        for option in options:
            if answer.lower() == option or answer.lower() == option[0]:
                acceptable_answer = True
                time.sleep(DELAY)
                print()
                return option
            
def add_s(digit):
    if(digit==1):
        s = ""
    else: s = "s"
    return s