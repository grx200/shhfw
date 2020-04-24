import logging
import unittest
import time
from common.common_fun import Common
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from common.myunit_business import StartEnd
import ddt
from common.desired_caps_business import open_browser
from businessView_business.loginView import LoginView
from businessView_business.resourceManagement import resource_management
from common.excel_read import ExcelUtil
########添加人员测试用例
file = '../data/processingorder.xlsx'
excel = ExcelUtil(file,"Sheet1")
@ddt.ddt
class TestprocessingDemand(StartEnd):
    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')

    @ddt.data(*excel.next())
    def testAddPerson(self,data):
        try:
            l=LoginView(self.driver)
            l.login_action('17708179512','qq2883595')
            time.sleep(3)
            a = resource_management(self.driver)
            a.addPerson()
            self.assertTrue(True)
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