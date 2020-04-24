import logging
import time
import unittest

from common.HTMLTestRunner import HTMLTestRunner

from test_case_business import test_aplication_nj
from test_case_supervision import test_processing_application

test_dir='../test_case_business'
report_dir='../reports'
logging.info('start run test case...')
suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(test_application_nz.TestApplication))
suite.addTest(unittest.makeSuite(test_aplication_nj.TestApplication))
suite.addTest(unittest.makeSuite(test_processing_application.TestProcessingApplication))

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+' test_report.html'
with open(report_name,'wb') as file:
    HTMLTestRunner(stream=file,title='社会化服务测试报告',description='社会化服务测试报告').run(suite)
