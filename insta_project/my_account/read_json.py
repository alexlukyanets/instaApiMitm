import json
import csv

def write_csv_friendship(data):
    #with open('friendships.csv','a', newline='', encoding='utf-8') as file:
    with open('followers.csv','a', newline='', encoding='utf-8') as file:
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


#with open("friendships.json", "r", encoding='utf-8') as read_file:
with open("followers.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

#print(data['users'])
counter = 0
for item in data['users']:
    print(item['is_private'])
    try:
        profile_pic_id = item['profile_pic_id']
    except:
        profile_pic_id =''

    #if item['is_private'] == 'true':
        #is_private = True
    #else:
        #s_private = False

    data = {'pk': item['pk'],
    'full_name': item['full_name'],
    'username': item['username'],
    'is_private': item['is_private'],
    'profile_pic_url': item['profile_pic_url'],
    'profile_pic_id': profile_pic_id,
    'is_verified': item['is_verified'],
    'has_anonymous_profile_picture': item['has_anonymous_profile_picture'],
    'latest_reel_media': item['latest_reel_media']}
         
    counter += 1
    
    print(counter)
    write_csv_friendship(data)
    #print(data)
    #print()


"""
counter = 0
for item in data['users']:
    
    counter += 1
    
    print(counter)

    print(item['pk'])
    print(item['username'])
    print(item['is_private'])
    print(item['profile_pic_url'])
    try:
        print(item['profile_pic_id'])
    except:
        pass
    print(item['is_verified'])
    print(item['has_anonymous_profile_picture'])
    print(item['latest_reel_media'])

    print()
"""