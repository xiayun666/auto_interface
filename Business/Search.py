from Commonlib.commonlib import Commomshare


class Search(Commomshare):
    def search(self):
        self.open_url("https://www.baidu.com")
        self.input_data("id", "kw", "selenium")
        self.click("id", "su")

    def search_unittest(self):
        self.open_url("https://www.baidu.com")
        self.driver.implicitly_wait(5)
        self.input_data("id", "kw", "unitteest")
        self.click("id", "su")
        self.driver.implicitly_wait(5)
        self.click("xpath", "//div[@id='1']//h3[@class='t']//a[1]")
        self.driver.implicitly_wait(5)
        # self.get_text("id", "cb_post_title_url")




