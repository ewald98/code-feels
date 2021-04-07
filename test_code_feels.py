import json
import os
import unittest


class MyTestCase(unittest.TestCase):

    def test_something(self):

        # TODO: assertEquals test.json with json_string
        json_string = """{"id": 1379122470595268616, "conversation_id": "1379122470595268616", 
        "created_at": "2021-04-05 20:23:14 EEST", "date": "2021-04-05", "time": "20:23:14", "timezone": "+0300", 
        "user_id": 1379085021508734986, "username": "onlytestinghere", "name": "tester", "place": "", 
        "tweet": "#python is better #justkidding", "language": "en", "mentions": [], "urls": [], "photos": [], 
        "replies_count": 0, "retweets_count": 1, "likes_count": 2, "hashtags": [ "python", "justkidding"], 
        "cashtags": [], "link": "https://twitter.com/onlytestinghere/status/1379122470595268616", "retweet": false, 
        "quote_url": "", "video": 0, "thumbnail": "", "near": "", "geo": "", "source": "", "user_rt_id": "", 
        "user_rt": "", "retweet_id": "", "reply_to": [], "retweet_date": "", "translate": "", "trans_src": "", 
        "trans_dest": ""}
        """
        expected_dict = json.loads(json_string)

        os.system('python3 code_feels.py hashtag=python user=onlytestinghere json=test.json')

        with open("test.json") as json_file:
            actual_dict = json.load(json_file)

        self.assertEqual(expected_dict, actual_dict)


if __name__ == '__main__':
    unittest.main()
