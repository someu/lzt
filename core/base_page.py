# encoding=utf-8

import logging
from time import sleep
from xmlrpc.client import Boolean
from core.config import Config
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from core.logger import get_logger
from selenium.webdriver.common.keys import Keys

from core.utils import get_class_name


class BasePage(object):
    '''页面基类，实现页面的常用操作'''

    # 页面url
    url = ""
    # 页面加载的等待时间
    implicitly_wait_time = Config.ImplicitlyWaitTime

    def __init__(self,
                 driver: webdriver.Chrome,
                 url="",
                 implicitly_wait_time=None) -> None:
        self.driver = driver
        self.logger = get_logger(get_class_name(self.__class__))

        # implicitly_wait_time 和 url 都是可选的，如果传入了值，则会覆盖默认的值
        if implicitly_wait_time != None:
            self.implicitly_wait_time = implicitly_wait_time
        if url:
            self.url = url

        self.driver.get(url=self.url)
        self.logger.debug(f"打开页面 {self.url}")

        # 隐式等待
        if self.implicitly_wait_time:
            self.logger.debug(f"等待页面加载完成，超时时间{self.implicitly_wait_time}")
            try:
                self.implicitly_wait(self.implicitly_wait_time)
            except TimeoutError as e:
                self.logger.debug("页面加载超时")
                raise e

    def implicitly_wait(self, implicitly_wait_time):
        '''隐式等待'''
        self.driver.implicitly_wait(implicitly_wait_time)

    def find_element(self, by=By.ID, value=None):
        '''查找一个元素'''
        return self.driver.find_element(by, value)

    def input_text(self, by=By.ID, value=None, text=""):
        '''查找一个元素，并输入文字'''
        return self.find_element(by, value).send_keys(text)

    def clear_text(self, by=By.ID, value=None):
        '''查找一个元素，并清除文字'''
        return self.find_element(by, value).clear()

    def enter_element(self, by=By.ID, value=None):
        '''在一个元素上按回车'''
        return self.find_element(by, value).send_keys(Keys.ENTER)

    def click(self, by=By.ID, value=None):
        '''点击元素'''
        return self.find_element(by, value).click()

    def wait_for(self, ec, timeout=10):
        '''等待某个条件为真'''
        try:
            WebDriverWait(self.driver, timeout).until(ec)
            return True
        except Exception:
            return False

    def wait_for_element_exist(self, by=By.ID, value=None, timeout=10):
        '''等待页面中有某个元素，默认超时10s'''
        ec = EC.presence_of_element_located((by, value))
        return self.wait_for(ec, timeout)

    def wait_for_element_include(
        self,
        by=By.ID,
        value=None,
        text="",
        timeout=10,
    ):
        '''等待页面某个元素包含某个字符串'''
        ec = EC.text_to_be_present_in_element((by, value), text)
        return self.wait_for(ec, timeout)

    def jump_to_url_if_needed(self,
                              url,
                              implicitly_wait_time=Config.ImplicitlyWaitTime):
        '''跳转至url'''
        current_url = self.driver.current_url
        if not current_url.startswith(url):
            self.driver.get(url)
            if implicitly_wait_time:
                self.implicitly_wait(implicitly_wait_time)

    def jump_to_origin(self, implicitly_wait_time=Config.ImplicitlyWaitTime):
        '''跳转回初始页面'''
        self.jump_to_url_if_needed(self.url, implicitly_wait_time)

    def screenshot(self):
        '''截屏，返回图片的base64字符串'''
        return self.driver.get_screenshot_as_base64()

    def screenshot_element(self, by=By.ID, value=None):
        '''对元素截屏，返回图片的base64字符串'''
        return self.find_element(by, value).screenshot_as_base64

    def get_window_size(self):
        '''获取窗口大小 { "width": 1024, "height": 960 }'''
        return self.driver.get_window_size()

    def set_window_size(self, width=1024, height=960):
        '''设置窗口大小'''
        return self.driver.set_window_size(width, height)

    def maximize_window(self):
        '''窗口最大化'''
        return self.driver.maximize_window()
    
    def minimize_window(self):
        '''窗口最小化'''
        return self.driver.minimize_window()

    def sleep(self, secs):
        '''time.sleep'''
        return sleep(secs)