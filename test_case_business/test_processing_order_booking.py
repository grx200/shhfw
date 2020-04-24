import logging
import unittest
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
import time
import xlrd
from businessView_business.processingOder_booking import processingOder
from common.myunit_business import StartEnd
import ddt
from common.desired_caps_business import open_browser
from businessView_business.loginView import LoginView
from common.excel_read import ExcelUtil
from common import common_fun
from common.common_fun import Common
from common.common_fun import Common
@ddt.ddt
class TestprocessingOder(StartEnd):
    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')
    file = '../data/booking.xls'

    excel = ExcelUtil(file,"Sheet1")
    @ddt.data(*excel.next())
    def testProcessingOder(self,data):
        try:
            self.yuqi = data['预期结果']
            da = ExcelUtil('../data/booking.xls','Sheet1').next()
            self.shiji = da[int(data['编号'])]['app新增订单结果']
            phone = da[int(data['编号'])-1]['随机电话(不要填写)']
            li1 = []
            if self.yuqi == 'ok' and self.shiji == 'ok':
                l = LoginView(self.driver)
                l.login_action('17708179512','qq2883595')
                l.check_loginStatus()
                time.sleep(3)
                a = processingOder(self.driver)
                a.processing_order_dfw(data['服务类型'],phone)
                a.processing_order(data['服务类型'],phone)
                # a.processing_order(data['订单类型'],data1)
                a.processing_servering_order(data["服务类型"],phone)
                result = a.check_processing_servering_order_status()
                if result == 'ok':
                    result = True
                else:
                    result = False
                self.assertTrue(result)
                self.driver.quit()
            else:
                self.assertTrue('False')
                logging.error('app新增订单，用例失败')


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