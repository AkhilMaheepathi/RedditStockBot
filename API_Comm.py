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
subred = reddit.subreddit("trakstocks")
#subreddit class methods: hot,new,controversial,top,gilded
hot = subred.hot(limit = 10)

for post in hot:
    print(post.title, post.url)