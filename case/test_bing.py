# encoding=utf-8

from core.base_case import BaseCase
# 1. 引入page
from page.bing import BingPage
from ddt import ddt, data


@ddt
class TestBing(BaseCase):
    '''测试bing'''

    # 可以自定义设置当前测试用例的配置
    # executable_path = ""
    # headless = ""
    # proxy = ""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        '''初始化测试方法使用到的页面'''

        # 2. 设置测试方法使用到的页面
        cls.bp = BingPage(cls.driver)

    @data("test1", "test2")
    def test_search(self, text):
        '''测试搜索'''
        self.assertIsNotNone(self.bp.search(text), "搜索功能")
        self.append_screenshot(self.bp.screenshot())
        self.bp.jump_to_origin()
        self.append_screenshot(self.bp.screenshot())
        self.append_screenshot(self.bp.screenshot_element(*self.bp.Input))
