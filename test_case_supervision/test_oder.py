import logging
import unittest
from common.common_fun import Common
import time
from businessView_business.processingOder import processingOder
from common.myunit_supervision import StartEnd
import ddt
from common.desired_caps_supervision import open_browser
from businessView_business.loginView import LoginView as LoginView_fw
from businessView_supervision.add_order_View import addOder
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from businessView_supervision.loginView_zf import LoginView_jg as LoginView_zf
from businessView_business.demand import demand
from common.excel_read import ExcelUtil

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
            l=LoginView_zf(self.driver)
            # data = l.get_csv_data(self.csv_file, 1)
            l.login_action('admin','123456')
            l.check_loginStatus()
            time.sleep(3)
            b = addOder(self.driver)
            b.addOder(data['订单类型'],data['服务类型'],data['订购人姓名'],number)
            self.assertTrue(b.check_add_order_action())
            self.driver.quit()
            c = LoginView_fw(self.driver)
            c.login_action('17708179512','qq2883595')
            c.check_loginStatus()
            time.sleep(3)
            d = processingOder(self.driver)
            d.processing_order(data['订单类型'],data['订单编号'])
            d.processing_servering_order(data['订单编号'])
            self.assertTrue(d.check_processing_servering_order_status())
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
