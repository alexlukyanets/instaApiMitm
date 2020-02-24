from get_work.DbWorking import DbWorking
from get_work.SearchAccount import SearchAccount
from get_work.SearchDataAccount import SearchDataAccount
from get_work.AccountInfo import AccountInfo
from get_work.SmartCsv import SmartCsv
import random
import time
import re


def verifyAccount(account):
    data = AccountInfo.get_from_json()
    print(data)

    if data != False:
        if account == data['username']:
            print(f'It`s need {account}')
            return True
        else:
            return False

def press_like(account):
    time.sleep(random.uniform(5, 7))
    data = AccountInfo.get_from_json()
    print(data)
    SearchDataAccount.get_scroling()
    if data != False:
        if account == data['username']:
            print(f'It`s need {account}')

        k = data['following_count'] / data['follower_count']
        if k > 0.1:
            DbWorking.update_db(data)

            if data['media_count'] > 0:
                like = SearchDataAccount.like(data['media_count'], 1, data['username'])

                if like == True:
                    time.sleep(random.uniform(30, 60))
        else:
            print(f'Save to BL becouse {k}')
            DbWorking.to_black_list(account)
    else:
        print(f'This cant like {account}')


def press_folowing():
    pass

def get_account():
    pass

def smart_like(counter):
    accounts = DbWorking.get_account_for_like()
    accounts = accounts[0:counter]
    random.shuffle(accounts)
    print(f'I must do {len(accounts)} to job')
    counter = 0
    for account in accounts:
        counter += 1
        print()
        print(counter)
        time.sleep(random.uniform(3, 5))

        breaker = SearchAccount.search_and_open_account(account)

        if breaker == False:
            print('Next becouse haven`t exist')
            DbWorking.to_black_list(account)
            print('Welcome to DB')
            continue


        press_like(account)

def follow(counter):
    accounts = DbWorking.get_account_for_follow()
    accounts = accounts[0:counter]
    print(f'I must do {len(accounts)} to follow job')
    for account in accounts:
        print()
        breaker = SearchAccount.search_and_open_account(account[0])
        if breaker == False:
            print('Next becouse haven`t exist')
            continue
        #time.sleep(random.uniform(1, 10))

        data = AccountInfo.get_from_json()


        if data != False:
            print(data)
            if account[0] == data['username']:
                print(f'It`s need {account[0]}')

                result = SearchDataAccount.follow(account[0])


                if result == True:
                    DbWorking.follow_to_db(account[0])
                    print(f" I follow {account[0]}")
                    time.sleep(random.uniform(30, 60))


def getAccountFromCsv():
    unfollow = get_read_csv('get_work/data/unfollow.csv')
    print(unfollow)
    accounts = []
    for strings in unfollow:
        account = re.split(r',', strings)
        accounts.append(account[2])

    return accounts

def get_read_csv(filename):
    with open(filename, encoding='utf-8') as f:
        work = f.read()
    work = work.split('\n')
    return work

def unfollow():
    #SmartCsv.createUnfollowList()
    time.sleep(3)
    accounts = getAccountFromCsv()


    for account in accounts[75:300]:
        print()
        time.sleep(random.uniform(3,5))
        print(account)
        SearchAccount.search_and_open_account(account)

        itsneed = verifyAccount(account)

        if itsneed:

            SearchDataAccount.unfollow()
            time.sleep(random.uniform(30, 60))
            SearchDataAccount.unfollowElse()


        else:
            print(f'Next account becouse it`s false {account}')

def main():
    unfollow()
    #smart_like(30)
    #follow(25)
    #time.sleep(random.uniform(150, 200))
    #follow(25)

    """time.sleep(random.uniform(150, 200))
    follow(5)
    time.sleep(random.uniform(150, 200))
    smart_like(30)
    follow(10)
    time.sleep(random.uniform(150, 200))

    smart_like(30)
    follow(5)
    time.sleep(random.uniform(150, 200))
    follow(5)
    time.sleep(random.uniform(150, 200))
    smart_like(30)
    follow(10)
    time.sleep(random.uniform(150, 200))

    smart_like(30)
    follow(5)
    time.sleep(random.uniform(150, 200))
    follow(5)"""

if __name__ == '__main__':
    main()