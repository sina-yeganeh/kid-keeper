from colorama import Fore as c
import os

def root_list():
    print(c.RED + "\n [" + c.WHITE + "1" + c.RED + "] " + c.WHITE + "Start Keeping")
    print(c.RED + " [" + c.WHITE + "2" + c.RED + "] " + c.WHITE + "How To Use")
    print(c.RED + " [" + c.WHITE + "3" + c.RED + "] " + c.WHITE + "Setting")
    print(c.RED + " [" + c.WHITE + "4" + c.RED + "] " + c.WHITE + "Developer")
    print(c.RED + " [" + c.WHITE + "0" + c.RED + "] " + c.RED + "Exit")

def input_number():
    print(c.BLUE + "\n Please Enter A Number")
    number = int(input(c.WHITE + " $ "))
    return number

def how_to_use():
    print(c.GREEN + """
 Just chose a number!""")

def developer():
    print(c.GREEN + """
 Develope by : sina-yeganeh(GitHub ID)
 Gmail       : sinayeganeh1384@gmail.com
 Discord     : Sina#7161""")

def waiting_input():
    input(c.WHITE + "> Press enter to continue . . .")
