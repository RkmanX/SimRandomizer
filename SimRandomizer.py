#  This is an older script that I rewrote to be more efficient. I'm a newbie obviously go easy.
#  I don't understand why The Sims 1 never included a random feature.
#  This code assumes you are running it in 800x600 windowed mode, modify the x/y values for your custom size.
from pyautogui import*
import time, random, win32api, win32con, win32gui


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def biology(x, y):
    print(x)
    if x == 2:
        click(x0 + 526, y0 + 350)
    else:
        click(x0 + 455, y0 + 350)
    if y == 0:
        click(x0 + 424, y0 + 269)
    if y == 1:
        click(x0 + 470, y0 + 269)
    if y == 2:
        click(x0 + 525, y0 + 269)

def irange(num, xz, yz, x, y):
    for i in range(num):
        click(xz + x, yz + y)


def clothes(a, b, x, y):
    irange(a, x0, y0, 605, 203)  # Left Head
    irange(b, x0, y0, 724, 203)
    irange(x, x0, y0, 587, 331)
    irange(y, x0, y0, 739, 331)


hwnd = win32gui.FindWindow(None, 'The Sims Complete Collection')

x0, y0, x1, y1 = win32gui.GetWindowRect(hwnd)
w = x1 - x0
h = y1 - x1
zodiac_sign = random.randint(1, 15)
running = True
gender = random.randint(1, 2)
skin = random.randint(0, 2)
head_left = random.randint(0, 100)
head_right = random.randint(0, 100)
body_left = random.randint(0, 100)
body_right = random.randint(0, 100)


if running is True:
    print('Starting. Please do not interact with computer until finished!')
    click(x0 + 268, y0 + 173)
    irange(zodiac_sign, x0, y0, 191, 328)
    time.sleep(0.5)
    biology(gender, skin)
    time.sleep(0.5)
    clothes(head_left, head_right, body_left, body_right)
    click(x0 + 66, y0 + 464)
    print('Alright this Character is Finished!')
    press('enter')
    typewrite('    This Sim was Generated by SimRandomizer')
    press('enter')
    typewrite('-Roninkin <(O.O<)')
    time.sleep(1)
    sys.exit()
