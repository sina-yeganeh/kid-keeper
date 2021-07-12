from os import path
import time
import pathlib
from colorama import Fore as c
from pyautogui import screenshot
from .settings import BASE_DIR


def take_screenshot(screenshots: int, delay: float):
    try:
        screenshots = screenshots + 1
        print(c.RED + "\n [!] Keeping Started . . .")
        for i in range(1, screenshots):
            screenshot_image = screenshot()
            screenshot_image.save((BASE_DIR / (r"./screenshot_images/screenshot" + str(i) + ".png")).resolve())
            print(c.GREEN + "Took Screenshot", str(i) + " Successfuly!")
            time.sleep(delay)
    except Exception as err:
        print(err)
