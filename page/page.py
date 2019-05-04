from page.page_home import HomepageAction


class Page:
    def __init__(self, driver):
        self.driver = driver

    def inithomepage(self):
        return HomepageAction(self.driver)