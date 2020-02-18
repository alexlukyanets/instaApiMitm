def sum1forline(filename):
    with open(filename, encoding='utf-8') as f:
        return sum(1 for line in f)

filename1 = 'friendship.csv' 
filename2 = 'followers.csv'
print(sum1forline(filename1))
print(sum1forline(filename2))