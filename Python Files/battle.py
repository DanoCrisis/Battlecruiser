from printing import *
from sub_functions import add_s
from stats import battlecruiser

battle_actions_selected = []

def battle_choices():
    s = add_s(battlecruiser[10])
    print_c(f"You have {battlecruiser[10]} action{s} left this turn. ", color=Fore.BLUE, brightness=Style.BRIGHT)  
    # Check weapons in BC
    # Check number of actions allowed
    # Display Power reserve
    # Display Power (left) this turn
    pass