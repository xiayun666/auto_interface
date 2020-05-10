from TestCase.testcase import testcase
import unittest
from Commonlib.HTMLTestRunner import HTMLTestRunner


class SuitTest(unittest.TestCase):
    def test_suit(self):
        case_list = ["test_001", "test_002"]
        my_suit = unittest.TestSuite()
        for case in case_list:
            my_suit.addTest(testcase(case))
        # unittest.TextTestRunner(verbosity=2).run(my_suit)
    # def test_suit(self):
    #     mysuit = unittest.TestSuite
    #     all_case = unittest.defaultTestLoader.discover(".", "testcase.py")
    #     for case in all_case:
    #         mysuit.addTest(case)
    #     unittest.TextTestRunner(verbosity=2).run(mysuit)
        with open('report.html', 'wb') as f:
            HTMLTestRunner(
                stream=f,
                title='测试报告',
                description='第一个测试报告',
                verbosity=2
            ).run(my_suit)


if __name__ == '__main__':
    unittest.main()






