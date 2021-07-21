from selenium import webdriver


class WebDriverClass:

    def getchromedriver(self):
        driver = webdriver.Chrome("D:/Driver/chromedriver.exe")
        driver.implicitly_wait(time_to_wait = 3000)
        return driver
