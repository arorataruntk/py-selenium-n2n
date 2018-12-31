from selenium import webdriver

class ListOfElements():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementListByClassName = driver.find_elements_by_class_name("inputs")

        if elementListByClassName is not None:
            print("Size of the list is: " + str(len(elementListByClassName)))

ff = ListOfElements()
ff.test()