import logging,os
import time
import xlwt,xlrd
import sys,random
from copy import copy
from businessView_supervision.loginView_zf import LoginView_jg
from common.common_fun import Common,NoSuchElementException
from common.desired_caps_supervision import open_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
###处理服务申请######
class ProcessingApplication(Common):
    fwzx = (By.XPATH,"/html/body/div[1]/div[1]/div/ul[1]/li[3]/div/span[1]")
    fwsh = (By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[1]/div/ul/li[2]/span[1]")
    search = (By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div/div[4]/input")
    search_btn = (By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div/div[4]/i")
    cl_btn = (By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/table/tbody/tr/td[8]/div/div/span[1]")
    shyj =(By.XPATH,"/html/body/div[11]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/form/div[2]/div/div/div/div/textarea")
    pass_btn = (By.XPATH,"/html/body/div[11]/div[2]/div/div/div[3]/div/button[3]")
    no_pass_btn = (By.XPATH,"/html/body/div[11]/div[2]/div/div/div[3]/div/button[2]")


    def processing_application(self,application_num,whether_to_pass):
        logging.info("====start processing application=====")
        self.driver.find_element(*self.fwzx).click()
        self.driver.find_element(*self.fwsh).click()
        self.driver.find_element(*self.search).send_keys(application_num)
        self.driver.find_element(*self.search_btn).click()
        time.sleep(2)
        self.driver.find_element(*self.cl_btn).click()
        time.sleep(1.5)
        self.driver.find_element(*self.shyj).send_keys("意见")
        if whether_to_pass == "通过":
            self.driver.find_element(*self.pass_btn).click()
        else:
            self.driver.find_element(*self.no_pass_btn).click()

    def check_processing_application_action(self):
        logging.info('====check_processing_application_action======')
        try:
            element = self.driver.find_element(*self.search_btn)
        except NoSuchElementException:
            logging.error('processing application Fail!')
            self.getScreenShot('processing application Fail')
            return False

        else:
            logging.info('processing application success!')
            return True

if __name__ == '__main__':
    driver=open_browser()
    l=LoginView_jg(driver)
    l.login_action('admin','123456')
    a = ProcessingApplication(driver)
    a.processing_application("5735303712528090","通过")
