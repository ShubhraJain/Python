# This program illustrates a technique that can be used on pages that have 
# a captcha.
# A Captha input can never by completely automated via Selenium. Usual workaround
# is to sleep for some time to allow the user (usually the Tester) to enter captcha
# text in input field. 

# But in this example we are using WebDriverWait to allow the tester enough time to
# manually enter the captcha text, but as soon as the captcha is entered, the test can
# proceed. This is better than time.sleep()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
# This opens up contact trainer page on http://hadoopbigdatatutorial.com/
driver.get("http://hadoopbigdatatutorial.com/home/contact_trainer/hadoop-development")

def check_captcha_length(driver):
    """
    This function finds the captcha INPUT element and 
    returns true when length of input text entered
    is greater than 2 characters.
    """
    elem = driver.find_element_by_css_selector("input.captcha_input[name='userCaptcha']")
    return len(elem.get_attribute('value')) > 2

# return true if captcha input is filled with a text of length more than 2 in 30 seconds
result = WebDriverWait(driver, 30).until(check_captcha_length)

# print title of the webpage
print(driver.title)
driver.close()