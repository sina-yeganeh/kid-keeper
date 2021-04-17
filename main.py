from modules import banner, help_list, kid_keeper
from modules.help_list import waiting_input
from colorama import Fore as c
import sys

while True:
    banner.SLANT_banner()
    help_list.root_list()
    number = help_list.input_number()

    if number == 0:
        sys.exit()
    elif number == 1:
        number_of_take_screenshot = int(input(c.RED + " [" + c.WHITE + "~" + c.RED + "] " + c.BLUE + "Please enter your screenshot number > "))
        waiting_time = int(input(c.RED + " [" + c.WHITE + "~" + c.RED + "] " + c.BLUE + "Please enter your waiting time > "))
        kid_keeper.take_screenshot(number_of_take_screenshot, waiting_time)
        waiting_input()
    elif number == 2:
        help_list.how_to_use()
        waiting_input()
    elif number == 3:
        print(c.RED + "Coming Soon ...")
        waiting_input()
    elif number == 4:
        help_list.developer()
        waiting_input()
    else:
        print(c.RED + "Please Chose a Number")
