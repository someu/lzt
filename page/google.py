# encoding=utf-8

from cgi import test
from core.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class GooglePage(BasePage):
    # 定义页面URL
    url = "https://www.google.com/"

    # 是否等待页面加载完，设置为0则不等待，默认取全局配置的 implicitly_wait_time
    # implicitly_wait_time = 0

    # 页面上元素的locator，格式为 (by, value)
    Input = (
        By.XPATH,
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    Pagation = (By.XPATH,
                '/html/body/div[7]/div/div[10]/div/div[6]/span[1]/table')

    def search(self, text):
        '''搜索'''
        self.input_text(*self.Input, text)
        self.enter_element(*self.Input)
        return self.wait_for_element_exist(*self.Pagation, timeout=20)