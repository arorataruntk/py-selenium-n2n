from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWIthElementsList():

    def testListOfElements(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(By.XPATH, "//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        size = len(radioButtonsList)
        print("Size of the list is: " + str(size))

        for rb in radioButtonsList:
            isSelected = rb.is_selected()
            if not isSelected:
                rb.click()
            time.sleep(2)

        time.sleep(5)
        driver.quit()

ff = WorkingWIthElementsList()
ff.testListOfElements()
