import logging

import time

from common.common_fun import Common,NoSuchElementException
from common.desired_caps_app import appium_desired
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#########注册###########
class RegisterView(Common):
    # '//android.widget.EditText[@text="注册手机号"]'
    registerBtn = (By.XPATH,'//android.widget.Button[@text="注　册"]')
    phoneNumber = (By.XPATH,'//android.widget.EditText[@text="注册手机号"]')
    passwd1 = (By.XPATH,'//android.widget.EditText[@text="初始密码"]')
    passwd2 = (By.XPATH,'//android.widget.EditText[@text="确认密码"]')
    subjectType = (By.XPATH,'//android.widget.TextView[@text="主体类型"]')
    subjectType2 = (By.XPATH,'//android.widget.TextView[@text="农户"]')
    name = (By.XPATH,'//android.widget.EditText[@text="姓名"]')
    documentType = (By.XPATH,'//android.widget.TextView[@text="证件类型"]')
    documentType2 = (By.XPATH,'//android.widget.TextView[@text="军人证"]')
    documentNumber = (By.XPATH,'//android.widget.EditText[@text="证件号码"]')
    region = (By.XPATH,'//android.widget.TextView[@text="所在区域"]')
    region2 = (By.XPATH,'//android.widget.TextView[@text="山东省"]')
    region3 = (By.XPATH,'//android.widget.TextView[@text="德州市"]')
    region4 = (By.XPATH,'//android.widget.Button[@text="确定"]')
    address = (By.XPATH,'//android.widget.EditText[@text="常用服务地址"]')
    agreement = (By.XPATH,'//android.widget.TextView[@text="阅读并同意协议"]')
    submissionBtn = (By.XPATH,'//android.widget.Button[@text="提交注册"]')
    check = (By.XPATH,'//android.widget.Button[@text="进圈看看"]')

    def register_action(self,phone,password1,password2,name,documentType,documentNumber,region,address):
        logging.info("========select region=========")
        self.driver.find_elements(By.CLASS_NAME,"android.widget.ImageView")[4].click()
        self.driver.implicitly_wait(20)

        logging.info('============register_action==============')
        self.driver.find_element_by_id("android:id/button2").click()
        time.sleep(2)
        self.driver.find_element_by_id("android:id/button2").click()
        self.driver.find_elements_by_android_uiautomator("new UiSelector().text(\"我的\")")[0].click()
        self.driver.find_element(*self.registerBtn).click()
        self.driver.find_element(*self.phoneNumber).send_keys(phone)
        time.sleep(3)
        self.driver.find_element(*self.passwd1).send_keys(password1)
        self.driver.find_element(*self.passwd2).send_keys(password2)
        self.driver.find_element(*self.subjectType).click()
        self.driver.find_element(*self.subjectType2).click()
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.documentType).click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="%s"]'%documentType).click()
        self.driver.find_element(*self.documentNumber).send_keys(documentNumber)
        li1 = str(region).split("-")
        logging.info("------region is %s------"%region)
        if len(li1) <2:
            logging.error("区域不正确")
        elif len(li1) ==2:
            self.driver.find_element(*self.region).click()
            self.driver.find_element(*self.region2).click()
            self.driver.find_element(*self.region3).click()
            self.driver.find_element(*self.region4).click()
        elif len(li1) ==3:
            self.driver.find_element(*self.region).click()
            self.driver.find_element(*self.region2).click()
            self.driver.find_element(*self.region3).click()
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="%s"]'%li1[2]).click()
            self.driver.find_element(*self.region4).click()
        elif len(li1) ==4:
            self.driver.find_element(*self.region).click()
            self.driver.find_element(*self.region2).click()
            self.driver.find_element(*self.region3).click()
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="%s"]'%li1[2]).click()
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="%s"]'%li1[3]).click()
            self.driver.find_element(*self.region4).click()
        elif len(li1) ==5:
            self.driver.find_element(*self.region).click()
            self.driver.find_element(*self.region2).click()
            self.driver.find_element(*self.region3).click()
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="%s"]'%li1[2]).click()
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="%s"]'%li1[3]).click()
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="%s"]'%li1[4]).click()
            self.driver.find_element(*self.region4).click()
        else:
            self.driver.find_element(*self.region).click()
            self.driver.find_element(*self.region2).click()
            self.driver.find_element(*self.region3).click()
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="%s"]'%li1[2]).click()
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="%s"]'%li1[3]).click()
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="%s"]'%li1[4]).click()
            self.driver.find_element_by_xpath('//android.widget.TextView[@text="%s"]'%li1[5]).click()



        self.driver.find_element(*self.address).send_keys(address)
        self.driver.find_element(*self.agreement).click()
        self.driver.find_element(*self.submissionBtn).click()


        # logging.info('username is:%s' %username)
        # self.driver.find_element(*self.username_type).send_keys(username)
        #
        # logging.info('password is:%s'%password)
        # self.driver.find_elements(*self.password_type)[1].send_keys(password)
        #
        # logging.info('click loginBtn')
        # self.driver.find_element(*self.loginBtn).click()
        # logging.info('login finished!')

    def check_registerStatus(self):
        logging.info('====check_register_Status======')
        try:
            time.sleep(4)
            element = self.driver.find_element(*self.check)
        except NoSuchElementException:
            logging.error('regist Fail!')
            self.getScreenShot('regist fail')
            return False
        else:
            logging.info('regist success!')
            return True





if __name__ == '__main__':
    driver=appium_desired()
    l=RegisterView(driver)
    # l.register_action('17708179510',123456)
    l.check_registerStatus()