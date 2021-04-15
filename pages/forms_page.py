from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class PatientsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        driver.wait = WebDriverWait(driver, 5)
        self.driver = driver
    
    #locators
    _patient_tab = "//a[@test-id='patients-tab']" #click
    _dots_menu = "(//div[@class='dropdown'])[10]" #click
    _forms_dropdown_option = "(//button[@role='menuitem'])[2]" #hover
    _prepare_patient_forms = "//a[contains(text(),'Prepare patient forms')]" #click
    _patient_forms_h2 = "modal-person-dialog" #class

    # For this test, because all tests should be atomic (independent of one another)
    # You're going to need to start from the beginning for EVERY test.
    # This means you will need to first login to begin.

    # forms_test.py:


    def navigate_to_patient_forms_modal(self):
        self.driver.find_element(By.XPATH, self._patient_tab).click()
        self.driver.find_element(By.XPATH, self._dots_menu).click()

        # Hover over the Forms dropdown item
        action = ActionChains(self.driver)
        forms_menu_item = self.driver.find_element(By.XPATH, self._forms_dropdown_option)
        action.move_to_element(forms_menu_item).perform()

        time.sleep(1)
        self.driver.wait.until(EC.element_to_be_clickable((By.XPATH, self._prepare_patient_forms))).click()

    def verify_patient_forms_modal_is_displayed(self):
        """
        Verifies that the 'Prepare Patient Forms modal is displayed on the UI
        """
        patient_forms_modal_header = self.driver.find_element(By.CLASS_NAME, self._patient_forms_h2)
        assert patient_forms_modal_header.is_displayed()