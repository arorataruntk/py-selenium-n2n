from selenium import webdriver

class FindByClassTag():
    
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementbyClassName = driver.find_element_by_class_name("displayed-class")

        if elementbyClassName is not None:
            print("We found an element by Class Name")
        
        elementbyTagName = driver.find_element_by_tag_name("header")

        if elementbyTagName is not None:
            print("We found an element by Tag Name")

        
ff = FindByClassTag()
ff.test()