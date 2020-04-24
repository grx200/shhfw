from config.log import logger
import unittest
import ddt,time,xlrd
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from businessView_app.bookingView import BookingView
from businessView_app.loginView_app import LoginView
from businessView_app.applyDemand import xuqiu
from common.myunit_app_login import StartEnd
from common.excel_read import ExcelUtil
from common.common_fun import Common
from xlutils.copy import copy

@ddt.ddt
class TestBooking(StartEnd):
    file = '../data/booking.xls'
    excel = ExcelUtil(file,"Sheet1")
    # csv_file='../data/account.csv'
    # @unittest.skip('skip test_login_001')
    @ddt.data(*excel.next())
    def testBooking(self,data):
        try:
            #每次用例执行前重启APP（APP不能像web端一样，用例执行前通过地址栏跳转至固定页面，只能通过重启的方式来实现固定流程）
            self.driver.launch_app()
            #登录

            l=LoginView(self.driver)
            l.login_action('17708179510',123456)
            logger.info('======test_booking=====')
            time.sleep(2)
            #订单业务
            a = BookingView(self.driver)
            self.bh = data['编号']
            # 最后一个参数电话号码，是用来找到这个输入域的，因为元素定位不到，且输入域中有默认值，所有根据默认值来定位电话号码输入域，然后再把他清除掉，传入生成的随机电话
            # 里面的服务名称都是乱编的，二天跑的时候，需要按照具体情况去修改新增订单选择的农机或农资的名称
            #123是电话号码输入域的默认值
            a.booking_action(data['编号'],data['服务类型'],data["服务名称"],data["服务数量"],'123')
            # 看看新增订单的实际情况，如果新增成功，就在excel中记录"T",失败的话记录“F”
            self.re = a.check_bookingStatus()
            if self.re == True:
                workbook = xlrd.open_workbook('../data/booking.xls')
                excel =copy(workbook)
                # excel.get_sheet()中的参数0表示第一个sheet表，改为参数1的话就表示在第二个sheet表中添加数据
                table = excel.get_sheet(0)
                table.write(int(self.bh),5,'ok')
                excel.save('../data/booking.xls')
            else:
                workbook = xlrd.open_workbook('../data/booking.xls')
                excel =copy(workbook)
                table = excel.get_sheet(0)
                table.write(int(self.bh),5,'ko')
                excel.save('../data/booking.xls')

            # 再从excel中读取实际结果和预期结果，判断是否一致
            self.yuqi = data['预期结果']
            self.assertEqual(self.yuqi,self.re)
            #每次用例结束后，关闭APP
            self.driver.close_app()


        except NoSuchElementException:
            file_name = "no_such_element"
            b = Common(self.driver)
            b.getScreenShot(file_name)
            workbook = xlrd.open_workbook('../data/booking.xls')
            excel =copy(workbook)
            table = excel.get_sheet(0)
            table.write(int(self.bh),5,'ko')
            excel.save('../data/booking.xls')

            self.assertEqual(self.yuqi,False)
            self.driver.close_app()
            raise

        except ElementNotVisibleException:
            file_name = "element_not_visible"
            b = Common(self.driver)
            b.getScreenShot(file_name)
            workbook = xlrd.open_workbook('../data/booking.xls')
            excel =copy(workbook)
            table = excel.get_sheet(0)
            table.write(int(self.bh),5,'ko')
            excel.save('../data/booking.xls')

            self.assertEqual(self.yuqi,False)
            self.driver.close_app()
            raise


if __name__ == "__main__":
    unittest.main()