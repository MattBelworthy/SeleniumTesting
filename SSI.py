import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class SSITest(unittest.TestCase):

    def setUp(self):
        #state chromedriver directory.
        self.browser = webdriver.Chrome("C:\Windows\chromedriver")
        self.wait = WebDriverWait(self.browser, 10)
        #navigates you to the K2 SSI Form page.
        self.browser.get('https://forms-uat.kiwirail.co.nz/Designer/Runtime/Form/Site+Safety+Inspection')
        #find the username field and enter the email example@yahoo.com.
        username = self.browser.find_elements_by_css_selector("input[name=loginfmt]")
        username[0].send_keys('username')
        #find the next button and click it.
        nextButton = self.browser.find_elements_by_xpath("//input[@value='Next']")[0]
        nextButton.click()
        #find the password field and enter the password password.
        password = self.browser.find_elements_by_css_selector("input[name=passwd]")
        password[0].send_keys('password')
        #explicitly wait for object to be present.
        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@value='Sign in']")))
        #find the login button and click it.
        loginButton = self.browser.find_elements_by_xpath("//input[@value='Sign in']")
        loginButton[0].click()
        #find the no button and click it.
        noButton = self.browser.find_elements_by_xpath("//input[@value='No']")
        noButton[0].click()
        #explicitly wait for the form to be present.
        #wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@id='00000000-0000-0000-0000-000000000000_3eb2ef74-5721-7727-cc6e-ed79ddc8d125']")))
    
    def tearDown(self):
        print("Tear down begin")
        self.browser.close()

    def test_empty_form(self):
        "Submits a form with no filled in fields and expects an error"
        #find the submit button and click it.
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@name='btnSubmit']")))
        submitButton = self.browser.find_elements_by_xpath("//a[@name='btnSubmit']")
        submitButton[0].click()
        #explicitly wait for object to be present.
        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='pop-up-header-text']")))
        #find the ok button and click it.
        okButton = self.browser.find_elements_by_xpath("//a[@id='messageBoxButton_OK1566861689691']")
        okButton[0].click()

if __name__ == '__main__':
    unittest.main()

