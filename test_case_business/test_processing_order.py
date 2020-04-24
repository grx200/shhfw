import logging
import unittest
from common.common_fun import Common
import time
from businessView_business.processingOder import processingOder
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from common.myunit_business import StartEnd
import ddt
from common.desired_caps_business import open_browser
from businessView_business.loginView import LoginView
from businessView_business.demand import demand
from common.excel_read import ExcelUtil

file = '../data/processingorder.xlsx'
excel = ExcelUtil(file,"Sheet1")
@ddt.ddt
class TestprocessingOder(StartEnd):
    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')


    @ddt.data(*excel.next())
    def testProcessingOder(self,data):
        try:
            data1 = []
            for line in open("../data/cs.txt","r+"):
                data1.append(line)

            l=LoginView(self.driver)
            l.login_action('17708179512','qq2883595')
            time.sleep(3)
            a = processingOder(self.driver)

            a.processing_order(data['订单类型'],data1[int(data['编号'])])
            # a.processing_order(data['订单类型'],data1)
            a.processing_servering_order(data["订单类型"],data['订单编号'])
            self.assertTrue(a.check_processing_servering_order_status())
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