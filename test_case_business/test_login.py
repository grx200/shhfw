from common.myunit_business import StartEnd
from common.common_fun import Common
from common.desired_caps_business import open_browser
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from businessView_business.loginView import LoginView
import unittest
import logging,ddt
from common.common_fun import Common
@ddt.ddt
class TestLogin(StartEnd,Common):
    csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')
    def test_login_001(self):
        logging.info('======test_login_001=====')
        try:
            l=LoginView(self.driver)
            data = l.get_csv_data(self.csv_file, 1)
            # l.login_action(data[0],data[1])

            l.login_action(18888888888,"qq123456")
            self.assertTrue(l.check_loginStatus())
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
