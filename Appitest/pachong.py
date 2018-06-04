#coding:utf-8
from bs4 import BeautifulSoup

yemian = open("test.html")
soup = BeautifulSoup(yemian,"html.parser")
print soup.prettify()
