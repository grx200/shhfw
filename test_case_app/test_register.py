import logging
import unittest
import ddt
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from businessView_app.bookingView import BookingView
from businessView_app.registerView import RegisterView
from common.myunit_app_login import StartEnd
from common.excel_read import ExcelUtil
from common.common_fun import Common
file = '../data/APPaccount.xlsx'
excel = ExcelUtil(file,"register")
@ddt.ddt
class TestRegister(StartEnd):
    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')
    @ddt.data(*excel.next())
    def testLogin(self,data):
        try:
            logging.info('======test_register=====')
            l=RegisterView(self.driver)
            # data = l.get_csv_data(self.csv_file, 1)
            # print(data['account'],data['password'])
            l.register_action(data['手机号'],data['密码'],data['确认密码'],data['姓名'],data['证件类型'],data['证件号码'],
                              data['所在区域'],data['常用服务地址'])
            self.assertTrue(l.check_registerStatus())
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