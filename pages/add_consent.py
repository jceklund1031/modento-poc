from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class AddConsents(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#locators
    _add_consent = "(//button[@class='btn btn-default btn-sm'])[3]" #click
    _new_consent_lookup = "(//li[@class='category-item'])[3]" #click
    _new_consent_add = "(//li[@class='category-item'])[4]" #click
    _verify_new_consent = "//li[@title='COVID-19 Pandemic Emergency Dental Treatment Consent Form']"
    
 

   
    def add_new_consent(self):
        self.driver.find_element(By.XPATH, self._add_consent).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self._new_consent_lookup).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self._new_consent_add).click()



    def verify_consent_is_present(self): # confirming consent is present in field
        verify_consent = self.driver.find_element(By.XPATH, self._verify_new_consent)
        assert verify_consent.is_displayed()
  