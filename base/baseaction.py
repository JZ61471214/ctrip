from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Baseaction(object):

    def __init__(self,abc):
        self.driver = abc

    def find_element(self, feature):
        # 自定义元素查找方法
        # 依据用户传入的元素信息特征，然后返回当前用户想要查找的元素
        # feature 元祖类型
        # return self.driver.find_element(feature[0], feature[1])
        # 设置显示等待时的x就是self.driver
        # show_feature = By.XPATH, "//*[@text='显示']"

        by = feature[0]
        value = feature[1]
        wait = WebDriverWait(self.driver, 5, 1)

        if by == By.XPATH:
            return wait.until(lambda x: x.find_element(by, self.make_xpath(value)))
        else:
            return wait.until(lambda x: x.find_element(feature[0], feature[1]))

    def find_elements(self, feature):

        wait = WebDriverWait(self.driver, 5, 1)
        return wait.until(lambda x: x.find_elements(feature[0], feature[1]))

    def click(self, feature):
        # 自定义元素操作
        self.find_element(feature).click()

    def input_txt(self, feature, value):
        """
        依据用户传入的元素特征，找到对应的元素，然后在其中输入我们传入的value值
        :param feature: 元组，表示元素的特征
        :param value: 用户输入的元素
        :return: none
        """
         # self.find_element(feature).send_keys("我是中文")
        self.find_element(feature).send_keys(value)

    def make_xpath(self, feature):
        """
        自定义一个可以拼接xpath的工具函数
        show_feature = By.XPATH, "//*[@text='显示']"
        :return:
        """
        start_path = "//*["
        end_path = "]"
        res_path = ""

        if isinstance(feature, str):

            # 如果是字符串 我们不能直接上来就拆我们可以判断一下它是否是默认正确的 xpath 写法
            if feature.startswith("//*["):
                return feature

            # 如果用户输入的是字符串，那么我们就拆成列表再次进行判断
            split_list = feature.split(",")
            if len(split_list) == 2:
                # //*[contains(@text,'设')]
                res_path = "%scontains(@%s,'%s')%s" % (start_path, split_list[0], split_list[1], end_path)
            elif len(split_list) == 3:
                # //[@text='设置']
                res_path = "%s@%s='%s'%s" % (start_path, split_list[0], split_list[1], end_path)
            else:
                print("请按规则使用")
        elif isinstance(feature, tuple):
            # //*[contains(@text,'设置') and @resource-id='abc']
            for item in feature:
                # 默认用户在元组当中定义的数据都是字符串
                split_list2 = item.split(',')
                if len(split_list2) == 2:
                    # //*[contains(@text,'设')]
                    res_path += "contains(@%s,'%s') and " % (split_list2[0], split_list2[1])
                elif len(split_list2) == 3:
                    # //[@text='设置']
                    res_path += "@%s='%s' and " % (split_list2[0], split_list2[1])
                else:
                    print("请按规则使用")
            andIndex = res_path.rfind(" and")
            res_path = res_path[0:andIndex]
            res_path = start_path + res_path + end_path
        else:
            print("请按规则使用")

        return res_path

    def get_device_size(self):
        # 自定义获取当前设备尺寸的函数
        w = self.driver.get_window_size()["width"]
        h = self.driver.get_window_size()["height"]
        return w, h

    def swipe_left(self):
        # 自定义实现向左滑屏操作
        start_x = self.get_device_size()[0]*0.9
        start_y = self.get_device_size()[1]*0.5
        end_x = self.get_device_size()[0]*0.4
        end_y = self.get_device_size()[1]*0.5
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=300)