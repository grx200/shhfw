import logging,os
import random
import time
from businessView_business.loginView import LoginView
from common.common_fun import Common,NoSuchElementException
from common.desired_caps_business import open_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#####资源管理模块####
class resource_management(Common):
    ###新增人员
    zyglBtn = (By.XPATH,"/html/body/div[1]/div[1]/div/ul[1]/li[8]/div[1]")
    xzryBtn = (By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div/div[1]/div[1]/div/button[1]")
    ygbh = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[3]/div/div/div/div/input")
    xm = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[4]/div/div/div/div/input")
    xb1 = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[5]/div/div/div/div/div/div/span")
    xb2 = (By.XPATH,"/html/body/div[12]/ul[2]/li[1]")
    csrq = (By.XPATH,"/html/body/div[12]/ul[2]/li[1]")
    whcd1 = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[7]/div/div/div/div/div/div/span")
    whcd2 = (By.XPATH,"/html/body/div[13]/ul[2]/li[1]")
    zw1 = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[8]/div/div/div/div/div/div/span")
    zw2 = (By.XPATH,"/html/body/div[14]/ul[2]/li[1]")
    lxfs = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[9]/div/div/div/div/input")
    sfz = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[10]/div/div/div/div/input")
    bz = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[11]/div/div/div/div/textarea")
    cznjlx = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[12]/div/div/div/div/div/div/span")
    jsz = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[13]/div/div/div/div/input")
    sfcz = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[14]/div/div/div/label[1]/span/input")
    username = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[15]/div/div/div/div/input")
    passwd = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[2]/form/div[17]/div/div/div/div/input")
    tjBtn = (By.XPATH,"/html/body/div[16]/div[2]/div/div/div[3]/div/button[2]")

    ###新增农机

    njglBtn = (By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[3]")
    xznjBtn = (By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[3]/div/div/div[1]/div[1]/div/button/span")
    njmc = (By.XPATH,"/html/body/div[14]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div[1]/input")
    xhgg = (By.XPATH,"/html/body/div[14]/div[2]/div/div/div[2]/form/div[3]/div/div/div/div/input")
    sccj = (By.XPATH,"/html/body/div[14]/div[2]/div/div/div[2]/form/div[4]/div/div/div/div/input")
    zylx1 = (By.XPATH,"/html/body/div[14]/div[2]/div/div/div[2]/form/div[5]/div/div/div/div/div/div/span")
    zylx2 = (By.XPATH,"/html/body/div[12]/ul[2]/li[1]")
    njzp = (By.XPATH,"/html/body/div[14]/div[2]/div/div/div[2]/form/div[7]/div/div/div/div/div/div[1]/div/input")
    cfdd = (By.XPATH,"/html/body/div[14]/div[2]/div/div/div[2]/form/div[8]/div/div/div/div/input")
    xxpz = (By.XPATH,"/html/body/div[14]/div[2]/div/div/div[2]/form/div[9]/div/div/div/div/textarea")
    njbz = (By.XPATH,"/html/body/div[14]/div[2]/div/div/div[2]/form/div[10]/div/div/div/div/textarea")
    xzsbBtn = (By.XPATH,"/html/body/div[14]/div[2]/div/div/div[2]/form/div[11]/div/button")
    sbbh = (By.XPATH,"/html/body/div[13]/div[2]/div/div/div[2]/form/div/div/div/div/div/input")
    addBtn = (By.XPATH,"/html/body/div[13]/div[2]/div/div/div[3]/div/button[2]")
    qrBtn = (By.XPATH,"/html/body/div[14]/div[2]/div/div/div[3]/div/button[2]")
    ###采集仪管理


    def addPerson(self):
        time.sleep(4)
        self.driver.find_element(*self.zyglBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.xzryBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.ygbh).send_keys(random.randint(10000000,999999999))
        self.driver.find_element(*self.xm).send_keys("测试")
        self.driver.find_element(*self.xb1).click()
        time.sleep(0.5)
        self.driver.find_element(*self.xb2).click()
        # self.driver.find_element(*self.csrq).send_keys("2019-08-16")
        self.driver.find_element(*self.whcd1).click()
        time.sleep(0.5)
        self.driver.find_element(*self.whcd2).click()
        time.sleep(0.5)
        self.driver.find_element(*self.zw1).click()
        time.sleep(0.5)
        self.driver.find_element(*self.zw2).click()
        self.driver.find_element(*self.lxfs).send_keys("17708179510")
        self.driver.find_element(*self.username).send_keys("test111")
        self.driver.find_element(*self.passwd).send_keys("qq2883595")
        self.driver.find_element(*self.tjBtn).click()

    def addEquipment(self):

        time.sleep(3)
        self.driver.find_element(*self.zyglBtn).click()
        time.sleep(1)
        self.driver.find_element(*self.njglBtn).click()
        time.sleep(0.8)
        self.driver.find_element(*self.xznjBtn).click()
        time.sleep(0.8)
        self.driver.find_element(*self.njmc).send_keys("测试农机设备")
        self.driver.find_element(*self.xhgg).send_keys("asasasa")

        self.driver.find_element(*self.zylx1).click()
        time.sleep(0.5)
        self.driver.find_element(*self.zylx2).click()
        self.driver.find_element(*self.zylx2).click()
        time.sleep(0.3)
        file = os.path.abspath(os.path.join(os.getcwd(), "../.."))
        picture_file = file+ "\shhfw\data\%s"%"update_test.png"
        self.driver.find_element(*self.njzp).send_keys(picture_file)

        self.driver.find_element(*self.xzsbBtn).click()
        self.driver.find_element(*self.sbbh).send_keys(random.randint(100,99999))
        self.driver.find_element(*self.addBtn).click()
        time.sleep(2)
        self.driver.find_element(*self.qrBtn).click()


if __name__ == "__main__":
    driver = open_browser()
    b= LoginView(driver)
    b.login_action("17708179512","qq2883595")
    c = resource_management(driver)
    # c.addPerson()
    c.addEquipment()