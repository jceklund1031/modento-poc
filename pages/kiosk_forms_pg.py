from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class KioskForms(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        driver.wait = WebDriverWait(driver, 5)
        self.driver = driver


    #locators
    _kiosk_radio_btn = "//*[@id='send_to_kiosk']" #click
    _kiosk_device_dd = "//*[@id='kiosk_device_id']" #click
    _kiosk_device_dd_opt = "(//option[@class='ng-star-inserted'])[2]" #click 
    _button_send_close = "//button[@test-id='sendandclose']" #click
    _green_validation = "//div[@role='alertdialog']" #validate the form has been sent by modento
    #api call to confirm the form was delivered

    def kiosk_initial_setup(self):
        self.driver.find_element(By.XPATH, self._kiosk_radio_btn).click() #selecting kiosk radio btn
        self.driver.find_element(By.XPATH, self._kiosk_device_dd).click() #selecting the kiosk dropdown
        self.driver.find_element(By.XPATH, self._kiosk_device_dd_opt).click() #selecting within the dropdown


    def kiosk_send_and_close_button(self):
        self.driver.find_element(By.XPATH, self._button_send_close).click() #send & close btn

    def verify_form_sent_to_kiosk(self):
        forms_sent_validation = self.driver.wait.until(EC.visibility_of_element_located((By.XPATH, self._green_validation)))
        assert forms_sent_validation.is_displayed() #verify we get the green alert box