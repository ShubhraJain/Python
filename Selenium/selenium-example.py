from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GmailPage:

    def __init__(self, driver):
        self.driver = driver
        self.openGmail()

    def openGmail(self):
        self.driver.get("http://bbc.com")
        # assert "Gmail" in self.driver.title
        driver.implicitly_wait(5)

    # def getEmailInputElement(self):
    #     return self.driver.find_element_by_xpath(".//*[@id='identifierId']")

    # def getHelp(self):
    #     return self.driver.find_element_by_xpath(".//a[text()='Help']").click()

    def clickUsingCssSelector(self):
        return self.driver.find_element_by_css_selector("div[id='orb-nav-links'] ul li:nth-child(4) a")

driver = webdriver.Firefox()

gp = GmailPage(driver)
# element = gp.getEmailInputElement()
# element = gp.clickHelp()
element = gp.clickUsingCssSelector()
print(element.text)
# element.send_keys("haha")
# text = element.get_attribute("value")
# print(text)
# element.clear()

driver.close()
