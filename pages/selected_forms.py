from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class SelectedForms(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #locators
    _select_qr_code = "//input[@id='qrcode']" #click
    _select_pt_initial = "//input[@id='authorize']" #click
    _selected_minor_form = "//input[@id='for_minor']" #click
    _verify_np_form = "//li[@title='New Patient Form']"
    _verifiy_hh_form = "//li[@title='Health History']"
    _verify_dh_form = "//li[@title='Dental History']"
    _green_validation = "//div[@role='alertdialog']" #validate the form has been sent by modento
    #api call to confirm the form was delivered

    def form_check_box(self):
        self.driver.find_element(By.XPATH, self._select_qr_code).click()
        self.driver.find_element(By.XPATH, self._select_pt_initial).click()
    
    def form_check_box_unclick(self):
        self.driver.find_element(By.XPATH, self._select_qr_code).click()
        self.driver.find_element(By.XPATH, self._select_pt_initial).click()

    def verify_forms_are_present(self): # confirming np,hh,dh are all present in forms field
        np_form_present = self.driver.find_element(By.XPATH, self._verify_np_form)
        assert np_form_present.is_displayed()
        hh_form_present = self.driver.find_element(By.XPATH, self._verifiy_hh_form)
        assert hh_form_present.is_displayed()
        dh_form_present = self.driver.find_element(By.XPATH, self._verify_dh_form)
        assert dh_form_present.is_displayed()
    
    def minor_form_checkbox(self):
        self.driver.find_element(By.XPATH, self._selected_minor_form).click()
    
    def minor_form_checkbox_unclick(self):
        self.driver.find_element(By.XPATH, self._selected_minor_form).click()
  