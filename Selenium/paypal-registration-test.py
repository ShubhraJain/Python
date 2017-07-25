# This tests the sign up page of Paypal.com 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class paypalRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.paypal.com/")
        self.driver.implicitly_wait(20)
        #Click on sign up button
        signUpButton = self.driver.find_element_by_id("signup-button")
        signUpButton.click()
        # Assert opened page is as expected
        assert "It’s a secure, easy way to pay and get paid" in self.driver.title
        self.driver.find_element_by_id("cta-btn").click()
        # Check the title of new page
        WebDriverWait(self.driver, 100).until(lambda x: x.find_element_by_id(
                                        "paypalAccountData_confirmPassword").is_displayed())

    def test_AllBlankFields(self):
        print("test_AllBlankFields")
        nextButton = self.driver.find_element_by_id("/appData/action")
        nextButton.click()
        assert self.driver.find_element_by_css_selector(
                "span.vx_form-control-error-icon.icon.icon-small.icon-critical-small").is_displayed()

    def test_EmptyFirstName(self):
        """
        Asserts error icon is seen on the page when
        firstname is not entered
        """
        print("test_EmptyFirstName")
        lname = self.driver.find_element_by_id("paypalAccountData_lastName")
        lname.send_keys("xyxy")
        email = self.driver.find_element_by_id("paypalAccountData_email")
        email.send_keys("xyz@abc.com")
        pwd = self.driver.find_element_by_id("paypalAccountData_password")
        pwd.send_keys("password101")
        cnfrmPwd = self.driver.find_element_by_id("paypalAccountData_confirmPassword")
        cnfrmPwd.send_keys("password101")
        nextButton = self.driver.find_element_by_id("/appData/action")
        nextButton.click()
        assert self.driver.find_element_by_css_selector(
                "span.vx_form-control-error-icon.icon icon-small.icon-critical-small").is_displayed()

    def test_EmptyLastName(self):
        """
        Asserts error icon is seen on the page when
        lastname is not entered
        """
        print("test_EmptyLastName")
        fname = self.driver.find_element_by_id("paypalAccountData_firstName")
        fname.send_keys("abcd")
        email = self.driver.find_element_by_id("paypalAccountData_email")
        email.send_keys("xyz@abc.com")
        pwd = self.driver.find_element_by_id("paypalAccountData_password")
        pwd.send_keys("password101")
        cnfrmPwd = self.driver.find_element_by_id("paypalAccountData_confirmPassword")
        cnfrmPwd.send_keys("password101")
        nextButton = self.driver.find_element_by_id("/appData/action")
        nextButton.click()
        assert self.driver.find_element_by_css_selector(
                "span.vx_form-control-error-icon.icon icon-small.icon-critical-small").is_displayed()

    def test_EmptyEmail(self):
        """
        Asserts error icon is seen on the page when
        email address is not entered
        """
        print("test_EmptyEmail")
        fname = self.driver.find_element_by_id("paypalAccountData_firstName")
        fname.send_keys("abcd")
        lname = self.driver.find_element_by_id("paypalAccountData_lastName")
        lname.send_keys("xyxy")
        pwd = self.driver.find_element_by_id("paypalAccountData_password")
        pwd.send_keys("password101")
        cnfrmPwd = self.driver.find_element_by_id("paypalAccountData_confirmPassword")
        cnfrmPwd.send_keys("password101")
        nextButton = self.driver.find_element_by_id("/appData/action")
        nextButton.click()
        assert self.driver.find_element_by_css_selector(
                "span.vx_form-control-error-icon.icon icon-small.icon-critical-small").is_displayed()

    def test_EmptyPwd(self):
        """
        Asserts error icon is seen on the page when
        password and confirm password fields are blank
        """
        print("test_EmptyPwd")
        fname = self.driver.find_element_by_id("paypalAccountData_firstName")
        fname.send_keys("abcd")
        lname = self.driver.find_element_by_id("paypalAccountData_lastName")
        lname.send_keys("xyxy")
        email = self.driver.find_element_by_id("paypalAccountData_email")
        email.send_keys("xyz@abc.com")
        nextButton = self.driver.find_element_by_id("/appData/action")
        nextButton.click()
        assert self.driver.find_element_by_css_selector(
                "span.vx_form-control-error-icon.icon icon-small.icon-critical-small").is_displayed()

    def test_DifferentPwdAndCnfrmPwd(self):
        """
        Asserts error icon is seen on the page when
        password and confirm password don't match
        """
        print("test_DifferentPwdAndCnfrmPwd")
        fname = self.driver.find_element_by_id("paypalAccountData_firstName")
        fname.send_keys("abcd")
        lname = self.driver.find_element_by_id("paypalAccountData_lastName")
        lname.send_keys("xyxy")
        email = self.driver.find_element_by_id("paypalAccountData_email")
        email.send_keys("xyz@abc.com")
        pwd = self.driver.find_element_by_id("paypalAccountData_password")
        pwd.send_keys("password101")
        cnfrmPwd = self.driver.find_element_by_id("paypalAccountData_confirmPassword")
        cnfrmPwd.send_keys("101password")
        nextButton = self.driver.find_element_by_id("/appData/action")
        nextButton.click()
        assert self.driver.find_element_by_css_selector(
                "span.vx_form-control-error-icon.icon icon-small.icon-critical-small").is_displayed()

    def test_ExistingEmail(self):
        """
        Asserts message "It looks like you already signed up. 
        Log in to your account." if user has already signed up 
        using that email address.
        """
        print("test_ExistingEmail")
        fname = self.driver.find_element_by_id("paypalAccountData_firstName")
        fname.send_keys("abcd")
        lname = self.driver.find_element_by_id("paypalAccountData_lastName")
        lname.send_keys("xyxy")
        email = self.driver.find_element_by_id("paypalAccountData_email")
        email.send_keys("xyz@abc.com")
        self.assertIn("It looks like you already signed up.", 
                 self.driver.find_element_by_css_selector(
                            "div.vx_form-control-message > p > span.title"))

    def test_CorrectInputs(self):
        """
        Asserts when all inputs are correct, user is navigated
        to next page for creating the account.
        """
        print("test_CorrectInputs")
        fname = self.driver.find_element_by_id("paypalAccountData_firstName")
        fname.send_keys("abcd")
        lname = self.driver.find_element_by_id("paypalAccountData_lastName")
        lname.send_keys("xyxy")
        email = self.driver.find_element_by_id("paypalAccountData_email")
        email.send_keys("sjpadhai@gmail.com")
        pwd = self.driver.find_element_by_id("paypalAccountData_password")
        pwd.send_keys("p@ssword1")
        cnfrmPwd = self.driver.find_element_by_id("paypalAccountData_confirmPassword")
        cnfrmPwd.send_keys("p@ssword1")
        nextButton = self.driver.find_element_by_id("/appData/action")
        nextButton.click()
        self.assertEqual(self.driver.find_element_by_id("/appData/action").text, 
                         "Agree and Create Account")
        
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

