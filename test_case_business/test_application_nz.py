from common.myunit_business import StartEnd
from common.desired_caps_business import open_browser
from businessView_business.loginView import LoginView
from businessView_business.applicationView import ApplicationView
import unittest
import logging
from common.common_fun import Common
from businessView_business.loginView import LoginView
import ddt,time
from common.excel_read import ExcelUtil
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
file = '../data/application.xls'
excel = ExcelUtil(file,"Sheet2")
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
            a.add_application_action_nz(data['产品名称'],data['服务类别'],data['产品单价'],data['价格单位'],data['服务图片'],data['生产厂家'],data['产品规格'],data['产品编码'],data['产品品牌'],data['其他参数'],data['描述内容'])
            self.assertTrue(a.check_application_action_nz())
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