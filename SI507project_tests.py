import unittest
from SI507project_tools import *

class TestScrapFunct(unittest.TestCase):
    def setUp(self):
        self.url = "https://millercenter.org/president"

    def test_return_value_type(self):
        result = scrape_function(self.url)
        self.assertTrue(type(result) is str)

class TestData(unittest.TestCase):
    def test_crawl_links(self):
        self.assertTrue(type(crawl_links) is list)

    def test_pres_links(self):
        self.assertTrue(type(pres_data_list) is list)

    def test_tag_links(self):
        self.assertFalse(type(a_tags_list) is str)

    def test_tag_links_true(self):
        self.assertTrue(type(a_tags_list) is list)
    # def test_full_name(self):
    #     self.assertNotEqual()

class TestPopData (unittest.TestCase):
    def test_make_pres_list(self):
        self.assertTrue(type(pres_data_list) is list)


if __name__ == '__main__':
    unittest.main()
