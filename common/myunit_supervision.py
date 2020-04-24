import unittest
from common.desired_caps_supervision import open_browser
import logging
from time import sleep
from businessView_supervision.loginView_zf import LoginView_jg
#封装用例执行前后的操作
class StartEnd(unittest.TestCase):
    #打开浏览器，并登陆系统
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        l=LoginView_jg(cls.driver)
        l.login_action("admin",'123456')
    #用例执行结束后关闭浏览器
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    #用例执行失败或异常时，默认进行截图（注意这里的截图不会保存至screenshots包中，而是直接放到测试报告中）
    #想要在本地保存截图，需要在用例执行过程中调用Common中的截图方法
    def add_img(self):
        self.driver.get_screenshot_as_base64()
        return True
    #下面这两个方法，是因为为python3.X中unittest机制和python2不一致，为了默认截图的解决办法
    def setUp(self):
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass