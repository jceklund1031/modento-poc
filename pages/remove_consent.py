from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class RemoveConsents(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#locators
    _add_consent = "(//button[@class='btn btn-default btn-sm'])[3]" #click
    _new_consent_lookup = "(//li[@class='category-item'])[3]" #click
    _new_consent_add = "(//li[@class='category-item'])[4]" #click
    _consent_form = "//li[@title='COVID-19 Pandemic Emergency Dental Treatment Consent Form']"
    _remove_new_consent = "(//*[@class='far fa-times-circle action-icon'])[4]"
    
 

   
    def add_new_consent(self):
        self.driver.find_element(By.XPATH, self._add_consent).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self._new_consent_lookup).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self._new_consent_add).click()
        self.driver.find_element(By.XPATH, self._add_consent).click()
        time.sleep(2)


    def verify_consent_is_present(self): # confirming consent is present in field
        verify_consent = self.driver.find_element(By.XPATH, self._consent_form)
        assert verify_consent.is_displayed()

    def remove_added_consent(self):
        self.driver.find_element(By.XPATH, self._remove_new_consent).click()

    def verify_form_no_longer_displayed(self):
        # assert self.driver.find_element(By.XPATH, self._consent_form).is_displayed() is None
        try:
            element = self.driver.find_element(By.XPATH, self._consent_form)
            if element.is_displayed():
                raise Exception("Element should not be found")
        except:
            assert True        