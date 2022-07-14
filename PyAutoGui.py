import pyautogui as pg
import time
import keyboard

text = ""
keyboard.wait('Enter')
text = text.split()
for word in text:
    for char in word:
        pg.write(char, interval=.00001)
    pg.write(" ")

# time.sleep(4)
# for i in range(1, 1920, 40):
#     for j in range(1, 1080, 40):
#         pg.moveTo(i, j)
#         pg.click()
# for i in range(20):
#     pg.hotkey('ctrl', 'p')
#     pg.moveTo(1409, 880)
#     pg.click()
#     time.sleep(1)
#     pg.hotkey("enter")
#     pg.moveTo(272,
#               22)
#     pg.click()
#     time.sleep(1)

# while True:
#     time.sleep(5)
#     x, y = pg.position()
#     coordinates = 'X: ' + str(x) + ' Y: ' + str(y)
#     print(coordinates)
