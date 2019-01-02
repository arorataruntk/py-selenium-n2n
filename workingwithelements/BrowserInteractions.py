from selenium import webdriver

class BrowserInteractions():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        
        # Window Maximize
        driver.maximize_window()

        # Open the URL        
        driver.get(baseUrl)

        # Get Title
        title = driver.title
        print("Title of the Page: " + title)

        # Get current url
        currentUrl = driver.current_url
        print("Current Url of the web page is " + currentUrl)

        # Browser Refresh
        driver.refresh()
        print("Browser refreshed 1st time")

        driver.get(driver.current_url)
        print("Browser refreshed 2nd time")

        # Open another URL
        driver.get("https://www.google.co.in")

        # Browse back
        driver.back()
        print("Go one step back in browser history")

        # Browse forward
        driver.forward()
        print("Go one step forward in browser history")
        
        # Get page source
        pageSource = driver.page_source
        
        # Browser Close / Quit
        driver.quit()


ff = BrowserInteractions()
ff.test()