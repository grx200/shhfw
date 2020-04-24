import unittest
from common.desired_caps_app import appium_desired
from config.log import logger
from businessView_app.loginView_app import LoginView
from time import sleep
import warnings
#封装用例执行前后的操作
class StartEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        logger.info('=====setUp====')
        cls.driver=appium_desired()
    #所有用例执行完成后退出appium
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def add_img(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass
