import subprocess
# import pymysql,pymssql
import xlrd,xlwt
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from xlutils.copy import copy
from baseView.baseView import BaseView
# from common.desired_caps_business import open_browser
from selenium.common.exceptions import NoSuchElementException
from config.log import logger
from selenium.webdriver.common.by import By
import time,os
import csv

class Common(BaseView):
    #获取当前系统时间
    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    #截图保存到本地
    def getScreenShot(self,model):
        logger.info("get screenshot %s failed"%model)

        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath = os.path.join('..\screenshots', '%s.png' % str(timestrmap))
        self.driver.save_screenshot(imgPath)
        print('screenshot:', timestrmap, '.png' )

    #截图保存到测试报告中
    def add_img(self):
        self.driver.get_screenshot_as_base64()
        return True

    #从csv格式表单中获取数据
    def get_csv_data(self,csv_file,line):
        logger.info('=====get_csv_data======')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row

    def fast_input(self,str,element):
    #####'快速输入'######
        x = subprocess.check_output('adb devices', shell=True).decode()
        x= x.split('\n')[1][:-7]
        element.click()
        time.sleep(0.3)
        subprocess.Popen('adb -s %s shell input text %s'%(x,str), shell=True)
        time.sleep(0.5)

    def editClear(self,text):
    ###直接使用clear()太慢了的话，可以使用这个方法####
    #     123代表光标移动到末尾
        self.driver.keyevent(123)
        for i in range(0, len(text)):
            #67退格键
            self.driver.keyevent(67)

    def get_result(self,file,column):
        data = xlrd.open_workbook(file)
        sheet = data.sheet_by_index(0)
        nrows = sheet.nrows
        ncols = sheet.ncols
        li1 = []
        for i in range(1,nrows):#第0行为表头
            alldata = sheet.row_values(i)#循环输出excel表中每一行，即所有数据
            li1.append(alldata[column])
        return li1

    #获取手机屏幕大小
    def getSize(self):                               #获取当前的width和height的x、y的值
        x = self.driver.get_window_size()['width']   #width为x坐标
        y = self.driver.get_window_size()['height']  #height为y坐标
        return (x, y)
    #向下滑动swipedown

    def swipeDown(self):
        #获取屏幕大小
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        #设置坐标系坐标
        x1 = int(x * 0.5)
        y1 = int(y * 0.25)
        y2 = int(y * 0.75)
        #进行滑动操作
        driver.swipe(x1, y1, x1, y2,500)

    def writeExcell(self,excelPath,sheet_index,nrow,col,data):  ########写入数据导excel文件中
        workbook = xlrd.open_workbook(excelPath) ##获取需要写入的excel文件
        excel =copy(workbook)  ###复制一份，因为如果不复制的话下面过程中出现问题，那么原来的excel文件可能就打不开了
        table = excel.get_sheet(sheet_index) #####选择需要写入的sheet
        table.write(int(nrow),int(col),str(data))   #####写入数据，意思为写入OrderNumber到nrow行，第col列
        excel.save(excelPath) ####再保存文件，其实就是覆盖

    '''这里注释掉了下方方法，如需使用到取消注释即可'''
    # def conectDatabase(self,sql_type,host,user,password,database,sql):
    #     #########连接数据库进行操作,sql_type="数据库类型:mysql、sqlsever"host="数据库地址"，user=用户名，password=密码，database=数据库名，sql=SQL语句
    #     ####使用这个方法需要安装第三方包pymysql以及pymssql
    #     if sql_type=="mysql" or sql_type=="MySQL":
    #         conn = pymysql.connect(host=host,user=user,password=password,database=database,charset='utf-8')
    #         cursor=conn.cursor()
    #         req =cursor.execute(sql)
    #         cursor.close()
    #         conn.close()
    #         return req
    #     elif sql_type=="sqlsever" or sql_type=="SQLSever":
    #         conn = pymssql.connect(host=host,user=user,password=password,database=database)
    #         cursor =conn.cursor()
    #         req=cursor.execute(sql)
    #         cursor.close()
    #         conn.close()
    #         return req
    #     else:
    #         logging.error("----sql type error----")

# if __name__ == '__main__':
#     driver=open_browser()







