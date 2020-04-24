import logging
from common.common_fun import Common,NoSuchElementException
from common.desired_caps_supervision import open_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class LoginView_jg(Common):
    username_type=(By.ID,'username')
    password_type=(By.ID,'password')
    loginBtn=(By.ID,'login-submit')
    loginCheck=(By.CLASS_NAME,'menuBox')
    userBtn=()
    logoutBtn=()
    def login_action(self,username,password):

        logging.info('============login_action==============')
        logging.info('username is:%s' %username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('password is:%s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished!')

    def check_loginStatus(self):
        logging.info('====check_loginStatus======')
        try:
            driver = self.driver
            element = WebDriverWait(driver, 4).until(lambda driver : driver.find_element(*self.loginCheck))
        except NoSuchElementException:
            logging.error('login Fail!')
            self.getScreenShot('login fail')
            return False
        else:
            logging.info('login success!')
            return True

    def logout_action(self):
        logging.info('=====logout_action======')
        self.driver.find_element(*self.userBtn).click()
        self.driver.find_element(*self.logoutBtn).click()




if __name__ == '__main__':
    driver=open_browser()
    l=LoginView(driver)
    l.login_action('admin','123456')
    l.check_loginStatus()