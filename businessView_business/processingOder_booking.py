import logging,os
import time

import sys,random

from businessView_business.loginView import LoginView
from businessView_supervision.loginView_zf import LoginView_jg
from common.common_fun import Common,NoSuchElementException
from businessView_supervision.add_order_View import addOder
from common.desired_caps_business import open_browser
from common.desired_caps_supervision import open_browser as open_browser_jg
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import xlrd
#######处理APP端新增的订单#######
class processingOder(Common):
    #待签约

    njclBtn_dfw=(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div[2]/table/tbody/tr/td[9]/div/div/span[1]")
    hetongBtn=(By.XPATH,"/html/body/div[27]/div[2]/div/div/div[2]/div/div[1]/ul/li[2]")
    htbh = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/form/div[7]/div/div/div/div/input")
    jsdate = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/form/div[13]/div/div/div/div/div[1]/div/input")
    zfType=(By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/form/div[22]/div/div/div/div/div/div/span")
    qdBtn=(By.XPATH,"/html/body/div[16]/div[2]/div/div/div[3]/div/button[2]")
    htxx = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[1]/ul/li[2]/span[1]")
    nzSelect1=(By.XPATH,"/html/body/div[33]/div[2]/div/div/div[2]/form/div[1]/div[2]/button")
    nzsearch =(By.XPATH,"/html/body/div[29]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/input")
    nzSelect2 =(By.XPATH,"/html/body/div[29]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div/span")
    nzUserSelect=(By.XPATH,"/html/body/div[33]/div[2]/div/div/div[2]/form/div[7]/div[1]/div/div/div/div[1]/div/input")
    nzQdBtn=(By.XPATH,"/html/body/div[33]/div[2]/div/div/div[3]/div/button[2]")
    htbhlist=[]

    #待处理
    zyglBtn = (By.XPATH,"/html/body/div[1]/div[2]/div/div[1]/div/div[3]/div[2]/span")
    fwzxBtn = (By.XPATH,"/html/body/div[1]/div[1]/div/ul[1]/li[3]/div")

    njfwBtn = (By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[1]/div/ul/li[1]/span[1]")
    nzcgBtn=(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[1]/div/ul/li[2]/span[1]")
    njsearch = (By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div/div/input")

    njclBtn = (By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div[2]/table/tbody/tr/td[9]/div/div/span[1]")
    # htxxBtn = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[1]/ul/li[2]/span[1]")
    # htbh = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/form/div[7]/div/div/div/div/input")
    # jsrq = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/form/div[13]/div/div/div/div[1]/div[1]/div/input")
    # zffs = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/form/div[22]/div/div/div/div/div/div/span")
    # fjzlBtn = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[1]/ul/li[3]/span[1]")
    # xzsjBtn = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div[1]/div[1]/div/div[2]/div/ul/li[2]/i")
    # scfjBtn = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div/input")
    # file = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    # picture_file = file+ "\shhfw_test\data\%s"%picture
    fpfwBtn=(By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[1]/ul/li[4]/span[1]")
    tjryBtn = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div[2]/div[1]/button")
    ryxz1 = (By.XPATH,"/html/body/div[37]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]")
    ryxz2 = (By.XPATH,"/html/body/div[38]/div[2]/div/div/div[3]/div/button[2]")
    fpnjBtn=(By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div[1]/ul/li[2]")
    tjnjBtn=(By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div[2]/div[2]/button")
    njxz1 = (By.XPATH,"/html/body/div[39]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/div/label/span/input")
    njxz2 = (By.XPATH,"/html/body/div[39]/div[2]/div/div/div[3]/div/button[2]")

    nzcl = (By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div[2]/table/tbody/tr/td[8]/div/div/span[1]")
    zfpsBtn=(By.XPATH,"/html/body/div[17]/div[2]/div/div/div[2]/div/div[1]/ul/li[2]/span[1]")
    psfs1= (By.XPATH,"/html/body/div[17]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/form/div[1]/div/div/div/div")
    psfs2 = (By.XPATH,"/html/body/div[38]/ul[2]/li[1]")
    psgs = (By.XPATH,"/html/body/div[17]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/form/div[2]/div/div/div/div/input")
    ydh = (By.XPATH,"/html/body/div[17]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/form/div[4]/div/div/div/div/input")
    zfxxBtn = (By.XPATH,"/html/body/div[17]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/div/div/div/div[3]")
    zffs1 = (By.XPATH,"/html/body/div[34]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[4]/form/div[1]/div/div/div/div/div/div/span")
    zffs2 = (By.XPATH,"/html/body/div[39]/ul[2]/li[1]")
    zfje=(By.XPATH,"/html/body/div[17]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[4]/form/div[2]/div/div/div/div/input")
    tjBtn= (By.XPATH,"/html/body/div[17]/div[2]/div/div/div[3]/div/button[2]")

    ####服务中
    njsearch_fwz=(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div/div[3]/input")
    fwzBtn = (By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div[1]/ul/li[2]")
    clBtn =(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div[2]/table/tbody/tr/td[9]/div/div/span[1]")
    fpfw =(By.XPATH,"/html/body/div[33]/div[2]/div/div/div[2]/div/div[1]/ul/li[4]/span[1]")
    fwsj = (By.XPATH,"/html/body/div[33]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div[2]/div[1]/div/div[1]/div[1]/div/button")
    njbh1 = (By.XPATH,"/html/body/div[32]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div/div[1]/div/span")
    njbh2 = (By.XPATH,"/html/body/div[32]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div/div[2]/ul[2]/li")
    tj = (By.XPATH,"/html/body/div[32]/div[2]/div/div/div[3]/div/button[2]/span")
    fwwc = (By.XPATH,"/html/body/div[33]/div[2]/div/div/div[3]/div/button[1]")

    def processing_order_dfw(self,type,phone):
        time.sleep(1.5)
        self.driver.find_element(*self.fwzxBtn).click()
        # file = '../data/booking.xlsx'
        # data = xlrd.open_workbook(file)
        # sheet = data.sheet_by_index(0)
        # nrows = sheet.nrows
        # ncols = sheet.ncols
        # li1 = []
        # for i in range(1, nrows):#第0行为表头
        #     alldata = sheet.row_values(i)#循环输出excel表中每一行，即所有数据
        #     result = alldata[0]#取出表中第二列数据
        #     li1.append(alldata[0])
        #
        # result_dic={}
        # for item_str in li1:
        #     if item_str not in result_dic:
        #         result_dic[item_str]=1
        #     else:
        #         result_dic[item_str]+=1
        #
        # print(result_dic)
        if type == "农资服务":
            pass

        else:
            logging.info("====start processing wait signed nongji order====")
            # if result_dic["农机服务"] <=20:
            time.sleep(1)
            self.driver.find_element(*self.njfwBtn).click()
            time.sleep(3)

            self.driver.find_element(*self.njsearch).send_keys(phone)
            self.driver.find_element(*self.njsearch).send_keys(Keys.ENTER)
            time.sleep(1)
            try:
                element = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]")


            except NoSuchElementException:
                logging.error("元素不存在")

                self.getScreenShot("processing order fail")
            else:
                pass
            time.sleep(2)
            element = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]")
            element.find_elements_by_class_name("textBtn")[0].click()
            time.sleep(1)
            self.driver.find_element(*self.htxx).click()
            time.sleep(1)
            randomNum = random.randint(100000000,999999999999999)
            self.driver.find_element(*self.htbh).send_keys(randomNum)
            self.driver.find_element(*self.jsdate).send_keys("2019-08-28")
            self.driver.find_element(*self.zfType).click()
            self.driver.find_element_by_xpath("/html/body/div[14]/ul[2]/li[1]").click()
            time.sleep(1)


            self.driver.find_element(*self.qdBtn).click()
            logging.info("procesing Waiting for signed order finish!")
            time.sleep(5)

    def processing_order(self,type,phone):
        # self.driver.find_element(*self.zyglBtn).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.fwzxBtn).click()
        time.sleep(2)
        if type == "农资服务":
            logging.info("====start processing wait server nongzi order====")
            self.driver.implicitly_wait(5)
            logging.info("====phone number is %s===="%phone)
            self.driver.find_element(*self.nzcgBtn).click()

            time.sleep(1.5)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div/div/input").send_keys(orderNumber)
            self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[2]/div/div/input").send_keys(Keys.ENTER)

            time.sleep(3)
            try:
                element = self.driver.find_element(*self.nzcl)
            except NoSuchElementException:
                logging.error("元素不存在")
                self.getScreenShot("processing order fail")
            else:
                element.click()
            time.sleep(3)
            self.driver.find_element(*self.zfpsBtn).click()
            time.sleep(3)
            self.driver.find_element(*self.psfs1).click()
            time.sleep(1)
            ul = self.driver.find_element_by_xpath("/html/body/div[37]/ul[2]")
            ul.find_elements_by_xpath('li')[0].click()
            time.sleep(1.5)
            self.driver.find_element(*self.psgs).send_keys("顺丰")
            self.driver.find_element(*self.ydh).send_keys("123456")
            self.driver.find_element(*self.zfxxBtn).click()
            time.sleep(1)
            self.driver.find_element_by_xpath("/html/body/div[17]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[4]/form/div[1]/div/div/div/div/div").click()
            time.sleep(1)
            ul2=self.driver.find_element_by_xpath("/html/body/div[38]/ul[2]")
            ul2.find_elements_by_xpath("li")[0].click()

            self.driver.find_element(*self.zfje).send_keys("123456")
            self.driver.find_element(*self.tjBtn).click()

        else:
            logging.info("====start processing wait server nongji order====")
            time.sleep(1)
            self.driver.find_element(*self.njfwBtn).click()



            time.sleep(3)
            try:
                element = self.driver.find_element(*self.njclBtn)
            except NoSuchElementException:
                logging.error("元素不存在")
                self.getScreenShot("processing order fail")
            else:
                element.click()
            time.sleep(2)
            self.driver.find_element(*self.fpfwBtn).click()
            time.sleep(2)
            self.driver.find_element(*self.tjryBtn).click()
            time.sleep(2)
            try:
                time.sleep(3)
                element2 = self.driver.find_element_by_xpath("/html/body/div[38]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]")
            except NoSuchElementException:
                logging.error("元素不存在")
                self.getScreenShot("processing order fail")
            else:
                element2.click()
            time.sleep(1)
            self.driver.find_element(*self.ryxz2).click()
            time.sleep(2)
            self.driver.find_element(*self.fpnjBtn).click()
            self.driver.implicitly_wait(10)
            self.driver.find_element(*self.tjnjBtn).click()
            time.sleep(1)
            self.driver.find_element(*self.njxz1).click()
            time.sleep(1.5)
            self.driver.find_element(*self.njxz2).click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath("/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr/td[4]/div/div/div[1]/div/span").click()
            self.driver.find_element_by_xpath("/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div[2]/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr/td[4]/div/div/div[2]/ul[2]/li").click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath("/html/body/div[16]/div[2]/div/div/div[3]/div/button[2]").click()
            logging.info("procesing Waiting for service order finish!")
            time.sleep(5)
    def processing_servering_order(self,type,orderNumber):
            logging.info("====start processing servering nongji order====")

            if type == "农机服务":
                self.driver.find_element(*self.fwzBtn).click()
                self.driver.implicitly_wait(5)
                self.driver.find_element(*self.njsearch_fwz).send_keys(orderNumber)
                self.driver.find_element(*self.njsearch_fwz).send_keys(Keys.ENTER)
                time.sleep(1)
                try:
                    time.sleep(1.5)
                    element = self.driver.find_element(*self.clBtn)
                except NoSuchElementException:
                    logging.error("元素不存在")
                    self.getScreenShot("processing order fail")
                else:
                    element.click()
                self.driver.implicitly_wait(5)
                self.driver.find_element(*self.fpfw).click()
                self.driver.implicitly_wait(5)
                self.driver.find_element(*self.fwsj).click()
                self.driver.implicitly_wait(2)
                self.driver.find_element(*self.njbh1).click()
                self.driver.find_element(*self.njbh2).click()
                time.sleep(1)
                self.driver.find_element(*self.tj).click()
                time.sleep(1)
                self.driver.find_element(*self.fwwc).click()
                logging.info("====processing servering nongji order finish====")
            else:
                pass
    def check_processing_waiting_server_order_status(self):
        logging.info('====check_processing_waiting_server_order_status_action======')
        try:
            time.sleep(3)
            element = self.driver.find_element(*self.zyglBtn)
        except NoSuchElementException:
            logging.error('processing order Fail!')
            self.getScreenShot('processing order fail')
            return False
        else:
            logging.info('processing oder Success!')
            return True

    def check_processing_servering_order_status(self):
        logging.info('====check_processing_ervering_order_status_action======')
        try:
            time.sleep(3)
            element = self.driver.find_element(*self.zyglBtn)

        #     备注一下：因为bool类型true和false无法比较 所以check方法的返回值该为字符串
        except NoSuchElementException:
            logging.error('processing order Fail!')
            self.getScreenShot('processing order fail')
            return 'ok'
        else:
            logging.info('processing order Success!')
            return 'ko'



if __name__ == '__main__':
    # driver_zf=open_browser_jg()
    # l=LoginView_jg(driver_zf)
    # l.login_action('admin','123456')
    # a = addOder(driver_zf)
    # a.addOder("农资订单","小麦种子","测试","17708179510")
    # a.check_add_order_action()
    # ordernumber = a.get_order_number("农资订单")
    # driver_zf.quit()
    driver = open_browser()
    b= LoginView(driver)
    b.login_action("17708179512","qq2883595")
    c= processingOder(driver)
    c.processing_order_dfw('农机订单','测试测试','15818658527')
    c.processing_order('测试测试',15818658527)
    c.check_processing_waiting_server_order_status()
    c.processing_servering_order('农机服务',15818658527)
    c.check_processing_servering_order_status()
    driver.quit()