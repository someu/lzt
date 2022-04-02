# encoding=utf-8
#!/usr/bin/env python

import fire
from unittest import defaultTestLoader
from core.config import Config
from core.logger import logger
from core.utils import big_camel_case
import datetime
from os import path
from XTestRunner import HTMLTestRunner


class Run():
    '''UI自动化测试框架'''

    def new_page(self, name):
        '''根据模版生成一个测试用例，传入name参数指定测试用例名，以下划线形式。
            eg: python run.py new_page <name>
        '''

        class_name = big_camel_case(name)
        class_name = f"{class_name}Page"

        # 页面文件
        page_path = path.join(Config.PageDirPath, f"{name}.py")

        with open(Config.PageTemplatePath, encoding="utf-8") as pf:
            content = pf.read()
            content = content.replace('__PageTemplate__', class_name)
            with open(page_path, "w", encoding="utf-8") as cf:
                cf.write(content)
                cf.close()
            pf.close()
        logger.info(f'生成页面文件: {page_path}')

    def new_case(self, name):
        '''根据模版生成一个测试用例，传入 name 参数指定测试用例名，以下划线形式。
            eg: python run.py new_case <name>
        '''

        class_name = big_camel_case(name)
        class_name = f"Test{class_name}"

        # 测试用例文件
        case_path = path.join(Config.CaseDirPath, f"test_{name}.py")

        with open(Config.TestCaseTemplatePath, encoding="utf-8") as pf:
            content = pf.read()
            content = content.replace('__CaseTemplate__', class_name)
            with open(case_path, "w", encoding="utf-8") as cf:
                cf.write(content)
                cf.close()
            pf.close()
        logger.info(f'生成测试用例文件: {case_path}')

    def start(self):
        '''开始测试。eg: python run.py start'''
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        suite = defaultTestLoader.discover(Config.CaseDirPath,
                                           pattern="test_*.py")
        report_path = path.join(Config.ReportOutput, f"report_{now}.html")
        with (open(report_path, 'wb')) as fp:
            runner = HTMLTestRunner(stream=fp,
                                    title=Config.ReportTitle,
                                    description=Config.ReportDesc,
                                    tester=Config.ReportTester,
                                    language='zh-CN',
                                    verbosity=2)
            runner.run(testlist=suite, rerun=Config.Rerun, save_last_run=False)
        logger.debug(f"生成测试报告：{report_path}")

    def showconfig(self):
        '''查看所有的配置。eg: python run.py show'''
        for key, value in vars(Config).items():
            if not key.startswith("__"):
                print(f"{key}: {value}")


if __name__ == '__main__':
    fire.Fire(Run)
