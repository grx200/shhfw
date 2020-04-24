from config.log import logger
import random
import time
from xlutils.copy import copy
import xlwt,xlrd
from common.excel_read import ExcelUtil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from businessView_app.loginView_app import LoginView
from common.common_fun import Common,NoSuchElementException
from common.desired_caps_app import appium_desired
######申请商家#######
class applicationProvider(Common):
    ##申请人信息
    applyBtn=(By.XPATH,'//android.widget.TextView[@text="申请加入农业社会化商家圈"]')
    name=(By.XPATH,'//android.widget.EditText[@text="（必填）申请人姓名"]')
    document_type=(By.XPATH,'//android.widget.TextView[@text="（必填）申请人证件类型"]')
    document_number=(By.XPATH,'//android.widget.EditText[@text="（必填）申请人证件号码"]')
    phone1=(By.XPATH,'//android.widget.EditText[@text="（必填）申请人联系方式"]')
    email1=(By.XPATH,'//android.widget.EditText[@text="（必填）申请人电子邮箱地址（用于审核结果通知）"]')
    #####组织信息
    server_type=(By.XPATH,'//android.widget.TextView[@text="（必填）服务商类型"]')
    server_number=(By.XPATH,'//android.widget.EditText[@text="（必填）服务主体机构编码"]')
    server_name=(By.XPATH,'//android.widget.EditText[@text="（必填）服务组织名称"]')
    server_phone=(By.XPATH,'//android.widget.EditText[@text="（必填）服务组织联系方式"]')
    name2 = (By.XPATH,'//android.widget.EditText[@text="（必填）法人名称"]')
    phone2 = (By.XPATH,'//android.widget.EditText[@text="（必填）法人联系方式"]')
    document_type2 = (By.XPATH,'//android.widget.TextView[@text="（必填）法人证件类型"]')

    document_number2=(By.XPATH,'//android.widget.EditText[@text="（必填）法人证件号码"]')
    email12=(By.XPATH,'//android.widget.EditText[@text="（必填）法人电子邮箱地址"]')
    area=(By.XPATH,'//android.widget.TextView[@text="（必填）所在区域"]')
    adress=(By.XPATH,'//android.widget.EditText[@text="（必填）公司地址"]')
    sure=(By.XPATH,'//android.widget.TextView[@text="已查看并同意  仪陇县农业服务管理协议]')
    nextBtn=(By.XPATH,'//android.widget.Button[@text="下一步]')
    #####第二步
    def application_provider(self):
        self.driver.find_element(*self.applyBtn).click()
        self.driver.find_element(*self.name).send_keys('11')
        self.driver.find_element(*self.document_type).click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="护照"]').click()
        self.driver.find_element(*self.document_number).send_keys('11')
        self.driver.find_element(*self.phone1).send_keys('11')
        self.driver.find_element(*self.email1).send_keys('11')
        self.driver.find_element(*self.server_type).click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="农业企业"]').click()
        self.driver.find_element(*self.server_name).send_keys('11')
        self.driver.find_element(*self.server_phone).send_keys('11')

        self.driver.find_element(*self.name2).send_keys('11')
        self.driver.find_element(*self.phone2).send_keys('11')
        self.driver.find_element(*self.document_type2).click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="护照"]').click()
        self.driver.find_element(*self.document_number2).send_keys('11')
        self.driver.find_element(*self.email12).send_keys('11')
        self.driver.find_element(*self.area).click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="山东省"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="德州市"]').click()
        self.driver.find_element_by_xpath('//android.widget.Button[@text="确定"]').click()
        self.driver.find_element(*self.adress).send_keys('11')
        self.driver.find_element(*self.sure).send_keys('11')
        self.driver.find_element(*self.nextBtn).click()


if __name__ == "__main__":
    driver=appium_desired()
    l=LoginView(driver)
    l.login_action('17708179510',123456)
    b = applicationProvider(driver)
    b.application_provider()
