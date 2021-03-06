from peewee import * # all install
import csv

db = PostgresqlDatabase(database = 'instagram_db', user = 'postgres', password = 'wise2012A', host = 'localhost')

class Followers(Model):
    pk = CharField()
    full_name = CharField()
    username = CharField()
    is_private = CharField()
    profile_pic_url = TextField()
    profile_pic_id = TextField()
    is_verified = CharField()
    has_anonymous_profile_picture = CharField()
    latest_reel_media = CharField()
    
    class Meta:
        database = db

def main():
    db.connect()
    db.create_tables([Followers])
    
    with open("friendships.csv", "r", encoding='utf-8') as read_file:
        order = ['pk','full_name','username','is_private','profile_pic_url','profile_pic_id','is_verified','has_anonymous_profile_picture','latest_reel_media']
        reader = csv.DictReader(read_file, fieldnames = order)
       
        followers = list(reader)
        
        with db.atomic():
            for index in range(0, len(followers), 100):
                Followers.insert_many(followers[index:index + 100]).execute()
            
main()