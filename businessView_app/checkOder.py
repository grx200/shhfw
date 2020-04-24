
from common.desired_caps_app import appium_desired
from selenium.webdriver.support.ui import WebDriverWait
from businessView_app.loginView_app import LoginView
import logging,os
import time
import sys,random
from businessView_business.loginView import LoginView as LoginView_fw
from businessView_supervision.loginView_zf import LoginView_jg
from common.common_fun import Common,NoSuchElementException
from businessView_supervision.add_order_View import addOder
from common.desired_caps_business import open_browser
from common.desired_caps_supervision import open_browser as open_browser_jg
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from businessView_business.processingOder import processingOder
########验收订单########
class CheckOrder(Common):
    # '//android.widget.EditText[@text="注册手机号"]'
    dpjBtn=(By.XPATH,'//android.widget.TextView[@text="待评价"]')
    dshBth=(By.XPATH,'//android.widget.TextView[@text="待收货"]')
    nzBtn=(By.XPATH,'//android.widget.TextView[@text="农资采购"]')
    nz_checkBtn=(By.XPATH,'//android.widget.TextView[@text="验收农资"]')
    nj_checkBtn=(By.XPATH,'//android.widget.TextView[@text="验收评价"]')
    check_stustas_Btn=(By.XPATH,'//android.widget.TextView[@text="首页"]')

    plArea=(By.XPATH,'//android.widget.EditText[@text="留下您宝贵评价与建议，我们会慢慢改善哦！"]')

    xjpj=(By.CLASS_NAME,'android.widget.ImageView')
    yfysBtn=(By.XPATH,'//android.widget.Button[@text="服务验收"]')
    nzysBtn=(By.XPATH,"//android.widget.Button[@text='农资验收']")


    def checkorder(self,type):
        if type == "找服务":
            logging.info("==start check order===")
            time.sleep(6)
            self.driver.find_element(*self.dpjBtn).click()
            time.sleep(3)
            self.driver.find_element(*self.dpjBtn).click()
            time.sleep(8)
            element = self.driver.find_elements(*self.nj_checkBtn)
            element[0].click()
            self.driver.find_elements(*self.xjpj)[3].click()
            self.driver.find_element(*self.plArea).send_keys("测试")
            self.driver.find_element(*self.yfysBtn).click()
            logging.info("==start check finish===")

        else:
            logging.info("==start check order===")
            time.sleep(5)
            self.driver.find_element(*self.nzBtn).click()
            time.sleep(3)
            self.driver.find_element(*self.nzBtn).click()
            time.sleep(3)
            self.driver.find_element(*self.dshBth).click()
            time.sleep(5)
            # self.driver.find_element(*self.dshBth).click()
            time.sleep(5)
            element = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
            element1 = element[0].find_element_by_class_name("android.widget.LinearLayout")
            element1.find_element(*self.nz_checkBtn).click()
            time.sleep(1)

            self.driver.find_elements(*self.xjpj)[3].click()
            self.driver.find_element(*self.plArea).send_keys("测试")
            self.driver.find_element(*self.nzysBtn).click()
            logging.info("==start check finish===")
    def check_check_order_Status(self):
        logging.info('====check_check_order_Status======')
        try:
            driver = self.driver
            time.sleep(4)
            element = driver.find_element(*self.check_stustas_Btn)
        except NoSuchElementException:
            logging.error('check order Fail!')
            self.getScreenShot('check order fail')
            return False
        else:
            logging.info('check order success!')
            return True





if __name__ == '__main__':

    # driver_zf=open_browser_jg()
    # d=LoginView_jg(driver_zf)
    # d.login_action('admin','123456')
    # a = addOder(driver_zf)
    # a.addOder("农机订单","测试服务-耕地","测试","17708179510")
    # a.check_add_order_action()
    # ordernumber = a.get_order_number("农机订单")
    # driver_zf.quit()
    # driver = open_browser()
    # b= LoginView_fw(driver)
    # b.login_action("17708179512","qq2883595")
    # c= processingOder(driver)
    # c.processing_order('农机订单',ordernumber)
    # c.check_processing_waiting_server_order_status()
    # c.processing_servering_order('农机订单',ordernumber)
    # c.check_processing_servering_order_status()
    # driver.quit()

    driver=appium_desired()
    l=LoginView(driver)
    l.login_action('17708179510',123456)
    l.check_loginStatus()
    a= CheckOrder(driver)
    a.checkorder("找农资")
    a.check_check_order_Status()
    # a = xuqiu(driver)
    # a.xuqiu("找农资","测试")