import ddt
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from common.excel_read import ExcelUtil
from common.myunit_business import StartEnd
from common.desired_caps_business import open_browser
from businessView_business.loginView import LoginView
import unittest
import logging
from common.common_fun import Common
@ddt.ddt
class TestLogin(StartEnd):

    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')
    def testLogin(self):
        try:
            logging.info('======test_login=====')
            l=LoginView(self.driver)
            # data = l.get_csv_data(self.csv_file, 1)
            l.login_action('admin','123456')
            self.assertTrue(l.check_loginStatus())
        except NoSuchElementException:

            file_name = "no_such_element"
            b = Common(self.driver)
            b.getScreenShot(file_name)
            self.assertTrue(False)
            raise

        except ElementNotVisibleException:

            file_name = "element_not_visible"
            b = Common(self.driver)
            b.getScreenShot(file_name)
            self.assertTrue(False)
            raise


if __name__ == '__main__':
    unittest.main()
