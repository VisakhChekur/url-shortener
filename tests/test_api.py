import unittest
import requests
import requests
import os
import sys
sys.path.insert(1, os.getcwd())
from constants import url_base


URL = url_base + "api"

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.data_long = {
            "long_url": "www.existingwebsite.com",
        }
        self.data_long_invalid = {
            "long_url": "www.nonexistanturl.com"
        }
        self.data_short = {
            "short_url": url_base + "validcode",
        }
        self.data_short_invalid = {
            "short_url": "invalidcode",
        }
        self.data_url_code = {
            "short_url": "validcode",
        }
        self.data_invalid = {
            "wrong key": "value"
        }

    def test_post_request(self):
        
        response_fail = requests.post(URL, data=self.data_long)
        response_invalid = requests.post(URL, data=self.data_invalid)
        
        self.assertEqual(response_fail.status_code, 400)
        self.assertEqual(response_invalid.status_code, 400)

    def test_get_request(self):
        
        response_long = requests.get(URL, data=self.data_long)
        response_short = requests.get(URL, data=self.data_short)
        response_url_code = requests.get(URL, data=self.data_url_code)
        response_short_invalid = requests.get(URL, data=self.data_short_invalid)
        response_long_invalid = requests.get(URL, data=self.data_long_invalid)
        response_invalid = requests.get(URL, data=self.data_invalid)


        self.assertEqual(response_long.status_code, 200)
        self.assertEqual(response_short.status_code, 200)
        self.assertEqual(response_url_code.status_code, 200)
        self.assertEqual(response_short_invalid.status_code, 404)
        self.assertEqual(response_long_invalid.status_code, 404)
        self.assertEqual(response_invalid.status_code, 400)
        

        
        