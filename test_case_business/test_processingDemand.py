import logging
import unittest
from common.common_fun import Common
import time

from common.myunit_business import StartEnd
import ddt
from common.desired_caps_business import open_browser
from businessView_business.loginView import LoginView
from businessView_business.demand import demand
from common.excel_read import ExcelUtil
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
file = '../data/demand.xls'
excel = ExcelUtil(file,"Sheet1")
@ddt.ddt
class TestprocessingDemand(StartEnd):
    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')

    @ddt.data(*excel.next())
    def testProcessingDemand(self,data):
        try:
            self.driver.implicitly_wait(20)
            l=LoginView(self.driver)
            l.login_action('17708179512','qq2883595')
            time.sleep(3)
            a = demand(self.driver)
            a.xuqiu(data["需求类型"],data['需求标题'],data['编号'])
            self.assertTrue(a.check_xuqiu_action())
            a.get_order_number(data["需求类型"],data['编号'])
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





if __name__ == '__main__':

    unittest.main()