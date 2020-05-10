from selenium import webdriver
import  time


class Commomshare():


    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def __del__(self):
        time.sleep(3)
        self.driver.close()

    def open_url(self, url):
        self.driver.get(url)

    def __LocateElement(self, locatetype, value):
        if locatetype == "id":
            el = self.driver.find_element_by_id(value)
        elif locatetype == "name":
            el = self.driver.find_element_by_name(value)
        elif locatetype == "class":
            el = self.driver.find_element_by_class_name(value)
        elif locatetype == "tag":
            el = self.driver.find_element_by_tag_name(value)
        elif locatetype == "text":
            el = self.driver.find_element_by_tag_name(value)
        elif locatetype == "partial":
            el = self.driver.find_element_by_partial_link_text(value)
        elif locatetype == "xpath":
            el = self.driver.find_element_by_xpath(value)
        elif locatetype == "css":
            el = self.driver.find_element_by_css_selector(value)


        if el is not None:
            return el

    def click(self, locatetype, value):
        el = self.__LocateElement(locatetype, value)
        el.click()

    def input_data(self, locatetype, value, data):
        el = self.__LocateElement(locatetype, value)
        el.send_keys(data)

    def get_text(self, locatetype, value):
        el = self.__LocateElement(locatetype, value)
        return el.text

    def get_atr(self, locatetype, value, data):
        el = self.__LocateElement(locatetype, value)
        return el.get_attribute(data)




