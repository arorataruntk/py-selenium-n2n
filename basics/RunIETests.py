from selenium import webdriver
import os

class RunIETests():

    def test(self):
        driverLocation = "D:\\TKDE\\github\\py-selenium-n2n\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driverLocation
        driver = webdriver.Ie(driverLocation)
        driver.get("http://www.letskodeit.com")

Ie = RunIETests()
Ie.test()