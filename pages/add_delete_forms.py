from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class AddRemoveForms(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#locators
    #_verify_np_form = "//li[@title='New Patient Form']"
    _remove_np_form = "(//*[@class='far fa-times-circle action-icon'])[1]"
    _add_form = "//button[@test-id='addform']"
    _new_form_add = "(//li[@class='category-item'])[4]"
    _verifiy_hh_form = "//li[@title='Health History']"
    _verify_dh_form = "//li[@title='Dental History']"
    _verify_new_form = "//li[@title='COVID-19 Questionnaire']"
    _green_validation = "//div[@role='alertdialog']" #validate the form has been sent by modento
    #api call to confirm the form was delivered

    def remove_form_btn(self):
        self.driver.find_element(By.XPATH, self._remove_np_form).click()

    def add_new_form(self):
        self.driver.find_element(By.XPATH, self._add_form).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self._new_form_add).click()


    def verify_remaining_forms_are_present(self): # confirming,hh,dh are all present in forms field
       
        # np_form_present = self.driver.find_element(By.XPATH, self._verify_np_form)
        # assert np_form_present.is_displayed()
        hh_form_present = self.driver.find_element(By.XPATH, self._verifiy_hh_form)
        assert hh_form_present.is_displayed()
        dh_form_present = self.driver.find_element(By.XPATH, self._verify_dh_form)
        assert dh_form_present.is_displayed()
        covid_form_present = self.driver.find_element(By.XPATH, self._verify_new_form)
        assert dh_form_present.is_displayed()
  