import ddt
import time
from common.common_fun import Common
from common.excel_read import ExcelUtil
from common.myunit_supervision import StartEnd
from common.desired_caps_supervision import open_browser
from businessView_supervision.loginView_zf import LoginView_jg
from businessView_supervision.add_order_View import addOder
import unittest
import logging
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
file = '../data/processingorder.xlsx'
excel = ExcelUtil(file,"Sheet1")
@ddt.ddt
class TestAddOder(StartEnd):
    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')
    @ddt.data(*excel.next())
    def testAddOrder(self,data):
        try:
            logging.info('======test_add_order=====')

            l=LoginView_jg(self.driver)
            # data = l.get_csv_data(self.csv_file, 1)
            l.login_action('admin','123456')
            l.check_loginStatus()
            time.sleep(3)
            b = addOder(self.driver)
            b.addOder(data['订单类型'],data['服务类型'],data['订购人姓名'],data['订购人账号'])
            self.assertTrue(b.check_add_order_action())
            b.get_order_number(data['订单类型'])
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
