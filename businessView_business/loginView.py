from config.log import logger
import time
from common.common_fun import Common,NoSuchElementException
from common.desired_caps_business import open_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
class LoginView(Common):
    username_type=(By.ID,'username')
    password_type=(By.ID,'password')
    loginBtn=(By.ID,'login-submit')
    loginCheck=(By.CLASS_NAME,'menuBox')
    userBtn=()
    logoutBtn=()
    def login_action(self,username,password):
        logger.info('============login_action==============')
        logger.info('username is:%s' %username)
        self.driver.find_element(*self.username_type).send_keys(username)
        logger.info('password is:%s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)
        logger.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logger.info('login finished!')
    def check_loginStatus(self):
        logger.info('====check_loginStatus======')
        time.sleep(2)
        try:
            element = self.driver.find_element(*self.loginCheck)
        except NoSuchElementException:
            logger.error('login Fail!')
            self.getScreenShot('login')
            return False
        else:
            logger.info('login success!')
            return True
if __name__ == '__main__':
    driver=open_browser()
    l=LoginView(driver)
    l.login_action('admin','123456')
    l.check_loginStatus()