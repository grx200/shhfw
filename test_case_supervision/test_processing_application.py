import ddt
import time
import xlrd
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from common.common_fun import Common
from common.excel_read import ExcelUtil
from common.myunit_supervision import StartEnd
from common.desired_caps_supervision import open_browser
from businessView_supervision.loginView_zf import LoginView_jg
from businessView_supervision.processing_application import ProcessingApplication
import unittest
import logging

#获取excel文件中的用例条数，控制下方用例执行次数
file = '../data/application.xls'
excel = ExcelUtil(file,"Sheet1")
@ddt.ddt
class TestProcessingApplication(StartEnd):

    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')
    @ddt.data(*excel.next())
    def testAddOrder(self,data):
        try:
            #再次获取数据，需要注意的是前面执行的用例中有写入excel的操作时，需要再次获取一下以获取最新的数据
            data1 = xlrd.open_workbook('../data/application.xls')
            sheet = data1.sheet_by_index(0)
            nrows = sheet.nrows
            ncols = sheet.ncols
            li1 = []
            #取出服务编号
            for i in range(1,nrows):#第0行为表头
                alldata = sheet.row_values(i)#循环输出excel表中每一行，即所有数据
                li1.append(alldata[2]) #每次重新取数据，写在test外面会有问题
                print(alldata[2])

            logging.info('======test_processing_application=====')
            #每次用例执行前，返回系统服务概况模块
            self.driver.get("http://192.168.10.7:9000/supervision/#/fwgk")

            #强制等待3秒
            time.sleep(3)
            #处理申请
            b = ProcessingApplication(self.driver)
            b.processing_application(li1[int(data['编号'])-1],data['是否通过'])
            #检查测试结果
            self.assertTrue(b.check_processing_application_action())
        #异常处理：测试执行过程中，找不到定位元素的处理情况
        except NoSuchElementException:

            file_name = "no_such_element"
            b = Common(self.driver)
            b.getScreenShot(file_name)
            self.assertTrue(False)
            raise
        #异常处理：测试执行过程中，元素不可操作的处理情况
        except ElementNotVisibleException:
            file_name = "element_not_visible"
            b = Common(self.driver)
            b.getScreenShot(file_name)
            self.assertTrue(False)
            raise

if __name__ == '__main__':
    unittest.main()
