from  selenium import  webdriver
import unittest
from  selenium.webdriver.common.by import By
from lxt import public
import time
from  selenium.webdriver.support.select import Select

class Woperate_opera_addopera(unittest.TestCase):
    '''添加运员'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.name = '15510357528'
        self.pwd = '123123'
        self.add_oper_name = '运员1号'
        self.add_oper_pwd = '123123'
        self.add_oper_tel= '13683611333'
        self.opera_url = 'woperate.test.4000669696.com'
        self.type11= "运员"
        self.type12 = "财务"

        driver = self.driver
        driver.get('http://' + self.opera_url)
        driver.find_element(By.XPATH, ".//*[@id='form1']/div[1]/input").clear()
        driver.find_element(By.XPATH, ".//*[@id='form1']/div[1]/input").send_keys(self.name)
        driver.find_element(By.XPATH, ".//*[@id='form1']/div[2]/input").clear()
        driver.find_element(By.XPATH, ".//*[@id='form1']/div[2]/input").send_keys(self.pwd)
        driver.find_element(By.XPATH, ".//*[@id='form1']/div[3]/button").click()

    def test_case(self):
        driver = self.driver
        #Opera_login().opera_login()
        driver.find_element(By.XPATH,"html/body/div[1]/aside/section/ul/li[2]/a/span").click()
        driver.implicitly_wait(3)
        driver.find_element(By.LINK_TEXT,"添加运营人员").click()
        driver.find_element(By.XPATH,".//*[@id='bookss']/div/div[1]/div/input").clear()
        driver.find_element(By.XPATH,".//*[@id='bookss']/div/div[1]/div/input").send_keys(self.add_oper_name)
        driver.find_element(By.XPATH,".//*[@id='bookss']/div/div[2]/div/input").clear()
        driver.find_element(By.XPATH,".//*[@id='bookss']/div/div[2]/div/input").send_keys(self.add_oper_pwd)
        driver.find_element(By.XPATH,".//*[@id='phone']").clear()
        driver.find_element(By.XPATH,".//*[@id='phone']").send_keys(self.add_oper_tel)
        sel = driver.find_element(By.XPATH,".//*[@id='bookss']/div/div[4]/div/select")
        Select(sel).select_by_visible_text(self.type11)
        print("运员创建完成")
        driver.find_element(By.XPATH,".//*[@id='bookss']/div/div[5]/div/button").click()
        name2 = driver.find_element(By.XPATH,".//*[@id='example1']/tbody/tr[1]/td[1]").text
        print("运员名字为" + name2)
        liebiao = driver.find_element(By.XPATH,".//*[@id='example1']/tbody/tr[1]/td[2]").text
        print("列表中第一条数据是" + liebiao)
        #如果名字相符合，做断言
        if name2 == self.add_oper_name:
            self.assertEqual(liebiao,self.type11,msg=" Sorry,Add failure")

    def tearDown(self):
        self.driver.quit()

    if __name__ ==  '__main__':
        unittest.main()