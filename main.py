
import sys
import twint

# json

if __name__ == "__main__":

    print("No args:", len(sys.argv))
    print("Args:" + str(sys.argv))

    c = twint.Config()

    for argument in sys.argv:
        if "hashtag=" in argument:
            _, hashtag = argument.split("=", 1)
            c.Search = "#" + hashtag
        if "user=" in argument:
            _, user = argument.split("=", 1)
            c.Username = user
        if "term=" in argument:
            pass

    c.Store_json = True
    c.Output = "out.json"
    c.Limit = 20    # tweets to fetch, increments of 20
    data = twint.run.Search(c)
