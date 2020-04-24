import logging
import unittest
from common.common_fun import Common
import time

import xlrd
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from businessView_business.processingOrder_demand import processingOder
from common.myunit_business import StartEnd
import ddt
from common.desired_caps_business import open_browser
from businessView_business.loginView import LoginView
from businessView_business.demand import demand
from common.excel_read import ExcelUtil

file = '../data/demand.xls'
excel = ExcelUtil(file,"Sheet1")
@ddt.ddt
class TestprocessingOderXq(StartEnd):
    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')


    @ddt.data(*excel.next())
    def testProcessingOderXq(self,data):
        try:
            data1 = xlrd.open_workbook('../data/demand.xls')
            sheet = data1.sheet_by_index(0)
            nrows = sheet.nrows
            ncols = sheet.ncols
            li1 = []
            for i in range(1,nrows):#第0行为表头
                alldata = sheet.row_values(i)#循环输出excel表中每一行，即所有数据
                li1.append(alldata[4]) #每次重新取数据，写在test外面会有问题
            if len(li1[int(data['编号'])-1]) == 20:
                l=LoginView(self.driver)
                l.login_action('17708179512','qq2883595')
                time.sleep(3)
                a = processingOder(self.driver)
                a.processing_order_dfw(data['需求类型'],li1[int(data['编号'])-1])
                a.processing_order(data['需求类型'],li1[int(data['编号'])-1])
                # a.processing_order(data['订单类型'],data1)
                a.processing_servering_order(data["需求类型"],li1[int(data['编号'])-1])
                self.assertTrue(a.check_processing_servering_order_status())
                self.driver.quit()
            else:
                self.assertTrue(False)
        except NoSuchElementException:

            file_name = "no_such_element"
            b = Common(self.driver)
            b.getScreenShot(file_name)
            self.assertTrue(False)
            raise

        except ElementNotVisibleException:

            file_name = "element_not_visible"
            b = Common(self.driver)
            b.getScreenShot(file_name)
            self.assertTrue(False)
            raise


if __name__ == "__main__":
    unittest.main()