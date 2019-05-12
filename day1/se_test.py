#coding=utf8

from selenium import webdriver
from time import sleep
#打开浏览器
def opwd():
    #启动配置,消除Chome打开后提示
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    #打开Chome浏览器
    dr=webdriver.Chrome(chrome_options=option)
    dr.get("https://www.baidu.com")
    dr.maximize_window()
    sleep(5)
    dr.quit()
opwd()
