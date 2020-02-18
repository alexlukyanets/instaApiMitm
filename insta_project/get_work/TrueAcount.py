import pyautogui
import pyautogui.tweens
import os
from fuzzywuzzy import fuzz
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

class TrueAccount():

    @classmethod
    def finder(cls, x, y, h, w, account):
        pyautogui.screenshot('my_screenshot.png', region=(x, y, h, w))
        find_string = pytesseract.image_to_string('my_screenshot.png')
        path = 'my_screenshot.png'
        os.remove(path)
        search = fuzz.ratio(find_string, account)
        print(find_string)
        print(search)
        if search > 30:
            return True
        else:
            return False

    @classmethod
    def true_account(cls, account):
        true = cls.finder(90, 105, 500, 20, account)
        if true == True:
            return True
        else :
            true = cls.finder(60, 0, 500, 17, account)
            if true == True:
                return True
            else:
                return False

#TrueAccount.true_account('inna kovtun')