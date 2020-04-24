import logging
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
#####新增订单########
# booking_action需要的参数服务名称，是随便写的，之后跑自动化 需要根据具体的农资或农机产品的名称来进行编写用例
class BookingView(Common):
    # '//android.widget.EditText[@text="注册手机号"]'
    nongjiBtn=(By.XPATH,'//android.widget.TextView[@text="农机服务"]')
    search = (By.XPATH,'//android.widget.EditText[@text="搜索服务/商家/农资"]')
    chanpingBtn=(By.XPATH,'//android.widget.TextView[@text="泸县耕地服务有限公司"]')
    nzBtn = (By.XPATH,'//android.widget.TextView[@text="农资"]')
    yuyueBtn=(By.XPATH,'//android.widget.TextView[@text="服务预约"]')
    nz_booking=(By.XPATH,'//android.widget.TextView[@text="立即购买"]')
    nj_numArea=(By.XPATH,'//android.widget.EditText[@text="请填写服务数量"]')
    #phone = (By.XPATH,'//android.widget.EditText[@text="请填写服务数量"]/parent::android.view.View'
                      #'/parent::android.view.View/following-sibling::android.view.View/android.view.View[4]/android.widget.EditText') ##https://blog.csdn.net/niedongri/article/details/79448179
    nz_numArea=(By.XPATH,'//android.widget.EditText[@text="请填写采购数量"]')
    nj_tijiaoBtn=(By.XPATH,'//android.widget.Button[@text="提交预约"]')
    nz_tijiaoBtn=(By.XPATH,'//android.widget.Button[@text="立即购买"]')
    fanhuiBtn=(By.XPATH,'//android.widget.Button[@text="返回首页"]')
    def booking_action(self,nrow,type,name,number,phone):

        logging.info('============booking_action==============')
        self.imgs.append(self.driver.get_screenshot_as_base64())
        self.driver.find_elements_by_android_uiautomator("new UiSelector().text(\"首页\")")[0].click()
        self.imgs.append(self.driver.get_screenshot_as_base64())
        logging.info('-----start clear excel------')
        workbook = xlrd.open_workbook('../data/booking.xls')
        excel =copy(workbook)
        table = excel.get_sheet(0)
        table.write(int(nrow),4,str( ))
        excel.save('../data/booking.xls')
        logging.info('-----clear excel finished------')
        logging.info('-----search service-----')
        if type == "农机服务":
            self.add_img()
            self.driver.find_element(*self.nongjiBtn).click()
            self.add_img()
            self.driver.find_element(*self.search).send_keys(name)
            self.add_img()
            self.driver.keyevent(66)
            time.sleep(3)
            try:
                self.add_img()
                element = self.driver.find_element_by_xpath('//android.widget.TextView[@text="%s"]'%name)
            except NoSuchElementException:
                logging.error("-------no element---------")
                self.getScreenShot("bookingFailed")
            else:
                logging.info("search sucess")
                logging.info('-----select service-----')
                element.click()
            time.sleep(2)
            self.driver.find_element(*self.yuyueBtn).click()
            time.sleep(2)
            element1 = self.driver.find_element(*self.nj_numArea)

            # self.fast_input(number,element1) ####快速输入
            element1.send_keys(number)
            # driver = self.driver
            logging.info('-----start write order info------')
            logging.info('booking number is %s'%number)
            time.sleep(2)
            # self.driver.find_element_by_xpath('//android.widget.EditText[@text="%s"]'%phone).clear()###修改手机号，方便bs中搜索定位
            ############快速清除##########################
            element2 = self.driver.find_element_by_xpath('//android.widget.EditText[@text="%s"]'%phone)
            element2.clear()
            phoneNumber =random.randint(10000000000,19999999999)
            logging.info('-----start write excel------')
            workbook = xlrd.open_workbook('../data/booking.xls')
            excel =copy(workbook)
            table = excel.get_sheet(0)
            table.write(int(nrow),4,str(phoneNumber))
            excel.save('../data/booking.xls')
            logging.info('-----write excel finished------')
            logging.info('-----order phone number is %s------'%str(phoneNumber))
            element3 = self.driver.find_element_by_xpath('//android.widget.EditText[@text="请填写联系电话"]')
            element3.send_keys(phoneNumber)
            # self.fast_input(phoneNumber,element3)###修改手机号，方便bs中搜索定位
            ###修改手机号，方便bs中搜索定位

            self.driver.find_element(*self.nj_tijiaoBtn).click()
            logging.info('booking finished!')
            time.sleep(2)
        else:
            self.driver.find_element(*self.nzBtn).click()
            self.driver.find_element(*self.search).send_keys(name)
            self.driver.keyevent(66)
            element = self.driver.find_elements_by_xpath('//android.widget.TextView[@text="%s]'%name)
            element[0].click()
            time.sleep(2)
            self.driver.find_element(*self.nz_booking).click()
            time.sleep(2)
            element1 = self.driver.find_element(*self.nz_numArea)
            element1.send_keys(number)
            # self.fast_input(number,element1) ####快速输入
            # driver = self.driver
            logging.info('booking number is %d'%number)
            # self.driver.find_element_by_xpath('//android.widget.EditText[@text="%s"]'%phone).clear()###修改手机号，方便bs中搜索定位

            ############快速清除##########################
            element2 = self.driver.find_element_by_xpath('//android.widget.EditText[@text="%s"]'%phone)
            element2.clear()

            phoneNumber =random.randint(10000000000,19999999999)
            logging.info('-----start write excel------')
            element3 = self.driver.find_element_by_xpath('//android.widget.EditText[@text="请填写联系电话"]')
            element3.send_keys(phoneNumber)
            # self.fast_input(phoneNumber,element3)###修改手机号，方便bs中搜索定位
            ###修改手机号，方便bs中搜索定位
            workbook = xlrd.open_workbook('../data/booking.xls')
            excel =copy(workbook)
            table = excel.get_sheet(0)
            table.write(int(nrow),4,str(phoneNumber))
            excel.save('../data/booking.xls')
            logging.info('-----write excel finished------')
            logging.info('-----order phone number is %s------'%str(phoneNumber))
            self.driver.find_element(*self.nz_tijiaoBtn).click()
            logging.info('booking finished!')

    def check_bookingStatus(self):
        logging.info('====check_bookingStatus======')
        try:
            time.sleep(3)
            element =self.driver.find_element(*self.fanhuiBtn)
        except NoSuchElementException:
            logging.error('booking Fail!')
            self.getScreenShot('booking fail')
            return False
        else:
            logging.info('booking success!')
            return True





if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    username = '17708179511'
    l.login_action(username,123456)
    l.check_loginStatus()
    time.sleep(4)
    a =BookingView(driver)
    a.booking_action(1,'农机服务',"为遴选而生",111,username)
    a.check_bookingStatus()