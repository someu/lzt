# encoding=utf-8

from core.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By


class BingPage(BasePage):
    # 定义页面URL
    url = "http://bing.com/"

    # 是否等待页面加载完，设置为0则不等待，默认取全局配置的 implicitly_wait_time
    # implicitly_wait_time = 0

    # 页面上元素的locator，大写的方式，格式为 (by, value)
    Input = (By.XPATH, '//*[@id="sb_form_q"]')
    SearchBtn = (By.XPATH, '//*[@id="search_icon"]')
    Pagation = (By.XPATH, '//*[@id="b_results"]/li[14]')

    def search(self, text):
        '''搜索'''
        self.jump_to_origin()
        self.input_text(*self.Input, text)
        self.click(*self.SearchBtn)
        return self.wait_for_element_exist(*self.Pagation, timeout=20)