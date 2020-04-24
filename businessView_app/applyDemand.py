import logging
import random

import time

from common.common_fun import Common,NoSuchElementException
from common.desired_caps_app import appium_desired
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from businessView_app.loginView_app import LoginView
#########提交需求##########
class xuqiu(Common):
    # '//android.widget.EditText[@text="注册手机号"]'
    nongzi=(By.XPATH,'//android.widget.TextView[@text="找农资"]')
    fuwu=(By.XPATH,'//android.widget.TextView[@text="找服务"]')
    # print(username_type)
    biaoti=(By.XPATH,'//android.widget.EditText[@text="（必填）标题"]')
    leixing = (By.XPATH,'//android.widget.TextView[@text="（必填）农资类型"]')
    nf_leixing=(By.XPATH,'//android.widget.TextView[@text="（必填）服务类型"]')
    guanjianzi = (By.XPATH,'//android.widget.EditText[@text="（必填）农资关键字（例：杀虫剂）"]')
    nf_guanjianzi = (By.XPATH,'//android.widget.EditText[@text="（必填）服务关键字（例：农田旋耕）"]')
    shuliang = (By.XPATH,'//android.widget.EditText[@text="（必填）采购数量"]')
    nf_shuliang = (By.XPATH,'//android.widget.EditText[@text="（必填）服务数量"]')
    danwei = (By.XPATH,'//android.widget.TextView[@text="单位"]')
    fbButton=(By.CLASS_NAME,"android.widget.Button")
    xuqiuCheck=(By.XPATH,'//android.widget.Button[@text="返回首页"]')
    def xuqiu(self,type,tietle):
        logging.info('============click_xuqiu_button==============')
        self.driver.find_elements_by_android_uiautomator("new UiSelector().text(\"首页\")")[0].click()
        if type == "找农资":
            self.driver.find_element(*self.nongzi).click()

        elif type=="找服务":
            self.driver.find_element(*self.fuwu).click()
            xqlx =["喷洒服务","播种服务","土地平整","耕地服务","农机租赁","土地托管","加工服务","收割服务"]
        else:
            logging.error("服务类型错误")
            self.getScreenShot("type error")
        logging.info('xuqiu tittle is:%s' %tietle)

        self.driver.find_element(*self.biaoti).send_keys(tietle)
        xqlx1 =random.randint(0,7)
        if type == "找农资":
            xqlx =["肥料","农药","饲料","兽药","种苗","种禽","种子","农机具"]
            logging.info("demand type is %s"%xqlx[xqlx1])
            self.driver.find_element(*self.leixing).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,'//android.widget.TextView[@text="%s"]'%(xqlx[xqlx1])).click()
            time.sleep(1)
            self.driver.find_element(*self.guanjianzi).send_keys("测试")
            self.driver.find_element(*self.shuliang).send_keys("50")
            self.driver.find_element(*self.danwei).click()
            time.sleep(1.5)
            self.driver.find_element(By.XPATH,'//android.widget.TextView[@text="个"]').click()
            time.sleep(1)
            logging.info('click tijiao Btn')
            self.driver.find_element(*self.fbButton).click()
            logging.info('zhaoxuqiu finished!')
        else:
            xqlx =["喷洒服务","播种服务","土地平整","耕地服务","农机租赁","土地托管","加工服务","收割服务"]
            logging.info("demand type is %s"%xqlx[xqlx1])
            self.driver.find_element(*self.nf_leixing).click()
            time.sleep(2)
            self.driver.find_element(By.XPATH,'//android.widget.TextView[@text="%s"]'%(xqlx[xqlx1])).click()
            time.sleep(1)
            self.driver.find_element(*self.nf_guanjianzi).send_keys("测试")
            self.driver.find_element(*self.nf_shuliang).send_keys("50")
            self.driver.find_element(*self.danwei).click()
            time.sleep(1.5)
            self.driver.find_element(By.XPATH,'//android.widget.TextView[@text="个"]').click()
            time.sleep(1)
            logging.info('click tijiao Btn')
            self.driver.find_element(*self.fbButton).click()
            logging.info('zhaoxuqiu finished!')

    def check_xuqiuStatus(self):
        logging.info('====check_xuqiuStatus======')
        try:
            driver = self.driver
            time.sleep(4)
            element = driver.find_element(*self.xuqiuCheck)
        except NoSuchElementException:
            logging.error('xuqiu Fail!')
            self.getScreenShot('xuqiu fail')
            return False
        else:
            logging.info('xuqiu success!')
            return True





if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    l.login_action('17708179510',123456)
    l.check_loginStatus()
    a = xuqiu(driver)
    a.xuqiu("找服务","测试")