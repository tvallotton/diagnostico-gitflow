import sys
import json


def push_most_retweeted(current_top, new):
    if len(current_top) < 10:
        current_top.append(new)
        
    else: 
        for i, tweet in enumerate(current_top):
            if new["retweetCount"] > tweet["retweetCount"]:
                current_top[i] = new
                break




def main(path):

    with open("dataset.json") as file:
        data = [json.loads(data) for data in file.readlines()]

    most_retweeted = []
    users = {}
    days = {}
    hashtags = {}
    for tweet in data: 
        push_most_retweeted(most_retweeted, tweet)

        date = tweet["date"]
        tweet_count = users.get(date, [0])[0]
        days[date] = (tweet_count + 1, date)

        username = tweet["user"]["username"]
        tweet_count = users.get(username, [0])[0]
        users[username] = (tweet_count + 1, tweet["user"])

    users = list(users.values())
    users.sort(key=lambda x: -x[0])
    users = users[:10]
    
    days = list(days.values())
    days.sort(key=lambda x: -x[0])
    days = days[:10]

    with open("output.json", "w") as output: 
        json.dumps({
            "top_ten_days": days, 
            "top_ten_users": users, 
            "most_retweeted": most_retweeted,
            "hashtags": hashtags
        }, output)


if __name__ == "__main__":

    if len(sys.argv) <= 1: 
        raise ValueError("Missing required CLI argument: no path for dataset file.")
    main(sys.argv[1])
