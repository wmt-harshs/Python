
Friends = open("/home/wmt/Python/Python/Files/File.txt", "r")
for friend in Friends.readlines():
    print(friend)
# print(friends.readline())
Friends.close()