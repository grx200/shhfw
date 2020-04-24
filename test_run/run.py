import unittest
import time
from common.HTMLTestRunner import HTMLTestRunner
from common import send_email
from config.log import logger
from test_case_app import test_appDemand
from test_case_business import test_processingDemand
from test_case_business import test_processing_order_xq
from test_case_app import test_check
from test_case_app import test_booking
from test_case_business import test_processing_order_booking
from test_case_app import test_check

#设置测试用例、测试报告路径
test_dir='../test_case_business'
report_dir='../reports'
logger.info('start run test case...')

#加载测试用例
suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(test_appDemand.TestAppDemand))
# suite.addTest(unittest.makeSuite(test_processingDemand.TestprocessingDemand))
suite.addTest(unittest.makeSuite(test_processing_order_xq.TestprocessingOderXq))
suite.addTest(unittest.makeSuite(test_booking.TestBooking))
# suite.addTest(unittest.makeSuite(test_processing_order_booking.TestprocessingOder))
# suite.addTest(unittest.makeSuite(test_check.TestCheck))

##设置测试报告名称
now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+'report.html'

#执行测试用例生成测试报告
with open(report_name,'wb') as file:
    HTMLTestRunner(stream=file,title='社会化服务测试报告',description='社会化服务测试报告',retry=1,save_last_try=False).run(suite)

# 通过邮件发送测试报告的
logger.info("start send email......")
try:
    rep = send_email.get_report('../reports')
    send_email.send_email(rep)
except:
    logger.error("send_email failed")
finally:
    logger.info("send_email success")