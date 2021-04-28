import pyautogui
#from pyscreeze import ImageNotFoundException
import time

#active = True
#stopiter = False
class RPG():
    def __init__(self):
        self.checker = self.pyautogui.locateOnScreen
    def epicrpg(self):
        while True:
            self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
            if self.checker != None:
                self.pyautogui.click(self.checker)
            return
            for j in range(6):
                self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
                if self.checker != None:
                    self.pyautogui.click(self.checker)
                    return
                for k in range(2):
                    self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
                    self.pyautogui.click(self.checker)
                    if self.checker != None:
                        self.pyautogui.click(self.checker)
                        return
                    for i in range(5):
                        self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
                        if self.checker != None:
                            self.pyautogui.click(self.checker)
                            return
                        time.sleep(60)
                        time.sleep(1)
                        self.pyautogui.typewrite("rpg hunt",interval=0.25)
                        self.pyautogui.hotkey('enter')
                    time.sleep(1)
                    self.pyautogui.typewrite("rpg axe",interval=0.25)
                    self.pyautogui.hotkey('enter')
                self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
                self.pyautogui.click(self.checker)
                if self.checker != None:
                    self.pyautogui.click(self.checker)
                    return
                time.sleep(1)
                self.pyautogui.typewrite("rpg farm",interval=0.25)
                self.pyautogui.hotkey('enter')
        #time.sleep(1)
        #self.pyautogui.typewrite("rpg heal",interval=0.25)
        #self.pyautogui.hotkey('enter')
            self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
            if self.checker != None:
                self.pyautogui.click(self.checker)
            return
            self.pyautogui.typewrite("rpg adv",interval=0.25)
            self.pyautogui.hotkey('enter')

            self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
            if self.checker != None:
                self.pyautogui.click(self.checker)
            return
            time.sleep(1)
            self.pyautogui.typewrite("rpg heal",interval=0.25)
            self.pyautogui.hotkey('enter')

"""
def epicrpg():
    while True:
        self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
        if self.checker != None:
            self.pyautogui.click(self.checker)
            return
        for j in range(6):
            self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
            if self.checker != None:
                self.pyautogui.click(self.checker)
                return
            for k in range(2):
                self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
                self.pyautogui.click(self.checker)
                if self.checker != None:
                    self.pyautogui.click(self.checker)
                    return
                for i in range(5):
                    self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
                    if self.checker != None:
                        self.pyautogui.click(self.checker)
                        return
                    time.sleep(60)
                    time.sleep(1)
                    self.pyautogui.typewrite("rpg hunt",interval=0.25)
                    self.pyautogui.hotkey('enter')
                time.sleep(1)
                self.pyautogui.typewrite("rpg axe",interval=0.25)
                self.pyautogui.hotkey('enter')
            self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
            self.pyautogui.click(self.checker)
            if self.checker != None:
                self.pyautogui.click(self.checker)
                return
            time.sleep(1)
            self.pyautogui.typewrite("rpg farm",interval=0.25)
            self.pyautogui.hotkey('enter')
        #time.sleep(1)
        #self.pyautogui.typewrite("rpg heal",interval=0.25)
        #self.pyautogui.hotkey('enter')
        self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
        if self.checker != None:
            self.pyautogui.click(self.checker)
            return
        self.pyautogui.typewrite("rpg adv",interval=0.25)
        self.pyautogui.hotkey('enter')

        self.checker = self.pyautogui.locateOnScreen('epic_guard_car.png')
        if self.checker != None:
            self.pyautogui.click(self.checker)
            return
        time.sleep(1)
        self.pyautogui.typewrite("rpg heal",interval=0.25)
        self.pyautogui.hotkey('enter')
"""

test = RPG()
test.epicrpg()
   
