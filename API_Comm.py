import praw
import json


def create_reddit_object():
    with open('Credentials.json','r') as json_file: 
        userInfo = json.loads(json_file.read())

    reddit = praw.Reddit(client_id = userInfo['client_id'],
                        client_secret = userInfo['client_secret'],
                        user_agent = userInfo['user_agent'],
                        username = userInfo['username'],
                        password = userInfo['password'])

    return reddit

reddit = create_reddit_object()
trakstocks = reddit.subreddit("trakstocks")
wallstreetbets = reddit.subreddit('wallstreetbets')

#subreddit class methods: hot,new,controversial,top,gilded
TrakHot = trakstocks.hot(limit = 10)
WallHot = wallstreetbets.hot(limit = 10)

#for post in hot:
 #   print(post.title, post.url)
for post in WallHot:
    texts = post.title.split()
    print(texts)
    