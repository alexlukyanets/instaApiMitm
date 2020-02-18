import json
import csv
import time
class AccountInfo():

    @classmethod
    def get_from_json(cls):
        timing = time.time()
        while time.time() - timing < 4.0:
            try:
                with open("get_work/data/account_info.json", "r", encoding='utf-8') as read_file:
                    data = json.load(read_file)

            except:
                time.sleep(1)
                print('Timer')
                continue
            else:
                try:
                    contact_phone_number = data['user']['contact_phone_number']
                except:
                    contact_phone_number = ""

                try:
                    category = data['user']['category']
                except:
                    category = ""

                try:
                    mutual_followers_count = data['user']['mutual_followers_count']
                except:
                    mutual_followers_count = 0


                datadict = {

                    'username': data['user']['username'],
                    'media_count': data['user']['media_count'],
                    'biography': data['user']['biography'],
                    'mutual_followers_count': mutual_followers_count,
                    'contact_phone_number': contact_phone_number,
                    'category': category,
                    'is_business': data['user']['is_business'],
                    'follower_count': data['user']['follower_count'],
                    'following_count': data['user']['following_count']
                }
                print('I read data')
                return datadict

        return False




    @classmethod
    def get_number_of_followers(cls):
        with open("data/account_info.json", "r", encoding='utf-8') as read_file:
            data = json.load(read_file)
            print(f"From json {data['user']['follower_count']}")
        return (data['user']['follower_count'])

    @classmethod
    def get_number_of_friendship(cls):
        with open("data/account_info.json", "r", encoding='utf-8') as read_file:
            data = json.load(read_file)
        return (data['user']['following_count'])

    def write_csv_friendship(data):
        with open('data/account_info.csv', 'a', newline='', encoding='utf-8') as file:
            order = ['pk',
                     'full_name',
                     'username',
                     'is_private',
                     'profile_pic_url',
                     'profile_pic_id',
                     'is_verified',
                     'has_anonymous_profile_picture',
                     # 'latest_reel_media',
                     'media_count',
                     'geo_media_count',
                     'follower_count',
                     'following_count',
                     'following_tag_count',
                     'biography',
                     'external_url',
                     'has_biography_translation',
                     'is_business']
            writer = csv.DictWriter(file, fieldnames=order)
            writer.writerow(data)

    def read_json_write_csv():
        with open("data/account_info.json", "r", encoding='utf-8') as read_file:
            data = json.load(read_file)

        try:
            profile_pic_id = data['user']['profile_pic_id']
        except:
            profile_pic_id = ''

        datadict = {
            'pk': data['user']['pk'],
            'full_name': data['user']['full_name'],
            'username': data['user']['username'],
            'is_private': data['user']['is_private'],
            'profile_pic_url': data['user']['profile_pic_url'],
            'profile_pic_id': profile_pic_id,
            'is_verified': data['user']['is_verified'],
            'has_anonymous_profile_picture': data['user']['has_anonymous_profile_picture'],
            # 'latest_reel_media': data['user']['latest_reel_media'],
            'media_count': data['user']['media_count'],
            'geo_media_count': data['user']['geo_media_count'],
            'follower_count': data['user']['follower_count'],
            'following_count': data['user']['following_count'],
            'following_tag_count': data['user']['following_tag_count'],
            'biography': data['user']['biography'],
            'external_url': data['user']['external_url'],
            'has_biography_translation': data['user']['has_biography_translation'],
            'is_business': data['user']['is_business']}

        write_csv_friendship(datadict)
        print(datadict)