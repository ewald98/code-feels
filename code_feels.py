import os
import sys

import twint

if __name__ == "__main__":

    c = twint.Config()

    json_name = "out.json"  # default value

    for argument in sys.argv:
        if "hashtag=" in argument:
            _, hashtag = argument.split("=", 1)
            c.Search = "#" + hashtag
        if "user=" in argument:
            _, user = argument.split("=", 1)
            c.Username = user
        if "term=" in argument:
            _, term = argument.split("=", 1)
            c.Search = term
        if "json=" in argument:
            _, json_name = argument.split("=", 1)

    try:
        os.remove(json_name)
    except FileNotFoundError:
        pass

    c.Store_json = True
    c.Output = json_name
    c.Limit = 20  # tweets to fetch, increments of 20
    twint.run.Search(c)
