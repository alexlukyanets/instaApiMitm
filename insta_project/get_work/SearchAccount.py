import pyautogui
import pyautogui.tweens
import os
import re
import time
import random
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

class SearchAccount():
    @classmethod
    def search_and_open_account(cls, account):
        time.sleep(random.uniform(1,2))
        cls.search_and_click_point('image/search.png', False, False)
        time.sleep(random.uniform(0, 1))
        cls.click_search_icon_two()
        time.sleep(random.uniform(0, 1))
        print(f'Write {account}')
        pyautogui.write(account)
        time.sleep(random.uniform(5, 7))
        cls.best_find_need_account(account)
        time.sleep(random.uniform(0, 1))
        exisying = pyautogui.locateOnScreen('image/no_exist_user.png', confidence=0.9)
        if exisying == None:
            return True
        else:
            return False



    @classmethod
    def have_string_in_shortcut(cls, account):
        pyautogui.screenshot('my_screenshot.png', region=(540, 170, 200, 20))
        find_string = pytesseract.image_to_string(Image.open('my_screenshot.png'))
        time.sleep(0.5)
        path = 'my_screenshot.png'
        os.remove(path)
        search = re.search(account, find_string)

        if search == None:
            return False
        else:
            return True

    @classmethod
    def search_and_click_point(cls, image, add_x, add_y):
        searcher = pyautogui.locateOnScreen(image, confidence=0.9)
        while searcher == None:
            searcher = pyautogui.locateOnScreen(image, confidence=0.9)
            time.sleep(0.35)
        point = pyautogui.center(searcher)
        x_point, y_point = point

        if x_point == False and y_point == False:
            pyautogui.click(x_point, y_point)

        elif x_point == False:
            pyautogui.click(x_point, y_point + add_y)

        elif y_point == False:
            pyautogui.click(x_point + add_x, y_point)

        else:
            pyautogui.click(x_point + add_x, y_point + add_y)

    @classmethod
    def best_find_need_account(cls, account):
        cls.search_and_click_point('image/best_find_need_account.png', False, 35)
        have = True
        while have != False:
            have = cls.have_string_in_shortcut(account)
            time.sleep(0.3)

        time.sleep(random.uniform(1,3))
        pyautogui.doubleClick()
        time.sleep(random.uniform(0, 1))

        #print('I found ' + account)

    @classmethod
    def click_search_icon_two(cls):
        cls.search_and_click_point('image/search_two_step.png', False, False)
        finder_for_last = pyautogui.locateOnScreen('image/finder_for_last.png', confidence=0.9)

        if finder_for_last == None:
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')

#print(SearchAccount.search_and_open_account('wolrus'))
#print()
#print(SearchAccount.search_and_open_account('valentine1li'))