from config.log import logger
import time
from common.common_fun import Common,NoSuchElementException
from common.desired_caps_app import appium_desired
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class LoginView(Common):
    # '//android.widget.EditText[@text="注册手机号"]'
    username_type=(By.XPATH,'//android.widget.EditText[@text="注册手机号"]')
    password_type=(By.CLASS_NAME,'android.widget.EditText')
    loginBtn=(By.CLASS_NAME,'android.widget.Button')
    loginCheck=(By.XPATH,'//android.widget.TextView[@text="农机服务"]')
    def login_action(self,username,password):

        logger.info("========select region=========")
        self.add_img()
        self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[4].click()
        self.driver.implicitly_wait(20)
        self.add_img()
        logger.info('============login_action==============')
        ####到时记得删了
        # self.driver.find_element_by_id("android:id/button2").click()
        # time.sleep(2)
        # self.driver.find_element_by_id("android:id/button2").click()
        ######

        self.driver.find_elements_by_android_uiautomator("new UiSelector().text(\"我的\")")[0].click()

        logger.info('username is:%s' %username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logger.info('password is:%s'%password)
        self.driver.find_elements(*self.password_type)[1].send_keys(password)

        logger.info('click loginBtn')

        self.driver.find_element(*self.loginBtn).click()
        logger.info('login finished!')
    def check_loginStatus(self):
        logger.info('====check_loginStatus======')
        try:
            driver = self.driver
            time.sleep(4)
            element = driver.find_element(*self.loginCheck)
        except NoSuchElementException:
            logger.error('login Fail!')
            self.getScreenShot('login fail')
            return False
        else:
            logger.info('login success!')
            return True
if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    l.login_action('17708179510',123456)
    l.check_loginStatus()