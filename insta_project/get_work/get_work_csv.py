import re
import time
import os.path
import os
import json
import csv

def response(flow):
    pretty_url = flow.request.pretty_url
    account = re.match(r'https://i.instagram.com/api/v1/users/', pretty_url)
    info = re.search(r'/info/', pretty_url)

    both = re.match(r'https://i.instagram.com/api/v1/friendships/', pretty_url)
    follower = re.search(r'/followers/', pretty_url)
    friendships = re.search(r'/following/', pretty_url)

    if both != None and follower != None:
        write_followers(flow.response.text)
        time.sleep(1)
        convert_followers_json('data/followers')

    if both != None and friendships != None:
        write_friendship(flow.response.text)
        time.sleep(1)
        convert_followers_json('data/friendship')

    if account != None and info != None:
        write_txt_response_info_account(flow.response.text)


def write_txt_response_info_account(data):
    file_path = "data/account_info.json"
    if os.path.isfile(file_path) == True:
        os.remove(file_path)
        print('Delete JSON info_account')
    f = open(file_path, 'a')
    f.write(data)
    f.close()
    print('Create JSON info_account')

def write_friendship(data):
    file_path = "data/friendship.json"
    f = open(file_path, 'w')
    f.write(data)
    f.close()
    print('Create JSON friendship')


def write_followers(data):
    file_path = "data/followers.json"
    f = open(file_path, 'w')
    f.write(data)
    f.close()
    print('Create JSON followers')


def convert_followers_json(filename):
    with open(filename + '.json', "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename + '.json')
    os.remove(path)
    counter = 0

    for item in data['users']:
        counter += 1

        data = {'pk': item['pk'],
                'full_name': item['full_name'],
                'username': item['username'],
                'is_private': item['is_private']}

        write_csv(data, filename + '.csv')


def write_csv(data, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        order = ['pk',
                 'full_name',
                 'username',
                 'is_private']
        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)

