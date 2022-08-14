import sys
import json
import re

from attr import has

HASHTAG = re.compile("#\w+")

def push_most_retweeted(current_top, new):
    if len(current_top) < 10:
        current_top.append(new)
        
    else: 
        for i, tweet in enumerate(current_top):
            if new["retweetCount"] > tweet["retweetCount"]:
                current_top[i] = new
                break


def insert_date(days, tweet): 
    date = tweet["date"]
    tweet_count = days.get(date, [0])[0]
    days[date] = (tweet_count + 1, date)

def insert_user(users, tweet): 
    username = tweet["user"]["username"]
    tweet_count = users.get(username, [0])[0]
    users[username] = (tweet_count + 1, tweet["user"])


def insert_hashtags(hashtags, tweet): 
    for hashtag in HASHTAG.findall(tweet["content"]):
        count = hashtags.get(hashtag, 0)
        hashtags[hashtag] = count + 1


def main(path):
    with open(path) as file:
        data = [json.loads(data) for data in file.readlines()]

    most_retweeted = []
    users = {}
    days = {}
    hashtags = {}
    for tweet in data: 
        push_most_retweeted(most_retweeted, tweet)
        insert_user(users, tweet)
        insert_date(days, tweet)
        insert_hashtags(hashtags, tweet)

    users = list(users.values())
    users.sort(key=lambda x: -x[0])
    users = users[:10]
    
    days = list(days.values())
    days.sort(key=lambda x: -x[0])
    days = days[:10]

    hashtags = list(hashtags.items())
    hashtags.sort(key=lambda x: -x[1])
    hashtags = hashtags[:10]

    with open("output.json", "w") as output: 
        json.dump({
            "top_ten_days": days, 
            "top_ten_users": users, 
            "most_retweeted": most_retweeted,
            "hashtags": hashtags
        }, output)


if __name__ == "__main__":

    if len(sys.argv) <= 1: 
        raise ValueError("Missing required CLI argument: no path for dataset file.")
    main(sys.argv[1])
