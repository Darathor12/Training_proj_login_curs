import unittest
import HtmlTestRunner

from full_test_login import LoginTest


class TestSuite(unittest.TestCase):
    def test_suite(self):
        tests_suite = unittest.TestSuite()
        # tests_suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(Test),
        #                       unittest.defaultTestLoader.loadTestsFromTestCase(TestKeys)])
        tests_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(LoginTest))
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True,
                                               report_title="TestReport",
                                               report_name="Fulltest")
        runner.run(tests_suite)
