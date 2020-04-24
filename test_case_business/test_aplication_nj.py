from common.myunit_business import StartEnd
from common.desired_caps_business import open_browser
from common.common_fun import Common
from businessView_business.loginView import LoginView
from businessView_business.applicationView import ApplicationView
import unittest
import logging
from businessView_business.loginView import LoginView
import ddt,time
from common.excel_read import ExcelUtil
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ErrorInResponseException
file = '../data/application.xls'
excel = ExcelUtil(file,"Sheet1")
@ddt.ddt
class TestApplication(StartEnd):
    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')
    @ddt.data(*excel.next())
    def test_add_application(self,data):
        try:
            l=LoginView(self.driver)
            l.login_action('ht_01','qq2883595')
            time.sleep(3)
            logging.info('======test_add_application======')
            a=ApplicationView(self.driver)
            a.add_application_action_nj(data['编号'],data['服务名称'],data['服务类型'],data['服务单价'],data['服务单位'],data['服务图片'],data['服务区域'])
            self.assertTrue(a.check_application_action_nj())
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