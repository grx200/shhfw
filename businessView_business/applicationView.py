import os
import random
import time
from xlutils.copy import copy
import xlrd,xlwt,logging
from config.log import logger
from selenium.common.exceptions import WebDriverException
from businessView_business.loginView import LoginView
from common.common_fun import Common,NoSuchElementException
from common.desired_caps_business import open_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#申请服务
class ApplicationView(Common):
    #农机服务
    fwxz = (By.XPATH,"/html/body/div[1]/div[1]/div/ul[1]/li[2]/div/span[1]")
    applicationBtn=(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div[1]/span")
    applicationName=(By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[1]/div/div/div/div/input")
    applicationNumber=(By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div/input")
    applicationType_1=(By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[3]/div/div/div/div/div/div/span")
    applicationType_2=(By.XPATH,"/html/body/div[29]/ul[2]")
    applicationCast=(By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[4]/div/div/div/div/div[2]/input")
    applicationUnit1=(By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[5]/div/div/div/div/div/div/span")
    applicationUnit2=(By.XPATH,"/html/body/div[30]/ul[2]")
    updateBtn=(By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[7]/div/div/div/div/div/div[1]/div/input")
    serviceArea_Btn=(By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[8]/div/div/div/div/div[1]/div[1]/input")
    serviceArea_1=(By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[8]/div/div/div/div/div[2]/div/span/span/ul")
    serviceArea_2=(By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[8]/div/div/div/div/div[2]/div/span/span/span/ul")
    serviceArea_add=(By.XPATH,"/html/body/div[22]/div[2]/div/div/div[2]/form/div[8]/div[2]/button")
    jxmc = (By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[9]/div/div/div/div/input")
    jxxh = (By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[10]/div/div/div/div/input")
    zyms = (By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[11]/div/div/div/div/textarea")
    bz = (By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[12]/div/div/div/div/textarea")
    msnr = (By.XPATH,"/html/body/div[31]/div[2]/div/div/div[2]/form/div[13]/div/div/div/div/div[2]/div[2]/div[1]")

    application_submit=(By.XPATH,"/html/body/div[31]/div[2]/div/div/div[3]/div/button[2]")
    #农资产品
    nzBtn =(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div[1]/div[2]/div/div[2]/span")
    addBtn = (By.XPATH,"/html/body/div[49]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/button")
    cpmc = (By.XPATH,"/html/body/div[45]/div[2]/div/div/div[2]/form/div[1]/div/div/div/div/input")
    fwlx1 = (By.XPATH,"/html/body/div[45]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div/div/div/span")
    fwlx2 = (By.XPATH,"/html/body/div[43]/ul[2]")
    cpdj = (By.XPATH,"/html/body/div[45]/div[2]/div/div/div[2]/form/div[3]/div/div/div/div/input")
    jgdw1 = (By.XPATH,"/html/body/div[45]/div[2]/div/div/div[2]/form/div[4]/div/div/div/div/div/div/span")
    jgdw2 = (By.XPATH,"/html/body/div[44]/ul[2]")
    update = (By.XPATH,"/html/body/div[45]/div[2]/div/div/div[2]/form/div[5]/div/div/div/div/div/div[1]/div/input")
    sccj = (By.XPATH,"/html/body/div[45]/div[2]/div/div/div[2]/form/div[6]/div/div/div/div/input")
    cpgg = (By.XPATH,"/html/body/div[45]/div[2]/div/div/div[2]/form/div[7]/div/div/div/div/input")
    cpbm = (By.XPATH,"/html/body/div[45]/div[2]/div/div/div[2]/form/div[8]/div/div/div/div/input")
    cppp = (By.XPATH,"/html/body/div[45]/div[2]/div/div/div[2]/form/div[9]/div/div/div/div/input")
    qtcs = (By.XPATH,"/html/body/div[45]/div[2]/div/div/div[2]/form/div[10]/div/div/div/div/textarea")
    cpms = (By.XPATH,"/html/body/div[45]/div[2]/div/div/div[2]/form/div[11]/div/div/div/div/div[2]/div[2]/div[1]")
    qdBtn = (By.XPATH,"/html/body/div[45]/div[2]/div/div/div[3]/div/button[2]")

    checkBox=(By.XPATH,"/html/body/div[49]/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr/td[1]/div/label/span/input")
    tjBtn=(By.XPATH,"/html/body/div[49]/div[2]/div/div/div[3]/div/button[2]")
    yz = (By.XPATH,"//span[contains(text(),'遴选中心')]")
    def add_application_action_nj(self,number,application_name,application_type,application_cast,unit,picture,region):
        ###向excel中写入服务编号，方便监管端查询
        workbook = xlrd.open_workbook('../data/application.xls')
        excel =copy(workbook)
        table = excel.get_sheet(0)
        table.write(int(number),2,'')
        excel.save('../data/application.xls')
        logger.info('-----clean excel finished------')
        file = os.path.abspath(os.path.join(os.getcwd(), "../.."))
        picture_file = file+ "\shhfw\data\%s"%picture

        logger.info('============add_application_action==============')
        self.driver.find_element(*self.fwxz).click()
        self.driver.find_element(*self.applicationBtn).click()
        logger.info('服务名称 is:%s' %application_name)
        self.driver.find_element(*self.applicationName).send_keys(application_name)
        application_Number = random.randint(000000000000000,9999999999999999)
        logger.info('服务编号 is:%s' %application_Number)
        self.driver.find_element(*self.applicationNumber).send_keys(application_Number)
        ###向excel中写入服务编号，方便监管端查询
        workbook = xlrd.open_workbook('../data/application.xls')
        excel =copy(workbook)
        table = excel.get_sheet(0)
        table.write(int(number),2,str(application_Number))
        excel.save('../data/application.xls')
        logger.info('-----write excel finished------')

        logger.info('服务类型 is:%s' %application_type)
        self.driver.find_element(*self.applicationType_1).click()
        element = self.driver.find_element(*self.applicationType_2)
        element1 =element.find_elements_by_xpath('li')

        for values in element1:
            if application_type in values.text:
                values.click()
                break
        logger.info('服务单价(元) is:%s' %application_cast)
        self.driver.find_element(*self.applicationCast).send_keys(application_cast)
        time.sleep(1)
        self.driver.find_element(*self.applicationUnit1).click()

        element3 = self.driver.find_element(*self.applicationUnit2)
        element4 =element3.find_elements_by_xpath('li')
        for values in element4:
                if unit in values.text:
                    values.click()
                    break
        # logging.info('上传图片 is:%s' %picture)
        self.driver.find_element(*self.updateBtn).send_keys(picture_file)
        logger.info('select sever area')
        li1 = str(region).split("-")
        logger.info("------region is %s------"%region)
        if len(li1) ==1:
            pass
        elif len(li1) ==2:
            self.driver.find_element(*self.serviceArea_Btn).click()
            element_area1= self.driver.find_element(*self.serviceArea_1)
            element_area2 = element_area1.find_elements_by_xpath('li')
            ###找到所有li
            for values in element_area2:
                if li1[1] in values.text:
                    values.click()
                    break

        elif len(li1) ==3:
            self.driver.find_element(*self.serviceArea_Btn).click()
            element_area1= self.driver.find_element(*self.serviceArea_1)
            element_area2 = element_area1.find_elements_by_xpath('li')
            ###找到所有li
            for values in element_area2:
                if li1[1] in values.text:
                    values.click()
                    break

            element_area3= self.driver.find_element(*self.serviceArea_2)
            element_area4 = element_area1.find_elements_by_xpath('li')
            for values in element_area4:
                if li1[2] in values.text:
                    values.click()
                    break
        else:
            pass
            logger.error("area erorr")
        self.driver.find_element(*self.jxmc).send_keys("机械名称")
        self.driver.find_element(*self.jxxh).send_keys("dqeq112312")
        self.driver.find_element(*self.zyms).send_keys("作业描述")
        self.driver.find_element(*self.bz).send_keys("备注")
        self.driver.find_element(*self.msnr).send_keys("描述内容")


        logger.info('click savebutton')
        self.driver.find_element(*self.application_submit).click()
        logger.info('add_application_action finished!')
        time.sleep(5)

    def add_application_action_nz(self,product_name,product_type,product_cast,unit,picture,manufacturer,product_specification,number,trademark,other,description):
        file = os.path.abspath(os.path.join(os.getcwd(), "../.."))
        picture_file = file+ "\shhfw\data\%s"%picture
        self.driver.find_element(*self.fwxz).click()
        self.driver.find_element(*self.nzBtn).click()
        self.driver.find_element(*self.addBtn).click()
        self.driver.find_element(*self.cpmc).send_keys(product_name)
        self.driver.find_element(*self.fwlx1).click()
        element_type1= self.driver.find_element(*self.fwlx2)
        element_type2 = element_type1.find_elements_by_xpath('li')
            ###找到所有li
        for values in element_type2:
            if product_type in values.text:
                values.click()
                break
        self.driver.find_element(*self.cpdj).send_keys(product_cast)
        time.sleep(1)
        self.driver.find_element(*self.jgdw1).click()
        element_cast1= self.driver.find_element(*self.jgdw2)
        element_cast2 = element_cast1.find_elements_by_xpath('li')
            ###找到所有li
        for values in element_cast2:

            if unit in values.text:
                values.click()
                break
        # logging.info('上传图片 is:%s' %picture)
        self.driver.find_element(*self.update).send_keys(picture_file)
        self.driver.find_element(*self.sccj).send_keys(manufacturer)
        self.driver.find_element(*self.cpgg).send_keys(product_specification)
        self.driver.find_element(*self.cpbm).send_keys(number)
        self.driver.find_element(*self.cppp).send_keys(trademark)
        self.driver.find_element(*self.qtcs).send_keys(other)
        self.driver.find_element(*self.cpms).send_keys(description)
        self.driver.find_element(*self.qdBtn).click()
        time.sleep(1.5)
        try:
            self.driver.find_element(*self.checkBox).click()

        except WebDriverException as e:
            logger.error('add application Fail!')
            self.getScreenShot('add application fail')


        self.driver.find_element(*self.tjBtn).click()
        time.sleep(2)





    def check_application_action_nj(self):
        logging.info('====check_add_application_action======')
        try:
            time.sleep(3)
            element = self.driver.find_element(*self.yz)
        except NoSuchElementException:
            logging.error('add application Fail!')
            self.getScreenShot('add application fail')
            return False

        else:
            logging.info('add application success!')
            return True

    def check_application_action_nz(self):
            logging.info('====check_add_application_action======')
            try:
                time.sleep(3)
                element = self.driver.find_element(*self.yz)
            except NoSuchElementException:
                logging.error('add application Fail!')
                self.getScreenShot('add application fail')
                return False

            else:
                logging.info('add application success!')
                return True
if __name__ == '__main__':
    driver=open_browser()
    l=LoginView(driver)
    l.login_action('ht_01','qq2883595')
    l.check_loginStatus()
    time.sleep(4)
    a=ApplicationView(driver)
    a.add_application_action_nz("肥料","肥料",999,"个","update_test.png",'','','','','','')
    a.check_application_action_nz()
    driver.close()
