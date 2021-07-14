import argparse
import sys
import json
from colorama import Fore as c
from modules import banner, help_list, kid_keeper as kk
from modules.help_list import waiting_input
from modules.config import load_config_data



def cli_app():
    while True:
        banner.SLANT_banner()
        help_list.root_list()
        number = help_list.input_number()

        if number == 0:
            sys.exit()
        elif number == 1:
            number_of_take_screenshot = int(input(c.RED + " [" + c.WHITE + "~" + c.RED + "] " + c.BLUE + "Please enter number of screenshots > "))
            waiting_time = int(input(c.RED + " [" + c.WHITE + "~" + c.RED + "] " + c.BLUE + "Please enter delay (seconds) > "))
            kk.take_screenshot(number_of_take_screenshot, waiting_time)
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

def main():
    args = argparse.ArgumentParser(add_help="Kidd kipper")
    args.add_argument('-s', '--screenshots', dest="screenshots", type=int,
                      help="number of screenshots to take",
                      default=100)
    args.add_argument('-d', '--delay', dest="delay",type=float,
                      help="delay between each screenshot (seconds)",
                      default=25)
    args.add_argument('-c', '--config', dest="config", type=str,
                      help="configuration file path", default=None)
    args.add_argument('--cliapp', dest='cliapp', default=False,
                      help='if is specified, cli app starts',
                      action='store_true')
    parsed_arguments = args.parse_args()

    if parsed_arguments.cliapp:
        cli_app() # start cli app interface
    else:
        data = load_config_data(parsed_arguments.config) if parsed_arguments.config else {}
        config_params = {
            **data,
            "screenshots": parsed_arguments.screenshots,
            "delay": parsed_arguments.delay
        }
        kk.take_screenshot(**config_params)

if __name__ == "__main__":
    main()
