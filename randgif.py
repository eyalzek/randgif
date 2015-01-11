#!/usr/bin/python
import random
import sys
import webbrowser
import requests

def main(argv):
    r = requests.get(get_url("+".join([str(arg) for arg in argv[1:]])))
    try:
        webbrowser.open(random.choice(r.json()["data"])["images"]["original"]["url"])
    except IndexError:
        print("No gifs found for this query")

def get_url(query):
    return "http://api.giphy.com/v1/gifs/search?q={}&api_key=dc6zaTOxFJmzC".format(query)

if __name__ == "__main__":
    main(sys.argv)
