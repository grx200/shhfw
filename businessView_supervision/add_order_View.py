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
##新增订单###
class addOder(Common):



    zyjgBtn=(By.XPATH,"/html/body/div[1]/div[2]/div/div[1]/div/div[3]/div[2]/span")
    fwzxBtn=(By.XPATH,"/html/body/div[1]/div[1]/div/ul[1]/li[3]/div/span[1]")
    njBtn=(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div[4]/i")
    nzBtn=(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div[5]")
    njSelect1=(By.XPATH,"/html/body/div[27]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/form/div[1]/div[2]/button/span")
    search =(By.XPATH,"/html/body/div[19]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/input")
    njSelect2=(By.XPATH,"/html/body/div[19]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[9]/div/div/span")
    yuyueSelect=(By.XPATH,u"(.//*[normalize-space(text()) and normalize-space(.)='预约信息'])[1]/following::i[1]")
    hetongBtn=(By.XPATH,"/html/body/div[27]/div[2]/div/div/div[2]/div/div[1]/ul/li[2]")
    htbh = (By.XPATH,"/html/body/div[27]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/form/div[7]/div/div/div/div/input")
    jsdate = (By.XPATH,"/html/body/div[27]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/form/div[13]/div/div/div/div[1]/div[1]/div/input")
    cost = (By.XPATH,"/html/body/div[27]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/form/div[21]/div/div/div/div/input")
    zfType=(By.XPATH,"/html/body/div[27]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/form/div[22]/div/div/div/div/div/div/span")
    qdBtn=(By.XPATH,"/html/body/div[27]/div[2]/div/div/div[3]/div/button[2]")

    nzSelect1=(By.XPATH,"/html/body/div[33]/div[2]/div/div/div[2]/form/div[1]/div[2]/button")
    nzsearch =(By.XPATH,"/html/body/div[29]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/input")
    nzSelect2 =(By.XPATH,"/html/body/div[29]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div/span")
    nzUserSelect=(By.XPATH,"/html/body/div[33]/div[2]/div/div/div[2]/form/div[7]/div[1]/div/div/div/div[1]/div/input")
    nzQdBtn=(By.XPATH,"/html/body/div[33]/div[2]/div/div/div[3]/div/button[2]")
    htbhlist=[]
    def addOder(self,fwtype,fwleixing,username,userphone):
        # file = os.path.abspath(os.path.join(os.getcwd(), "../.."))
        # picture_file = file+ "\shhfw_test\data\%s"%picture
        logging.info('------add order start-------' )
        time.sleep(6)
        self.driver.find_element(*self.zyjgBtn).click()
        time.sleep(6)
        self.driver.find_element(*self.fwzxBtn).click()
        time.sleep(3)
        if fwtype == "农资订单":
            logging.info("start add nongzi order")
            self.driver.implicitly_wait(10)
            self.driver.find_element(*self.nzBtn).click()
            self.driver.find_element(*self.nzSelect1).click()
            self.driver.find_element(*self.nzsearch).send_keys(fwleixing)
            self.driver.find_element(*self.nzsearch).send_keys(Keys.ENTER)
            time.sleep(2)
            self.driver.implicitly_wait(10)
            self.driver.find_element(*self.nzSelect2).click()
            logging.info("select customer is %s"%username)
            time.sleep(2)
            self.driver.find_element(*self.nzUserSelect).click()
            ul = self.driver.find_element_by_xpath('/html/body/div[33]/div[2]/div/div/div[2]/form/div[7]/div[1]/div/div/div/div[2]/ul[2]')
            lilist = ul.find_elements_by_xpath("li")

            user = username+" "+userphone
            print(user)
            for li in lilist:
                if li.text==user:
                    li.click()
                else:
                    pass
            self.driver.find_element_by_xpath("/html/body/div[33]/div[2]/div/div/div[3]/div/button[2]").click()
        elif fwtype=="农机订单":
            logging.info("===start add nongji oder===")
            self.driver.implicitly_wait(10)
            self.driver.find_element(*self.njBtn).click()
            self.driver.find_element(*self.njSelect1).click()
            self.driver.find_element(*self.search).send_keys(fwleixing)
            self.driver.find_element(*self.search).send_keys(Keys.ENTER)
            time.sleep(3)
            self.driver.find_element(*self.njSelect2).click()
            logging.info("select customer is %s"%username)
            time.sleep(2)
            self.driver.find_element(*self.yuyueSelect).click()
            ul = self.driver.find_element_by_xpath('/html/body/div[27]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/form/div[7]/div[1]/div/div/div/div[2]/ul[2]')
            lilist = ul.find_elements_by_xpath("li")

            user = username+" "+userphone
            print(user)
            for li in lilist:
                if li.text==user:
                    li.click()
                else:
                    pass
            self.driver.find_element(*self.hetongBtn).click()
            randomNum = random.randint(100000000,999999999999999)
            self.driver.find_element(*self.htbh).send_keys(randomNum)

            self.driver.find_element(*self.jsdate).send_keys("2019-07-28")
            self.driver.find_element(*self.zfType).click()
            self.driver.find_element_by_xpath("/html/body/div[25]/ul[2]/li[1]").click()
            self.driver.find_element_by_xpath("/html/body/div[27]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/form/div[10]/div/div/div/div[1]/div[2]/input").send_keys(8)
            self.driver.find_element(*self.qdBtn).click()


        else:
            logging.error("type error!!!")
            sys.exit()
    def get_order_number(self,fwtype):
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul[1]/li[4]/div[1]").click()
        time.sleep(3)
        if fwtype=="农机订单":
            td= self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/div/span")
            OrderNumber = td.text

            with open('../data/cs.txt','a+') as f:
                f.write(OrderNumber+'\n')
            return OrderNumber
        else:
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div/div[1]/div/div/div/div/div[3]").click()
            td = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/div/span")
            OrderNumber = td.text

            with open('../data/cs.txt','a+') as f:
                f.write(OrderNumber+'\n')
            return OrderNumber
    def check_add_order_action(self):
        logging.info('====check_add_order_action======')
        try:
            time.sleep(1)
            self.driver.implicitly_wait(10)
            element = self.driver.find_element(*self.fwzxBtn)
        except NoSuchElementException:
            logging.error('add order Fail!')
            self.getScreenShot('add order Fail')
            return False
        else:
            logging.info('add order success!')
            return True

if __name__ == '__main__':
    driver=open_browser()
    l=LoginView_jg(driver)
    l.login_action('admin','123456')
    a = addOder(driver)
    a.addOder("农资订单","小麦种子","测试","17708179510")
    a.check_add_order_action()
    a.get_order_number("农资订单")
    driver.quit()

