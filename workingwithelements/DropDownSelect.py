from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select 
import time

class DropDownSelect():
    
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("carselect")
        selElement = Select(element)

        selElement.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        selElement.select_by_index("2")
        print("Select Honda by index")
        time.sleep(2)

        selElement.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        selElement.select_by_index(2)   # difference - passed as a number instead of string
        print("Select Honda by index")
        time.sleep(2)


        driver.quit()

ff =  DropDownSelect()
ff.test()