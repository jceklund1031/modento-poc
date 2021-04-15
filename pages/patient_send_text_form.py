from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class PatientTextForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #locators
    _patient_radio_btn = "//*[@id='send_to_patient']" #click
    _text_radio_btn = "//input[@id='channel_sms']" #click
    _just_send_btn = "//button[@test-id='justsend']" #click
    _green_validation = "//div[@role='alertdialog']" #validate the form has been sent by modento
    #api call to confirm the form was delivered

    def patient_option_radio(self):
        self.driver.find_element(By.XPATH, self._patient_radio_btn).click()

    def text_patient_option(self):
        self.driver.find_element(By.XPATH, self._text_radio_btn).click()

    def send_btn(self):
        self.driver.find_element(By.XPATH, self._just_send_btn).click()

    def verify_form_sent(self):
        forms_sent_validation = self.driver.find_element(By.XPATH, self._green_validation)
        assert forms_sent_validation.is_displayed()
