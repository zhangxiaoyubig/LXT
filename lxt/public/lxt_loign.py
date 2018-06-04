from  selenium import  webdriver
from selenium.webdriver.common.by import By


def opera_login(self, username, pwd):
    driver = self.driver
    driver.get('http://' + self.opera_url)
    driver.find_element(By.XPATH, ".//*[@id='form1']/div[1]/input").clear()
    driver.find_element(By.XPATH, ".//*[@id='form1']/div[1]/input").send_keys(username)
    driver.find_element(By.XPATH, ".//*[@id='form1']/div[2]/input").clear()
    driver.find_element(By.XPATH, ".//*[@id='form1']/div[2]/input").send_keys(pwd)
    driver.find_element(By.XPATH, ".//*[@id='form1']/div[3]/button").click()