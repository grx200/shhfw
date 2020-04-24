import logging,os
import time
import xlrd
from xlutils.copy import copy
from businessView_business.loginView import LoginView
from common.common_fun import Common,NoSuchElementException
from common.desired_caps_business import open_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
######处理需求####
class demand(Common):
    xuqiuBtn=(By.XPATH,"/html/body/div[1]/div[1]/div/ul[1]/li[5]/div[1]/span[1]")
    typeSelect=(By.XPATH,"//span[2]/div/div/div/span")
    nongziSelect=(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div[1]/div/div[2]/span[2]/div/div[2]/ul[2]/li[2]")
    search = (By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div[1]/div/div[1]/div/input")
    qyBtn = (By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[9]/div/div/span[4]')
    selectBtn1=(By.XPATH,"/html/body/div[17]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/form/div[2]/div/p[1]/div/div/button/span")
    selectBtn2=(By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div/span")
    nf_selectBtn1=(By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[1]/div[2]/button/span")
    nf_selectBtn2=(By.XPATH,"/html/body/div[15]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[8]/div/div/span")
    tjBtn = (By.XPATH,"/html/body/div[17]/div[2]/div/div/div[3]/div/button[2]")
    nf_tjBtn = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[3]/div/button[2]")
    nav = (By.CLASS_NAME,"ivu-message-custom-content ivu-message-success")

    fwzx = (By.XPATH,"/html/body/div[1]/div[1]/div/ul[1]/li[3]/div[1]/span[1]")
    fwzx_nzcg=(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[3]")


    def xuqiu(self,type,title,nrow):
        # file = os.path.abspath(os.path.join(os.getcwd(), "../.."))
        # picture_file = file+ "\shhfw_test\data\%s"%picture
        logging.info('------processing demand start-------' )
        workbook = xlrd.open_workbook('../data/demand.xls')
        excel =copy(workbook)
        table = excel.get_sheet(0)
        table.write(int(nrow),4,' ')
        excel.save('../data/demand.xls')
        logging.info('-----clean excel finished------')
        self.driver.find_element(*self.xuqiuBtn).click()
        time.sleep(2)
        if type == "找农资":
            self.find_element(*self.typeSelect).click()
            self.find_element(*self.nongziSelect).click()
        else:
            pass
        time.sleep(2)
        self.driver.find_element(*self.search).send_keys(title)
        self.driver.find_element(*self.search).send_keys(Keys.ENTER)
        time.sleep(2.5)
        try:
            element = self.driver.find_element(*self.qyBtn)
        except NoSuchElementException:
            logging.error("processing demand failed! There is no demand! ")

            self.getScreenShot("processing demand failed!")
            pass
        else:
            logging.info("search demand success!")
            element.click()
            time.sleep(1)
            if type == "找农资":
                time.sleep(1)
                self.driver.find_element(*self.selectBtn1).click()
                time.sleep(1)
                self.driver.find_element(*self.selectBtn2).click()
                time.sleep(1)
                self.driver.find_element(*self.tjBtn).click()
                time.sleep(1)
            else:
                time.sleep(1)
                self.driver.find_element(*self.nf_selectBtn1).click()
                time.sleep(1)
                self.driver.find_element(*self.nf_selectBtn2).click()
                time.sleep(1)
                self.driver.find_element(*self.nf_tjBtn).click()
                time.sleep(1)
    def get_order_number(self,type,nrow):
            time.sleep(1)
            self.driver.find_element(*self.fwzx).click()
            time.sleep(3.5)
            if type=="找农资":
                self.driver.find_element(*self.fwzx_nzcg).click()
                time.sleep(1.5)
                td= self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]")
                OrderNumber = td.text
                self.writeExcell(excelPath='../data/demand.xls',sheet_index=0,nrow=nrow,col=4,data=OrderNumber)
                logging.info('-----write excel finished------')
            else:

                td = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]") ##获取订单编号td元素
                OrderNumber = td.text ###获取订单编号
                self.writeExcell(excelPath='../data/demand.xls',sheet_index=0,nrow=nrow,col=4,data=OrderNumber)
                logging.info('-----write excel finished------')
            logging.info('-----order phone number is %s------'%str(OrderNumber))
    def check_xuqiu_action(self):
        logging.info('====check_demand_action======')
        try:
            time.sleep(4.5)
            element = self.driver.find_element(*self.nav)
        except NoSuchElementException:
            logging.info('processing demand success!')
            return True
        else:
            logging.error('processing demand Fail!')
            self.getScreenShot('processing demand fail')
            return False

if __name__ == '__main__':
    driver=open_browser()
    l=LoginView(driver)
    l.login_action('17708179512','qq2883595')
    l.check_loginStatus()
    time.sleep(4)
    a=demand(driver)
    # a.signing(111,513701199510265833,'2019-05-11',"update_test.png")
    # a.xuqiu("找农资","来个化肥")
    # a.check_application_action()
    # a.check_xuqiu_action()
    a.get_order_number("找农资")
    driver.close()
