class BaseView(object):
    #初始化driver
    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)

    #封装find_element_by_xxx  方法
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    #self.driver.find_elenment_by_xpath('xxxxx')

    #loginBtn=(By.ID,xxxxx)
    #self.driver.find_element(*self.loginBtn)
    #封装find_elements_by_xxx  方法

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)


