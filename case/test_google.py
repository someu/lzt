# encoding=utf-8

from core.base_case import BaseCase
# 1. 引入page
from page.google import GooglePage


class TestGoogle(BaseCase):
    '''测试google'''

    # 可以自定义设置当前测试用例的配置
    # executable_path = ""
    # headless = ""
    proxy = "socks5://127.0.0.1:1080"

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        '''初始化测试方法使用到的页面'''

        # 2. 设置测试方法使用到的页面
        # 传入 implicitly_wait_time 可以自定义页面等待时间
        cls.gp = GooglePage(cls.driver, implicitly_wait_time=0)

    def test_search(self):
        '''测试搜索'''

        # 4. 调用页面的业务逻辑，使用页面元素
        self.assertTrue(self.gp.search("ui test"), "搜索 ui test 失败")
