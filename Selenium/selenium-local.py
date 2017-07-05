from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get("file:///Users/shubhra/Desktop/Coding/remote_python/Selenium/test.html")
assert "LOCAL" in driver.title

lst = driver.find_elements_by_xpath("//div[@class='foo']/h3/a")
print(len(lst))
print([l.text for l in lst])