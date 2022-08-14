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
    

    for tweet in data: 
        push_most_retweeted(most_retweeted, tweet)

    

if __name__ == "__main__":

    if len(sys.argv) <= 1: 
        raise ValueError("Missing required CLI argument: no path for dataset file.")
    main(sys.argv[1])
