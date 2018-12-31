from selenium import webdriver

class FindByIdName():
    
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementbyId = driver.find_element_by_id("name")

        if elementbyId is not None:
            print("We found an element by Id")
        
        elementbyName = driver.find_element_by_name("show-hide")

        if elementbyName is not None:
            print("We found an element by Name")

        
ff = FindByIdName()
ff.test()