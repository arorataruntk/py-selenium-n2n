from selenium import webdriver
import time

class RadioButtonsAndCheckBoxes():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        #driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        bmwRadioButton = driver.find_element_by_id("bmwradio")
        bmwRadioButton.click()

        time.sleep(2)

        benzRadioButton = driver.find_element_by_id("benzradio")
        benzRadioButton.click()

        bmwCheckbox = driver.find_element_by_id("bmwcheck")
        bmwCheckbox.click()

        benxCheckbox = driver.find_element_by_id("benzcheck")
        benxCheckbox.click()

        time.sleep(5)
        driver.quit()

ff = RadioButtonsAndCheckBoxes()
ff.test()   