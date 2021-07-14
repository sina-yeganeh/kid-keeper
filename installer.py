import os
import sys
from modules.settings import BASE_DIR, SCREENSHOT_DIR

if not os.path.exists(sfullpath:=(BASE_DIR / SCREENSHOT_DIR).resolve()):
    os.mkdir(sfullpath)

os.system({
    'win32': 'python -m pip',
    'linux': 'pip3'
}[sys.platform] + ' install -r ./requirements.txt')