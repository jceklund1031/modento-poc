from base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class PatientsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    #locators
    _patient_tab = "//a[@test-id='patients-tab']" #click
    _dots_menu = "(//div[@class='dropdown'])[1]" #click
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

        time.sleep(3)

        self.driver.find_element(By.XPATH, self._prepare_patient_forms).click()

    def verify_patient_forms_modal_is_displayed(self):
        """
        Verifies that the 'Prepare Patient Forms modal is displayed on the UI
        """
        patient_forms_modal_header = self.driver.find_element(By.CLASS_NAME, self._patient_forms_h2)
        assert patient_forms_modal_header.is_displayed()