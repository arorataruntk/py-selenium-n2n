from selenium import webdriver
import time

class ElementState():

    def isEnabled(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Firefox()

        driver.get(baseUrl)
        driver.implicitly_wait(10)

        e1 = driver.find_element_by_name("g")
        e1State = e1.is_enabled()
        print("E1 is enabled? -> " + str(e1State))

        if e1State:
            e1.send_keys("letskodeit")
            time.sleep(5)
        driver.quit()

ff = ElementState()
ff.isEnabled()