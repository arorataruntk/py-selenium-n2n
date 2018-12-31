from selenium import webdriver

class FindByLinkText():
    
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementbyLinkText = driver.find_element_by_link_text("Login")

        if elementbyLinkText is not None:
            print("We found an element by Link text")
        
        elementbyPartialLinkText = driver.find_element_by_partial_link_text("Pract")

        if elementbyPartialLinkText is not None:
            print("We found an element by Partial Link Text")

        
ff = FindByLinkText()
ff.test()