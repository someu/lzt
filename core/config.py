# encoding=utf-8

from os import path
from configparser import ConfigParser

_base_path = path.split(path.dirname(path.abspath(__file__)))[0]
_config_path = path.join(_base_path, '.config.ini')

_config = ConfigParser()
_config.read(_config_path, encoding='UTF-8')

_core_path = path.join(_base_path, "core")
_template_path = path.join(_core_path, "templates")


class Config():
    '''配置'''
    # 路径
    BasePath = _base_path
    CaseDirPath = path.join(_base_path, "case")
    PageDirPath = path.join(_base_path, "page")
    TestCaseTemplatePath = path.join(_template_path, "case_template.py")
    PageTemplatePath = path.join(_template_path, "page_template.py")

    # 报告
    ReportOutput = path.join(_base_path, _config.get("report", "output"))
    ReportTitle = _config.get("report", "title")
    ReportTester = _config.get("report", "tester")
    ReportDesc = _config.get("report", "desc")

    # 日志
    LogDirPath = path.join(_base_path, _config.get("log", "output"))
    LogLevel = _config.get("log", "level")
    LogFormat = _config.get("log", "format", raw=True)

    # 浏览器
    Headless = _config.getboolean("browser", "headless")
    Proxy = _config.get("browser", "proxy")
    ExecutablePath = path.join(_base_path,
                               _config.get("browser", "executable_path"))
    ImplicitlyWaitTime = _config.getint("browser", "implicitly_wait_time")
    BrowserWidth = _config.get("browser", "width")
    BrowserHeight = _config.get("browser", "height")
    MaximizeWindow = _config.getboolean("browser", "maximize_window")

    # 测试用例运行
    Rerun = _config.getint("case", "rerun")