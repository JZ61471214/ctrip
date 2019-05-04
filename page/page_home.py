import random
import time

from selenium.webdriver.common.by import By

from base.baseaction import Baseaction


class HomepageAction(Baseaction):
    """
    home页中的所有动作都存放于当前，业务逻辑仅存放script中 继承实现self使用不报错
    """
    into_feature1 = By.XPATH, "text,跳过"
    into_feature2 = By.XPATH, "text,立即体验"
    into_feature3 = By.XPATH, "text,首页"

    def auto_enter_home(self):
        time.sleep(15)
        # 判断是否需要进行滑屏操作
        try:
            self.find_element(self.into_feature3)
            print("欢迎来到首页")
        except:
            # 没有直接进入首页时，需进行判断
            # 执行2次滑屏操作 点击'立即体验' 进入首页
            int01 = random.choice([1, 2])
            # int01 = random.randint(1,2)
            if int01 == 1:
                self.find_element(self.into_feature1)
                self.click(self.into_feature1)
                print("欢迎来到首页1")
            else:
                for i in range(2):
                    self.swipe_left()
                    time.sleep(1)
                self.click(self.into_feature2)
                print("欢迎来到首页2")



















