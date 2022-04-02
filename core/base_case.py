# encoding=utf-8

import csv
import logging
from time import sleep
from unittest import TestCase
from selenium import webdriver
from core.config import Config
from os import path

from core.logger import get_logger
from core.utils import get_class_name


class BaseCase(TestCase):
    '''
    测试用例基类，实现公共的测试用例逻辑：初始化时打开浏览器、关闭浏览器等。
    初始化时调用子类的subSetUp方法
    '''

    # webdriver 路径
    executable_path = Config.ExecutablePath
    # 是否无头模式（不显示页面）
    headless = Config.Headless
    # 代理
    proxy = Config.Proxy
    # 浏览器打开时的参数，用于自定义扩展
    options = webdriver.ChromeOptions()

    logger: logging.Logger
    images: list

    @classmethod
    def setUpClass(cls) -> None:
        '''所有测试方法运行前运行'''
        super().setUpClass()

        # 设置logger
        cls.logger = get_logger(get_class_name(cls))
        cls.logger.debug("打开浏览器")

        # 初始化浏览器
        chrome_options = cls.options
        if cls.headless:
            chrome_options.add_argument("--headless")
        if cls.proxy:
            chrome_options.add_argument(f"--proxy-server={cls.proxy}")

        cls.driver = webdriver.Chrome(executable_path=cls.executable_path,
                                      chrome_options=chrome_options)

        # 设置浏览器页面大小，无头模式下maximize_window不起作用
        if (not Config.Headless) and Config.MaximizeWindow:
            cls.driver.maximize_window()
        else:
            cls.driver.set_window_size(Config.BrowserWidth,
                                       Config.BrowserHeight)
        cls.logger.debug(f"浏览器大小：{cls.driver.get_window_size()}")

    @classmethod
    def tearDownClass(cls) -> None:
        '''所有测试方法结束后运行'''
        super().tearDownClass()
        # 关闭浏览器
        cls.driver.close()
        cls.logger.debug("关闭浏览器")

    def append_screenshot(self, img_base64):
        '''往报告里添加截图'''
        self.images.append(img_base64)

    def sleep(self, secs):
        '''time.sleep'''
        return sleep(secs)

    def useful(self):
        '''可以在测试用例上扩展常用的方法'''
        pass
