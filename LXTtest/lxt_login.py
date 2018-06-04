
#coding=utf-8
from selenium import webdriver

class login():
    """登录类"""
    def __init__(self,driver):
        driver = webdriver.Chrome()
        self.driver = driver

    def group_login(self):
        """集团登录"""
        group_url = "http://lxt.wgp.dev.4000669696.com"
        self.driver.get(group_url)
        self.driver.find_element_by_xpath(".//*[@id='userName1']").clear()
        self.driver.find_element_by_xpath(".//*[@id='userName1']").send_keys(1)
        self.driver.find_element_by_xpath(".//*[@id='password']").clear()
        self.driver.find_element_by_xpath(".//*[@id='password']").send_keys(2)
        self.driver.find_element_by_xpath(".//*[@id='form1']/div[3]/a").click()

    def branch_login(self,username,password):
        """分支登录"""
        self.driver.get("url")
        self.driver.find_element_by_xpath().clear()
        self.driver.find_element_by_xpath().send_keys(username)
        self.driver.find_element_by_xpath().clear()
        self.driver.find_element_by_xpath().send_keys(password)
        self.driver.find_element_by_xpath().click()

    def operaa_login(self,username,password):
        """运营登录"""
        self.driver.get("url")
        self.driver.find_element_by_xpath().clear()
        self.driver.find_element_by_xpath().send_keys(username)
        self.driver.find_element_by_xpath().clear()
        self.driver.find_element_by_xpath().send_keys(password)
        self.driver.find_element_by_xpath().click()


login.group_login()