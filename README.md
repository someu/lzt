<div align="center">
  <h1 align="center">UI TEST</h3>
  <p align="center">基于POM模型的UI自动化测试框架。  <p>
</div>


## 关于项目

UI TEST是基于POM模型的UI自动化测试框架。框架中每个测试用例会打开一个浏览器，并有对应的一个或多个页面。框架封装了基础页面类和基础测试用例类，并提供了页面类和测试用例类的模版。测试人员通过命令行生成页面类或测试用例类，能快速的编写测试用例进行测试。目前框架实现的功能有：


- [x] POM模型
- [x] 命令行功能：运行测试、生成测试用例、生成页面
- [x] 测试报告，可截图
- [x] DDT 数据驱动
- [x] 日志输出
- [x] 浏览器代理

![f75d532bc1b84d2aff7fd08c4765a219.jpg](https://image.ppzxxz.xyz/images/2022/04/02/f75d532bc1b84d2aff7fd08c4765a219.jpg)

### 目录结构

```sh
├─.chromedriver     # chrome driver
├─.logs             # 日志文件
├─.result           # 存放测试报告
├─.vscode           # vscode配置
├─case              # 测试用例
├─data              # 存放测试用例使用的数据，通过ddt注入
├─core              # 核心组件
└─page              # 页面
```

## 安装

1. 克隆该项目
   ```sh
   git@github.com:someu/ui-test.git
   ```

2. 安装python依赖

    ```sh
    pip install -r requirements.txt
    ```

3. 下载chromedriver

   1. 在 chrome://settings/help 中查看chrome版本（只需要大版本，例如99）。
   2. 在 https://chromedriver.chromium.org/downloads 中下载本地chrome版本对应的chromedriver。
   
4. 修改`.config.ini`中的配置，如测试报告信息、浏览器代理，日志输出等。
 
## 使用

### 查看所有命令


```sh
python run.py
```

### 新建页面


```sh
python run.py new_page <name>
```

传入的name参数使用下划线命名的方式，会在`page`目录下生成`<name>.py`文件。`page`目录下每个文件都包含了一个页面类，页面类继承于`BasePage`类，上面封装了通用的页面操作方法。而测试人员需要在页面类上添加的内容有：

- 页面URL，等待页面加载的时间
- 该页面的业务逻辑，例如搜索、登录等。
- 元组形式的页面元素的选择器，例如`(By.ID, "input_1")`、`(By.XPATH, "//input")`。

 
### 新建测试用例

```sh
python run.py new_case <name>
```

传入的name参数使用下划线命名的方式，会在`case`目录下生成`test_<name>.py`文件。`case`目录下每个文件都包含了一个测试用例类，测试用例类继承于`BaseCase`类，上面封装了通用的打开关闭浏览器等方法。而测试人员需要在测试用例类上添加的内容有：

- 该测试用例使用的代理、chromedriver路径等配置
- 该测试用例打开的页面
- 测试方法，在测试方法里通过调用页面的业务逻辑来进行测试



框架整合了 `ddt` ，使用`ddt`的案例可以在 `test_bing.py` 的测试用例中查看。

```python
@data("test1", "test2")
    def test_search(self, text):
        '''测试搜索'''
        self.assertIsNotNone(self.bp.search(text), "搜索功能")
```

### 运行测试

```sh
python run.py start
```

输出测试结果在 results 文件夹，格式为`report_yyyymmdd_hhmmss.html`。运行测试的案例：

[![13231c69b5834b3c173d33604f2495b1.jpg](https://image.ppzxxz.xyz/images/2022/04/02/13231c69b5834b3c173d33604f2495b1.jpg)](https://image.ppzxxz.xyz/image/VRD)

### 查看当前配置


```sh
python run.py showconfig
```
输出程序运行时使用的配置，用于检查。

## DDT

框架简单集成了 `ddt` ，在 `test/test_bing.py` 的测试用例上有案例。使用案例如下，通过 `@data` 装饰器，可以往测试方法中传递参数，并将原本的测试方法转化为多个测试方法。下面的例子中 `test_search` 测试方法将会转化为 `test_search_1` `test_search_2` 两个测试方法，分别接收传来的两个参数。如果数据比较多，可以将数据放到 `data` 目录。

```sh
from ddt import ddt, data
# ...

@ddt
class TestBing(BaseCase):
    # ...

    @data("test1", "test2")
    def test_search(self, text):
        # ...
```
## 日志

运行框架生成的日志放到了 `.log` 文件夹，以当天时间命名。日志打印默认为`DEBUG`级别，可以在配置文件中修改打印级别和日志打印格式。

```ini
# ...
# 日志
[log]
level=DEBUG
format=%(asctime)s - %(name)s - %(levelname)-6s - %(filename)-8s : %(lineno)s line - %(message)s
```

## 测试报告

测试报告默认生成在 `.result` 文件夹，可以在配置文件中修改生成位置和相关参数。

```ini
# 测试报告
[report]
output=.result
title=测试报告
tester=Tester
desc=测试报告
```

运行测试时可以截图放到测试报告中，操作方法为：

1. 获取屏幕或元素截图的base64字符串，页面类提供了两个截图的方法：

   - `page.screenshot()`：对当前页面截屏
   - `page.screenshot_element(*loc)`：对元素进行截屏

2. 调用测试用例类的 `append_screenshot` 方法将截图放到测试报告中。

在 `case/test_bing.py` 的测试用例中有截图的案例：
```python
class TestBing(BaseCase):
    # ...
    @data("test1", "test2")
    def test_search(self, text):
        '''测试搜索'''
        self.append_screenshot(self.bp.screenshot())
        self.bp.jump_to_origin()
        self.append_screenshot(self.bp.screenshot())
        self.append_screenshot(self.bp.screenshot_element(*self.bp.Input))
```

测试报告案例：

![175def1825015a9c3c8330bf9cb83699.jpg](https://image.ppzxxz.xyz/images/2022/04/02/175def1825015a9c3c8330bf9cb83699.jpg)

## 页面代理

科学上网访问页面时，页面的请求需要经过代理。框架中配置代理有两种方式：

1. 在配置文件中配置，配置后所有测试用例都将使用代理。
    ```ini
    # 浏览器相关配置
    [browser]
    proxy=https://127.0.0.1:7890
    ```

2. 在单个测试用例中配置，只有配置了的测试用例才使用代理。
    ```python
    class TestGoogle(BaseCase):
        proxy = "socks5://127.0.0.1:1080"
    ```