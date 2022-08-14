import sys
import json


def main(path):
    with open(path) as file: 
        data = json.load(file)


if __name__ == "__main__":

    if len(sys.argv) <= 1: 
        raise ValueError("Missing required CLI argument: no path for dataset file.")
    main(sys.argv[1])
