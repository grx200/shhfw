import logging
from common.common_fun import Common
import unittest
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
import ddt
from businessView_app.bookingView import BookingView
from businessView_app.loginView_app import LoginView
from businessView_app.applyDemand import xuqiu
from common.myunit_app_login import StartEnd
from common.excel_read import ExcelUtil
file = '../data/demand.xls'
excel = ExcelUtil(file,"Sheet1")
@ddt.ddt
class TestAppDemand(StartEnd):
    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')
    @ddt.data(*excel.next())
    def test_Xuqiu(self,data):
        try:
            logging.info('======test_submit_demand=====')
            l=LoginView(self.driver)
            # data = l.get_csv_data(self.csv_file, 1)
            l.login_action("17708179510","123456")
            # self.assertTrue(l.check_loginStatus())
            a = xuqiu(self.driver)
            a.xuqiu(data['需求类型'],data['需求标题'])
            self.assertTrue(a.check_xuqiuStatus())
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