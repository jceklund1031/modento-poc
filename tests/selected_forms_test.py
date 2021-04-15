from pages.forms_page import PatientsPage
from pages.sign_in_page import SignInPage
from pages.selected_forms import SelectedForms
from selenium import webdriver
import time
import pytest

class TestSelectedForms:

    @pytest.fixture(autouse=True)
    def class_object_setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://office.modento.io/demo/login")
        self.driver.implicitly_wait(.5)
        self.driver.maximize_window()

        self.sf = SelectedForms(self.driver)
      
        self.fp = PatientsPage(self.driver)
        self.si = SignInPage(self.driver)
        yield
        self.driver.quit()

    def test_user_sees_patient_forms_modal(self):
        self.si.login(username="jon+admin@modento.io", password="9Eiynh9jaH77")
        self.fp.navigate_to_patient_forms_modal()
        self.fp.verify_patient_forms_modal_is_displayed()
        time.sleep(1)
        self.sf.form_check_box()
        time.sleep(1)
        self.sf.form_check_box_unclick()
        self.sf.verify_forms_are_present()
        self.sf.minor_form_checkbox()
        self.sf.minor_form_checkbox_unclick()