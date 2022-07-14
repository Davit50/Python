from pyautogui import press, locateOnScreen, size


def check():
    width_ = size()[0]
    height_ = size()[1]
    if locateOnScreen('img.png', region=(width_ * 0.375, height_ * 0.2685, width_ * 0.07813, height_ * 0.056)) != None:
        press('space')


while True:
    check()
# if locateOnScreen('img.png', region=(740, 290, 150, 60)) != None:
# Dino(left=600, top=310, width=70, height=70)
