from peewee import * # all install
import csv

db = PostgresqlDatabase(database = 'instagram_db', user = 'postgres', password = 'wise2012A', host = 'localhost')

class Account_info(Model):
    pk = CharField()
    full_name = CharField()
    username = CharField()
    is_private = CharField()
    profile_pic_url = TextField()
    profile_pic_id = TextField()
    is_verified = CharField()
    has_anonymous_profile_picture = CharField()
    media_count = IntegerField()
    geo_media_count = IntegerField()
    follower_count = IntegerField()
    following_count = IntegerField()
    following_tag_count = IntegerField()
    biography = TextField()
    external_url = TextField()
    has_biography_translation = CharField()
    is_business = CharField()

    class Meta:
        database = db

def main():
    db.connect()
    db.create_tables([Account_info])
    
    with open("account_info.csv", "r", encoding='utf-8') as read_file:
        order = ['pk',
        'full_name',
        'username',
        'is_private',
        'profile_pic_url',
        'profile_pic_id',
        'is_verified',
        'has_anonymous_profile_picture',
        'media_count',
        'geo_media_count',
        'follower_count',
        'following_count',
        'following_tag_count',
        'biography',
        'external_url',
        'has_biography_translation',
        'is_business']

        reader = csv.DictReader(read_file, fieldnames = order)
       
        account_info = list(reader)
        
        with db.atomic():
            for index in range(0, len(account_info), 100):
                Account_info.insert_many(account_info[index:index + 100]).execute()
            
main()