import csv
import re
import os

class SmartCsv():

    @classmethod
    def write_csv(cls, data, filename):

        with open(filename, 'a', newline='', encoding='utf-8') as file:
            order = ['pk',
                     'full_name',
                     'username',
                     'is_private']

            writer = csv.DictWriter(file, fieldnames=order)
            writer.writerow(data)

    @classmethod
    def create_my_common(cls):
        filename = 'data/my_common.csv'
        common = cls.read_compres_csv()
        cls.convert_write_csv(common, filename)
        print('create_csv')

    @classmethod
    def createUnfollowList(cls):
        filename = 'data/unfollow.csv'
        common = cls.getUnfollow()
        cls.convert_write_csv(common, filename)
        print('create_csv')


    @classmethod
    def create_work_and_my_common(cls):
        filename = 'data/work_and_my_common.csv'
        common = cls.read_compres_common_my_csv()
        cls.convert_write_csv(common, filename)
        print('create_csv')



    @classmethod
    def create_work_csv(cls):
        filename = 'data/common.csv'
        common = cls.read_compres_csv()
        cls.convert_write_csv(common, filename)
        print('create_csv')

    @classmethod
    def convert_write_csv(cls, data, filename):
        if os.path.isfile(filename) == True:
            os.remove(filename)

        for line in data:
            spliting = re.split(r'!=!=!', line)
            data_dict = {'pk': spliting[0],
            'full_name': spliting[1],
            'username': spliting[2],
            'is_private': spliting[3]
            }
            cls.write_csv(data_dict, filename)

    @classmethod
    def csv_reader(cls, file_obj):
        lister = []
        reader = csv.reader(file_obj)

        for row in reader:
            counter = 0
            for item in row:
                row[counter] = item + '!=!=!'
                counter += 1
            lister.append("".join(row))
        return lister

    @classmethod
    def read_file(cls, file):
        with open(file, "r", encoding='utf-8') as f_obj:
            data = cls.csv_reader(f_obj)
        return data

    @classmethod
    def read_compres_csv(cls):
        followers = cls.read_file("data/followers.csv")
        lendata1 = len(followers)

        friendship = cls.read_file("data/friendship.csv")
        lendata2 = len(friendship)

        #Пересечение обоих списков. Взаимные подписка
        #result = list(set(followers) & set(friendship))

        #Cписок уникальных элементов в объединении двух списков. Общий список уникальных аккаунтов
        result = list(set(followers + friendship))

        #Разность(Множество из friendship не входящее в followers Все друзья которые не подписаны
        #result = list(set(friendship) - set(followers))

        #Разность(Множество из followers не входящее в friendship. Все подписчики на которые не подписан аккунт
        #result = list(set(followers) - set(friendship))

        return result

    @classmethod
    def read_compres_common_my_csv(cls):
        common = cls.read_file("data/common.csv")
        my_common = cls.read_file("data/my_common.csv")

        #Разность(Множество из common не входящее в my_common. Все подписчики на которые не подписан аккунт
        result = list(set(common) - set(my_common))

        return result

    @classmethod
    def getUnfollow(cls):
        followers = cls.read_file("data/followers.csv")
        friendship = cls.read_file("data/friendship.csv")

        # Разность(Множество из common не входящее в my_common. Все подписчики на которые не подписан аккунт
        result = list(set(friendship) - set(followers))

        return result