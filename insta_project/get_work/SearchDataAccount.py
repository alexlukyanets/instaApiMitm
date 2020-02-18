import pyautogui
import pyautogui.tweens
import random
import time
from get_work.DbWorking import DbWorking

#from DbWorking import DbWorking
class SearchDataAccount():

    @classmethod
    def search_and_click_point(cls, image, add_x, add_y):
        searcher = pyautogui.locateOnScreen(image, confidence=0.9)
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
    def follow(cls, account):
        friendship = pyautogui.locateOnScreen('image/unfollow.png')
        follow = pyautogui.locateOnScreen('image/follow.png')

        if follow != None:
            #print(f"follow + {follow}")
            time.sleep(random.uniform(1, 2))
            cls.search_and_click_point('image/follow.png', False, False)
            time.sleep(random.uniform(1, 2))

            friendship = pyautogui.locateOnScreen('image/unfollow.png')
            if friendship != None:
                return True
            else:
                return False

        if friendship != None:
            DbWorking.follow_to_db(account)
            return False
        #print(f"friendship + {friendship}")


        #cls.search_and_click_point('image/follow.png', False, False)
        #cls.search_and_click_point('friendship.png', False, False)
        #time.sleep(random.uniform(1,2))
        #searcher = pyautogui.locateOnScreen('friendship.png', confidence=0.9)
        #print(searcher)


    @staticmethod
    def unfollow():
        search_and_click_point('image/unfollow.png', False, False)

    @classmethod
    def findlike_and_get_like(cls, makelike, username):
        likepost = list(range(0, 3))
        slicer = 3 - makelike
        random.shuffle(likepost)
        likepost = likepost[slicer:]
        alllikes = list(pyautogui.locateAllOnScreen('image/like.png', confidence=0.9))

        try:
            for onelike in likepost:
                pyautogui.click(alllikes[onelike].left + 5, alllikes[onelike].top + 5)
                print('Post is liked')
                time.sleep(random.uniform(1.3, 2.8))

            DbWorking.like_to_db(username)
            print('Save data in DB')

            return True
        except:
            return False


    @classmethod
    def like(cls, posts, makelike, username):
        break_timer = False
        timing = time.time()
        while time.time() - timing < 7:
            alllikes = pyautogui.locateAllOnScreen('image/like.png')

            if len(list(alllikes)) == 0:
                print('Timer for finder')
                time.sleep(0.5)
            else:

                break_timer = True
                break

        if break_timer == True:
            print('Need to like')

            if makelike >= posts:
                makelike = posts

            if makelike == 3:
                print("Two one like")
                succes = cls.findlike_and_get_like(2, username)

                if succes == True:
                    time.sleep(2)
                    pyautogui.keyDown('down')
                    pyautogui.keyUp('down')
                    time.sleep(3)
                    cls.findlike_and_get_like(1, username)

            if makelike <= 2:
                print("Almost one like")
                cls.findlike_and_get_like(makelike, username)

            return True



        else:
            print('I have n`t find like')
            return False



    @classmethod
    def get_followers(cls):
        folowers = pyautogui.locateOnScreen('image/folowers.png')
        while folowers == None:
            folowers = pyautogui.locateOnScreen('image/folowers.png')
            time.sleep(0.3)
        pyautogui.click(folowers.left + 30, folowers.top - 10)
        time.sleep(2)

    @classmethod
    def get_scroling(cls):
        pyautogui.scroll(-999999999)

    @classmethod
    def get_friendship(cls):
        friendship = pyautogui.locateOnScreen('image/friendship.png')
        while friendship == None:
            friendship = pyautogui.locateOnScreen('image/friendship.png')
            time.sleep(0.3)
        pyautogui.click(friendship.left + 30, friendship.top - 10)
        time.sleep(2)

#SearchDataAccount.like(1,1, "filip_gerasim")
#print(SearchDataAccount.follow())