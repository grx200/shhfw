import logging
import unittest
import ddt
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from businessView_app.bookingView import BookingView
from businessView_app.loginView_app import LoginView
from common.myunit_app_login import StartEnd
from common.excel_read import ExcelUtil
from common.common_fun import Common
file = '../data/APPaccount.xlsx'
excel = ExcelUtil(file,"Sheet1")
@ddt.ddt
class TestLogin(StartEnd):
    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')
    @ddt.data(*excel.next())
    def testLogin(self,data):
        try:
            logging.info('======test_login=====')
            l=LoginView(self.driver)
            # data = l.get_csv_data(self.csv_file, 1)
            print(data['account'],data['password'])
            l.login_action(data['account'],data['password'])
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
