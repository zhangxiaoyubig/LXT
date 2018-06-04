#coding=utf-8
from  selenium import  webdriver
from  HTMLTestRunner import HTMLTestRunner
import  unittest
import time

class  Baidu(unittest.TestCase):
    '''百度搜索测试'''    #可以显示在小标题后
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"


    def test_baidu_search(self):
        '''搜索关键字'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("hah")
        driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))
    #按照一定的格式获取当前时间
    #now = time.strptime("%Y-%m-%d %H:%M:%S")
    now = time.strftime("%Y_%m_%d %H_%M_%S")

    #定义测试报告存放地址
    fp = open('./' + now + 'result.html','wb')

    runner = HTMLTestRunner(stream = fp,title='百度搜索测试报告',description='用例执行情况')
    runner.run(testunit)
    fp.close()