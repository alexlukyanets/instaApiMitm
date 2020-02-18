import json
import csv

def write_csv_friendship(data):
    with open('account_info.csv','a', newline='', encoding='utf-8') as file:
        order = ['pk', 
        'full_name', 
        'username',
        'is_private',
        'profile_pic_url',
        'profile_pic_id',
        'is_verified',
        'has_anonymous_profile_picture',
        #'latest_reel_media', 
        'media_count',
        'geo_media_count',
        'follower_count',
        'following_count',
        'following_tag_count',
        'biography',
        'external_url',
        'has_biography_translation',
        'is_business']
        writer = csv.DictWriter(file, fieldnames = order)
        writer.writerow(data)

with open("account_info.json", "r", encoding='utf-8') as read_file:
    data = json.load(read_file)
 
try:
    profile_pic_id = data['user']['profile_pic_id']
except:
    profile_pic_id =''

datadict = {
'pk': data['user']['pk'],
'full_name': data['user']['full_name'],
'username': data['user']['username'],
'is_private': data['user']['is_private'],
'profile_pic_url': data['user']['profile_pic_url'],
'profile_pic_id': profile_pic_id,
'is_verified': data['user']['is_verified'],
'has_anonymous_profile_picture': data['user']['has_anonymous_profile_picture'],
#'latest_reel_media': data['user']['latest_reel_media'], 
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

"""

print(data['user']['pk'])
print(data['user']['username'])
print(data['user']['is_private'])
print(data['user']['profile_pic_url'])
try:
    print(data['user']['profile_pic_id'])
except:
    pass
print(data['user']['is_verified'])
print(data['user']['has_anonymous_profile_picture'])
print(data['user']['media_count'])
print(data['user']['geo_media_count'])
print(data['user']['follower_count'])
print(data['user']['following_count'])
print(data['user']['following_tag_count'])
print(data['user']['biography'])
print(data['user']['external_url'])
print(data['user']['has_biography_translation'])
print(data['user']['is_business'])



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