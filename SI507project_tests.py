import unittest
from SI507project_tools import *

class TestScrapFunct(unittest.TestCase):
    def setUp(self):
        self.url = "https://millercenter.org/president"

    def test_return_value_type(self):
        result = scrape_function(self.url)
        self.assertTrue(type(result) is str)

class TestPresCsvFunct(unittest.TestCase):
    def setUp(self):
        self.list_dicts = pres_data_list
        self.result = make_pres_csv(self.list_dicts)
        self.header_list = ['President Number', 'Last Name', 'First Name', 'Birthday', 'Education' ,'Inagural Date', 'Religon', 'Career', 'Party']

    def test_return_not_int(self):
        self.assertFalse(self.result is int)

    def test_return_not_str(self):
        self.assertFalse(self.result is str)

    def test_return_not_tup(self):
        self.assertFalse(self.result is tuple)

    def test_return_is_list(self):
        self.assertTrue(self.result is list)

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

if __name__ == '__main__':
    unittest.main()
