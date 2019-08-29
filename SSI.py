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
        username[0].send_keys('matt.belworthy.lewthwaite@kiwirail.co.nz')
        #find the next button and click it.
        nextButton = self.browser.find_elements_by_xpath("//input[@value='Next']")[0]
        nextButton.click()
        #find the password field and enter the password password.
        password = self.browser.find_elements_by_css_selector("input[name=passwd]")
        password[0].send_keys('Funfun121')
        #explicitly wait for object to be present.
        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@value='Sign in']")))
        #find the login button and click it.
        loginButton = self.browser.find_elements_by_xpath("//input[@value='Sign in']")
        loginButton[0].click()
        #find the no button and click it.
        noButton = self.browser.find_elements_by_xpath("//input[@value='No']")
        noButton[0].click()
        #explicitly wait for the form to be present.
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@name='btnSubmit']")))   

    def tearDown(self):
        print("Tear down begin")
        self.browser.close()

    def test_empty_form(self):
        "Submits a form with no filled in fields and expects an error"
        #find the submit button and click it.
        submitButton = self.browser.find_elements_by_xpath("//a[@name='btnSubmit']")
        print("SUUUUUUUUUUUUUUUUUUUUUUUUUUUB")
        print(submitButton)
        submitButton[0].click()
        #explicitly wait for object to be present.
        testing = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//a[text()='OK']")))
        #find the ok button and click it.
        okButton = self.browser.find_elements_by_xpath("//a[text()='OK']")
        okButton[0].click()

    def test_no_area_conditions(self):
        "Submit form with no area conditions. Expecting missing mandatory fields error"
        #find the region drop down box and change selected field.
        dropDown = self.browser.find_elements_by_xpath("//div[@class='input-control select-box dropdown-box watermark' and @id='b54e7f6c-1707-842e-eae9-89faba43736b_9a91a61f-34da-273c-9bae-0c078787702e']")
        dropDown[0].click()
        selectPlatform = self.browser.find_elements_by_xpath("//ul/li[@title='Auckland']")
        selectPlatform[0].click()
        #find the submit button and click it.
        submitButton = self.browser.find_elements_by_xpath("//a[@name='btnSubmit']")
        submitButton[0].click()
        #explicitly wait for object to be present.
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//a[text()='OK']")))
        #find the ok button and click it.
        okButton = self.browser.find_elements_by_xpath("//a[text()='OK']")
        okButton[0].click()

if __name__ == '__main__':
    unittest.main()

