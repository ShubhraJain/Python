from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.jobserve.com/us/en/Job-Search/")
#driver.find_element_by_xpath(".//*[@id='PolicyOptInLink']").click()
#driver.find_element_by_xpath(".//*[@id='ddcl-selInd']/span/span").click()
#driver.find_element_by_xpath(".//*[@id='ddcl-selInd-ddw']/div/div[1]/label").click()
#for i in range(1, 27, 3):
#    link = ".//*[@id='ddcl-selInd-ddw']/div/div[%d]/label" %i
#   driver.find_element_by_xpath(link).click()
driver.find_element_by_xpath(".//*[@id='txtKey']").click()
input = driver.find_element_by_id("txtKey")
input.send_keys("testing")
driver.find_element_by_xpath(".//*[@id='btnSearch']").click()
driver.find_element_by_xpath(".//*[@id='PolicyOptInLink']").click()
