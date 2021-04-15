from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class FamilySelect(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        driver.wait = WebDriverWait(driver, 5)
        self.driver = driver


    #locators
    _family_radio_btn = "//*[@id='send_to_family_member']" #click
    _select_family_member_dd = "//select[@id='family_members']" #click
    _select_family_option = "//option[@value='1: Object']" #click
    _button_send_close = "//button[@test-id='sendandclose']" #click
    _green_validation = "//div[@role='alertdialog']" #validate the form has been sent by modento
    #api call to confirm the form was delivered

    def family_initial_setup(self):
        self.driver.find_element(By.XPATH, self._family_radio_btn).click()
        #time.sleep(1)
        self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, self._select_family_member_dd))).click()
        self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, self._select_family_option))).click()

    def family_send_and_close_button(self):
        self.driver.find_element(By.XPATH, self._button_send_close).click()

    def verify_form_sent_to_family(self):
        forms_sent_validation = self.driver.find_element(By.XPATH, self._green_validation)
        assert forms_sent_validation.is_displayed()

    