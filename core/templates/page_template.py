# encoding=utf-8

from core.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class __PageTemplate__(BasePage):
    # 定义页面URL
    url = "http://bing.com/"

    # 是否等待页面加载完，设置为0则不等待，默认取全局配置的 implicitly_wait_time
    # implicitly_wait_time = 0

    # 页面上元素的locator，大写的方式，格式为 (by, value)
    SearchIcon = (By.XPATH, '//*[@id="search_icon"]')

    def login(self):
        '''可以定义业务逻辑，比如登录、需要多个连续动作的操作等'''
        pass