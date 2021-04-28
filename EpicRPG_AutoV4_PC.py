import pyautogui
#from pyscreeze import ImageNotFoundException
import time

#active = True
#stopiter = False

def epicrpg():
    while True:
        checker = pyautogui.locateOnScreen('epic_guard_car.png')
        if checker != None:
            pyautogui.click(checker)
            return
        for j in range(6):
            checker = pyautogui.locateOnScreen('epic_guard_car.png')
            if checker != None:
                pyautogui.click(checker)
                return
            for k in range(2):
                checker = pyautogui.locateOnScreen('epic_guard_car.png')
                pyautogui.click(checker)
                if checker != None:
                    pyautogui.click(checker)
                    return
                for i in range(5):
                    checker = pyautogui.locateOnScreen('epic_guard_car.png')
                    if checker != None:
                        pyautogui.click(checker)
                        return
                    time.sleep(60)
                    time.sleep(1)
                    pyautogui.typewrite("rpg hunt",interval=0.25)
                    pyautogui.hotkey('enter')
                time.sleep(1)
                pyautogui.typewrite("rpg axe",interval=0.25)
                pyautogui.hotkey('enter')
            checker = pyautogui.locateOnScreen('epic_guard_car.png')
            pyautogui.click(checker)
            if checker != None:
                pyautogui.click(checker)
                return
            time.sleep(1)
            pyautogui.typewrite("rpg farm",interval=0.25)
            pyautogui.hotkey('enter')
        #time.sleep(1)
        #pyautogui.typewrite("rpg heal",interval=0.25)
        #pyautogui.hotkey('enter')
        checker = pyautogui.locateOnScreen('epic_guard_car.png')
        if checker != None:
            pyautogui.click(checker)
            return
        pyautogui.typewrite("rpg adv",interval=0.25)
        pyautogui.hotkey('enter')

        checker = pyautogui.locateOnScreen('epic_guard_car.png')
        if checker != None:
            pyautogui.click(checker)
            return
        time.sleep(1)
        pyautogui.typewrite("rpg heal",interval=0.25)
        pyautogui.hotkey('enter')

epicrpg()
    
   
