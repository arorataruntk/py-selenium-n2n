from selenium import webdriver

class FindByXpathCss():
    
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementbyXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementbyXpath is not None:
            print("We found an element by Xpath")
        
        elementbyCss = driver.find_element_by_css_selector("#displayed-text")

        if elementbyCss is not None:
            print("We found an element by Css")

        
ff = FindByXpathCss()
ff.test()