from pyautogui import screenshot
import time
from colorama import Fore as c

def take_screenshot(number_of_take_screenshot, waiting_time):
    try:
        number_of_take_screenshot = number_of_take_screenshot + 1
        print(c.RED + "\n [!] Start Keeping . . .")
        for i in range(1, number_of_take_screenshot):
            screenshot_image = screenshot()
            screenshot_image.save(r"./screenshot_images/screenshot" + str(i) + ".png")
            print(c.GREEN + "Toke Screenshot", str(i) + " Successfuly!")
            time.sleep(waiting_time)
    except Exception as err:
        print(err)
