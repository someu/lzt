# encoding=utf-8

from core.base_case import BaseCase
# 1. 引入page
# from page.bing import BingPage


class __CaseTemplate__(BaseCase):
    '''测试用例描述'''

    # 可以自定义设置当前测试用例的配置
    # executable_path = ""
    # headless = ""
    # proxy = ""

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        '''初始化测试方法使用到的页面'''

        # 2. 设置测试方法使用到的页面
        # cls.bp = BingPage(cls.driver)

    def test_search(self):
        '''3. 编写测试方法，以 test_* 格式'''

        # 4. 调用页面的业务逻辑，使用页面元素
        # ele = self.bp.wait_for_element_exist(*self.bp.SearchIcon)
        # self.assertIsNotNone(ele, "搜索按钮不存在")
