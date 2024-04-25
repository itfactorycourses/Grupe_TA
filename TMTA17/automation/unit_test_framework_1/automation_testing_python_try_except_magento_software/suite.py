import unittest
import HtmlTestRunner

from test_login import Test_Login
from test_search import Magento_search


class TestSuite(unittest.TestCase):

    def test_suite(self):
        # am creat un obiect instantiat din clasa TestSuite din libraira unittest
        test_list = unittest.TestSuite()
        test_list.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Magento_search),
                            unittest.defaultTestLoader.loadTestsFromTestCase(Test_Login)
                            ])

        # am instantiat un obiect numit runner din clasa HTMLTestRunner din libraria HtmlTestRunner
        runner = HtmlTestRunner.HTMLTestRunner \
                (
                combine_reports=True,  # daca rulam mai multe clase de test va genera un singur raport pentru toate,
                # nu cate un raport pentru fiecare clasa de test
                report_title="Test_execution_Report",
                report_name="Test results"
            	)

        # am apelat metoda run prin intermediul obiectului runner instantiat din clasa HTMLTestRunner
        runner.run(test_list)
