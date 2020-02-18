import csv


def write_csv_friendship(data):
    with open('data/common_new.csv', 'a', newline='', encoding='utf-8') as file:
        order = ['pk',
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
                 'blacklist']

        writer = csv.DictWriter(file, fieldnames=order)
        writer.writerow(data)


with open("data/work_and_my_common.csv", "r", encoding='utf-8') as read_file:
    order = ['pk',
             'full_name',
             'username',
             'is_private'
             ]

    reader = csv.DictReader(read_file, fieldnames=order)



    read_to_list = list(reader)
    print(type(reader))

for i in read_to_list:
    i.update({'last_opened': None})
    i.update({'liked': None})
    i.update({'my_follow': None})
    i.update({'my_friendship': None})
    i.update({'unsubscribing': None})
    i.update({'media_count': -1})
    i.update({'biography': None})
    i.update({'mutual_followers_count': -1})
    i.update({'contact_phone_number': None})
    i.update({'category': None})
    i.update({'is_business': None})
    i.update({'blacklist': None})

    write_csv_friendship(i)
