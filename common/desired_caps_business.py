from selenium import webdriver
import os
from config.log import logger


#封装了打开浏览器的方法，并返回driver
def open_browser():
    chromedriver = "C:/Users/cpt/AppData/Local/Google/Chrome/Application/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    url = "http://192.168.10.7:9000/"
    driver.get(url)
    driver.maximize_window()
    return driver

op = open_browser()

# if __name__ == '__main__':
#     logger.info("测试中文")


