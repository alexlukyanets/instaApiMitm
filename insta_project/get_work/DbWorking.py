from peewee import *  # all install
from peewee import PostgresqlDatabase

import csv
import datetime
import random
from dateutil.parser import parse

#db = PostgresqlDatabase(database='instagram_db', user='postgres', password='wise2012A', host='localhost')
db = PostgresqlDatabase(database='instagram_db_pasha', user='postgres', password='wise2012A', host='localhost')

class UnfollowKJob(Model):
    pk = CharField()
    full_name = CharField()
    username = CharField()
    is_private = CharField()
    last_opened = CharField()
    liked = CharField()
    my_follow = CharField()
    my_friendship = CharField()
    unsubscribing = CharField()
    media_count = IntegerField()
    biography = TextField()
    mutual_followers_count = IntegerField()
    contact_phone_number = CharField()
    category = CharField()
    is_business = CharField()
    blacklist = CharField()
    message = CharField()

    class Meta:
        database = db
        null = False



class JobWork(Model):
    pk = CharField()
    full_name = CharField()
    username = CharField()
    is_private = CharField()
    last_opened = CharField()
    liked = CharField()
    my_follow = CharField()
    my_friendship = CharField()
    unsubscribing = CharField()
    media_count = IntegerField()
    biography = TextField()
    mutual_followers_count = IntegerField()
    contact_phone_number = CharField()
    category = CharField()
    is_business = CharField()
    blacklist = CharField()
    message = CharField()

    class Meta:
        database = db
        null = False

class DbWorking():

    @staticmethod
    def save_db():
        db.connect()
        db.create_tables([JobWork])

        with open("data/common_new.csv", "r", encoding='utf-8') as read_file:
            order = [
                     'pk',
                     'full_name',
                     'username',
                     'is_private',
                     'last_opened',
                     'liked',
                     'my_follow',
                     'my_friendship',
                     'unsubscribing',
                     'media_count',
                     'biography',
                     'mutual_followers_count',
                     'contact_phone_number',
                     'category',
                     'is_business',
                     'blacklist',
                      'message']

            reader = csv.DictReader(read_file, fieldnames=order)

            jobwork = list(reader)

            with db.atomic():
                for index in range(0, len(jobwork), 100):
                    JobWork.insert_many(jobwork[index:index + 100]).execute()

    @classmethod
    def get_rand(cls):
        num_records = JobWork.select().count()
        #print(num_records)
        to_rand = [l for l in range(1, num_records)]
        rand = random.choice(to_rand)
        return rand

    @classmethod
    def get_account_from_db(cls):
        rand = cls.get_rand()
        #print(rand)
        account = JobWork.select(JobWork.username).where(JobWork.id == rand).get()
        return account.username

    @classmethod
    def get_account_for_like(cls):
        #db.connect()
        query = (JobWork.select(JobWork.username, JobWork.liked, JobWork.blacklist, JobWork.media_count).where(JobWork.is_private == 'False'))
        account = []
        for i in query:
            if i.liked == "" and i.blacklist == "" and i.media_count != 0:
                account.append(i.username)
        return account

    @classmethod
    def like_to_db(cls, account):
        query = JobWork.update(liked=datetime.datetime.now()).where(JobWork.username == account)
        query.execute()

    @classmethod
    def follow_to_db(cls, account):
        query = JobWork.update(my_follow=datetime.datetime.now()).where(JobWork.username == account)
        query.execute()

    @classmethod
    def unfollow_to_db(cls, account):
        query = UnfollowKJob.update(unsubscribing=datetime.datetime.now()).where(UnfollowKJob.username == account)
        query.execute()

    @classmethod
    def get_unfollow_accounts(cls):
        query = (UnfollowKJob.select(UnfollowKJob.username).where(UnfollowKJob.unsubscribing == ''))
        account = []
        for i in query:
            account.append(i.username)
        return account


    @classmethod
    def to_black_list(cls, account):
        #db.connect()
        query = JobWork.update(blacklist='True').where(JobWork.username == account)
        query.execute()

    @classmethod
    def update_db(cls, data):
        category = data['category']

        if category == None:
            category = 'Common'
        # db.connect()
        query = JobWork.update(media_count=data['media_count'],
                               biography = data['biography'],
                               mutual_followers_count=data['mutual_followers_count'],
                               contact_phone_number=data['contact_phone_number'],
                               category=category,
                               is_business=data['is_business']
                               ).where(JobWork.username == data['username'])

        query.execute()

    @classmethod
    def update_data_unfollow_db(cls, data):
        category = data['category']

        if category == None:
            category = 'Common'
            # db.connect()
        query = UnfollowKJob.update(media_count=data['media_count'],
                                biography=data['biography'],
                                mutual_followers_count=data['mutual_followers_count'],
                                contact_phone_number=data['contact_phone_number'],
                                category=category,
                                is_business=data['is_business']
                                ).where(UnfollowKJob.username == data['username'])

        query.execute()

    @classmethod
    def get_account_for_follow(cls):
        query = (JobWork.select(JobWork.username, JobWork.liked, JobWork.my_follow).where(JobWork.liked != ''))
        account = {}
        for i in query:
            if i.my_follow == "":
                dt = parse(i.liked)
                account[i.username] = dt
                #print(dt.date())
                #print(dt.time())
                #account.append(i.liked)


        account = sorted(account.items(), key=lambda p: p[1], reverse=False)
        return account





def main():
    db.connect()

if __name__ == '__main__':
    main()
    #print(DbWorking.get_unfollow_accounts('na4_blogers'))
    #DbWorking.save_db()
    #DbWorking.check_like('unison_kiev')
    #DbWorking.like_to_db('rodionov1620')
    #DbWorking.get_account_public_db()
    #DbWorking.get_liked_account()
    #DbWorking.get_last_liked_account()
