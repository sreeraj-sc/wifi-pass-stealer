from unicodedata import name
import pyautogui as gui
import time
name = input('Enter wifi name :')
with gui.hold('winleft'):
    gui.press('r')
gui.typewrite('cmd')
gui.press('enter')
time.sleep(1)
gui.typewrite('netsh wlan show profile name="')
gui.typewrite(name)
gui.typewrite('" key=clear > E:\python\wifiPassword\data\output.txt')
gui.press('enter')
time.sleep(1)
gui.typewrite('E:')
gui.press('enter')
gui.typewrite('python\wifiPassword\data\output.txt')
gui.press('enter')