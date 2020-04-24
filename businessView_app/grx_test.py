from selenium.webdriver.common.by import By
from common.desired_caps_app import appium_desired
from common.common_fun import Common
from common.excel_read import ExcelUtil
import time
from selenium.common.exceptions import NoSuchElementException
from businessView_app.bookingView import BookingView
import logging,random,xlrd
from xlutils.copy import copy

class Grx_test(Common):
    # fwbtn = (By.ID,'cd.cpt.agricultureservicecircle:id/tab_icon2')
    # nzcg1 = (By.XPATH,'//android.widget.TextView[@text="农药"]')
    # test_check = (By.ID,'cd.cpt.agricultureservicecircle:id/tv_tab_title')
    fwbtn = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.TabWidget/android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.ImageView[2]')
    nzcg1 = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView')
    test_check = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]')
    def cxny(self):
        self.driver.find_element(*self.fwbtn).click()
        time.sleep(1)
        self.driver.find_element(*self.nzcg1).click()
        try:
            driver = self.driver
            time.sleep(2)
            element = driver.find_element(*self.test_check)
            print('ok')
        except NoSuchElementException:
            print('failed')

if __name__ == '__main__':
    dr = appium_desired()
    g = Grx_test(dr)
    g.cxny()

# phoneNumber =random.randint(10000000000,19999999999)
# print(phoneNumber)
# workbook = xlrd.open_workbook('../data/booking.xls')
# excel =copy(workbook)
# table = excel.get_sheet(0)
# table.write(int(5),4,str(phoneNumber))
# excel.save('../data/booking.xls')
#

# element3 = self.driver.find_element_by_xpath('//android.widget.EditText[@text="请填写联系电话"]')
# element3.send_keys(phoneNumber)



# workbook = xlrd.open_workbook('../data/booking.xls')
# excel =copy(workbook)
# table = excel.get_sheet(0)
# table.write(int(5),5,'T')
# excel.save('../data/booking.xls')
# path = '..//data//booking.xls'
# name = 'Sheet1'
# re = ExcelUtil(path,name)
# yuqi = []
# alls = re.next()
# for i in range(len(alls)):
#     yq = alls[i]['预期结果']
#     yuqi.append(yq)
# print(yuqi)


# import xlwt
#
# def data_write(file_path, datas):
#     workbooks = xlwt.Workbook(encoding='utf-8')
#     sheet1 = workbooks.add_sheet(u'工作表1',cell_overwrite_ok=True) #创建sheet
#     dic = datas[0]
#     # 得到键名key 就是把它写入第一行
#     key = list(dic.keys())
#     for i in range(len(key)):
#         sheet1.write(0,i,key[i])
#
#     # 得到每个字典中的vluses，陆续写到后面每排
#     for j in range(len(datas)):
#         zd = datas[j]
#         print(zd)
#         key = list(zd.keys())
#         print(key)
#         for i in range(len(key)):
#             values = datas[j][key[i]]
#             sheet1.write(j+1,i,values)
#
#     workbooks.save(file_path) #
#
# if __name__ == '__main__':
#     data = [{'xm':'小明','nl':'18','mz':'汉族','xb':'男'},{'xm':'小红','nl':'11','mz':'诺克','xb':'女'}]
#     path = '../data/booking.xls'
#     data_write(file_path=path,datas=data)


# workbook = xlrd.open_workbook('../data/booking.xls')
#
# excel =copy(workbook)
# table = excel.get_sheet(0)
# table.write(1,5,'T')
# excel.save('../data/booking.xls')

