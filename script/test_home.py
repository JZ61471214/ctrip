from base.initDriver import initDriver
from page.page import Page

class TestDemo:

    def setup(self):
        # 初始化手机对象 -- 打开APP应用
        self.driver = initDriver()
        self.page = Page(self.driver)

    def test_auto_intohome(self):
        # 滑动手机对象进入首页
        self.page.inithomepage().auto_enter_home()
        # ...
