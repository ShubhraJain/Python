from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BBCPage():

    def __init__(self, driver):
        self.driver = driver
        self.openBBC()

    def openBBC(self):
        self.driver.get("http://bbc.com")
        # assert "BBC - Homepage" in self.driver.title
        self.driver.implicitly_wait(3)

    def findMultipleElements(self):
        return self.driver.find_elements_by_tag_name("a")

    def getNavigationLinks(self):
        nav_link = driver.find_element_by_id("orb-nav-links")
        return nav_link.find_elements_by_tag_name("a")


class RediffPage():

    def __init__(self, driver):
        self.driver = driver
        self.openRediff()

    def openRediff(self):
        self.driver.get("http://shopping.rediff.com/")
        self.driver.implicitly_wait(20)

    def getProductCatLinks(self):        
        nav_link = self.driver.find_element_by_xpath('id("popular_cat")')
        return nav_link.find_elements_by_tag_name("a")


def visitAllLinksSlow():
    driver = webdriver.Firefox()
    rediff = RediffPage(driver)
    l = len(elements)
    for i in range(l):
        e = elements[i]
        if e.is_displayed():
            e.click()
            print(driver.title + "\n")
            rediff.openRediff()
            elements = rediff.getProductCatLinks()
            for e in elements:
                print("Navlinks: ", e.text)

    driver.close()

def visitAllLinksFast():
    driver = webdriver.Firefox()
    rediff = RediffPage(driver)
    l = len(rediff.getProductCatLinks())
    for i in range(1, 3):
        driver.find_element_by_xpath("id(\"popular_cat\")/h3[%d]/a[1]" %(i)).click()
        print(driver.title)
        driver.back()

    driver.close()

visitAllLinksFast()