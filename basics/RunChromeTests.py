from selenium import webdriver
import os

class RunChromeTests():

    def test(self):
        driverLocation = "D:\\TKDE\\github\\py-selenium-n2n\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)

        # Open the provided URL
        driver.get("http://www.letskodeit.com")

chrome = RunChromeTests()
chrome.test()