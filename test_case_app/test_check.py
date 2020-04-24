import logging
import unittest
import ddt,time
from businessView_app.bookingView import BookingView
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from businessView_app.loginView_app import LoginView
from businessView_app.applyDemand import xuqiu
from common.myunit_app_login import StartEnd
from businessView_app.checkOder import  CheckOrder
from common.excel_read import ExcelUtil
from common.common_fun import Common
file = '../data/demand.xls'
excel = ExcelUtil(file,"Sheet1")
@ddt.ddt
class TestCheck(StartEnd):
    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')
    @ddt.data(*excel.next())
    def testCheck(self,data):
        try:
            logging.info('======test_check=====')
            l=LoginView(self.driver)
            # data = l.get_csv_data(self.csv_file, 1)

            l.login_action('17708179510','123456')
            time.sleep(2)
            a = CheckOrder(self.driver)
            a.checkorder(data['需求类型'])
            self.assertTrue(a.check_check_order_Status())
            self.driver.quit()
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


if __name__ == "__main__":
    unittest.main()