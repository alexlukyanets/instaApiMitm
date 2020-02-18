import re
import json
import csv
import os

def response (flow):
    
    pretty_url = flow.request.pretty_url
    account = re.match(r'https://i.instagram.com/api/v1/users/', pretty_url)
    info = re.search(r'/info/', pretty_url)

    both = re.match(r'https://i.instagram.com/api/v1/friendships/', pretty_url)
    follower = re.search(r'/followers/', pretty_url)
    friendships = re.search(r'/following/', pretty_url)

    if both != None and follower != None:
        write_followers(flow.response.text)
        convert_followers_json('followers')

    if both != None and friendships != None:
        write_friendship(flow.response.text)
        convert_followers_json('friendship')

    if account != None and info != None:
        write_txt_response_info_account(flow.response.text)



def write_txt_response_info_account(data):
    f = open("account_info.json", 'w')
    f.write(data)
    f.close()

def write_friendship(data):
    f = open("friendship.json", 'w')
    f.write(data)
    f.close()

def write_followers(data):
    f = open("followers.json", 'w')
    f.write(data)
    f.close()

def convert_followers_json(filename):
    with open(filename + '.json', "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename + '.json')
    os.remove(path)
    counter = 0
    for item in data['users']:
        counter += 1
        print(counter)

        try:
            profile_pic_id = item['profile_pic_id']
        except:
            profile_pic_id =''

        data = {'pk': item['pk'],
        'full_name': item['full_name'],
        'username': item['username'],
        'is_private': item['is_private'],
        'profile_pic_url': item['profile_pic_url'],
        'profile_pic_id': profile_pic_id,
        'is_verified': item['is_verified'],
        'has_anonymous_profile_picture': item['has_anonymous_profile_picture'],
        'latest_reel_media': item['latest_reel_media']}
            
       
        write_csv(data, filename + '.csv')

def write_csv(data, filename):
    with open(filename,'a', newline='', encoding='utf-8') as file:
        order = ['pk', 
        'full_name', 
        'username',
        'is_private',
        'profile_pic_url',
        'profile_pic_id',
        'is_verified',
        'has_anonymous_profile_picture',
        'latest_reel_media']
        writer = csv.DictWriter(file, fieldnames = order)
        writer.writerow(data)





