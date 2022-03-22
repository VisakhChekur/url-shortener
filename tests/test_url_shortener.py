import os
import sys
sys.path.insert(1, os.getcwd())
import url_shortener as us
from constants import url_base
import unittest


class TestURLShortener(unittest.TestCase):

    def test_valid_url_code(self):
        valid_code = "abcdef"
        invalid_code = "validcode"
        self.assertEqual(us.valid_url_code(invalid_code), False)
        self.assertEqual(us.valid_url_code(valid_code), True)
    
    def test_long_url_exists(self):

        existing_url = "www.existingwebsite.com"
        not_existing = "www.notawebsite.com"
        self.assertEqual(us.long_url_exists(existing_url), True)
        self.assertEqual(us.long_url_exists(not_existing), False)
    
    def test_get_short_url_code(self):
        
        url = "www.existingwebsite.com"
        self.assertEqual(us.get_short_url_code(url), "validcode")
    
    def test_url_shortener(self):
        
        url = "www.existingwebsite.com"
        self.assertEqual(us.url_shortener(url), url_base + "validcode")
    
    def test_get_long_url(self):

        url_code = "validcode"
        self.assertEqual(us.get_long_url(url_code), "www.existingwebsite.com")