from Business.Search import Search
import unittest


class testcase(unittest.TestCase):
    def test_001(self):
        search = Search()
        search.search()

    def test_002(self):
        search = Search()
        search.search_unittest()
        # search_value = search.get_text("id", "cb_post_title_url")
        # self.assertEqual("Python单元测试unittest", search_value)


