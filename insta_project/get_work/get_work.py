from SearchAccount import SearchAccount
from SearchDataAccount import SearchDataAccount
from AccountInfo import AccountInfo
from SmartCsv import SmartCsv
import time
import os
import pyautogui
import pyautogui.tweens
import random

def get_my_account():
    followers = 'data/followers.csv'
    try:
        old_csv = sumline(followers)
    except FileNotFoundError:
        old_csv = 0


    SearchDataAccount.get_followers()
    number_of_followers = AccountInfo.get_number_of_followers()
    print(number_of_followers)
    get_followers_get_friendship(number_of_followers, followers, old_csv)

    print()
    pyautogui.click(500, 150)

    friendship = 'data/friendship.csv'
    try:
        old_csv = sumline(friendship)
    except FileNotFoundError:
        old_csv = 0


    SearchDataAccount.get_friendship()
    number_of_friendship = AccountInfo.get_number_of_friendship()
    get_followers_get_friendship(number_of_friendship, friendship, old_csv)
    print(number_of_friendship)


def true_main():
    work = get_read_csv()

    for item in work:
        print('Start ' + item)
        SearchAccount.search_and_open_account(item)
        get_my_account()
        #os.remove('data/friendship.csv')
        #os.remove('data/followers.csv')
    SmartCsv.create_work_csv()

def sumline(filename):
    with open(filename, encoding='utf-8') as f:
        return sum(1 for line in f)

def get_followers_get_friendship(number_of, file, old_csv):
    time.sleep(random.uniform(0, 2))

    print()
    while True:
        print(old_csv)
        print(number_of)
        print(sumline(file))
        print('Scroling')
        SearchDataAccount.get_scroling()
        SearchDataAccount.get_scroling()
        time.sleep(random.uniform(0,1))

        if sumline(file) + 3 >= old_csv + number_of:
            break

    print(f'All {file} done')

def get_read_csv():
    with open('data/work.csv') as f:
        work = f.read()
    work = work.split('\n')
    return work

def main():
    #true_main()
    #get_my_account()
    #SmartCsv.create_my_common()
    SmartCsv.create_work_and_my_common()


main()

