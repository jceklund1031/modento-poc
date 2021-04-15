from pages.forms_page import PatientsPage
from pages.sign_in_page import SignInPage
from pages.remove_consent import RemoveConsents
from selenium import webdriver
import pytest

class TestSelectedForms:

    @pytest.fixture(autouse=True)
    def class_object_setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://office.modento.io/demo/login")
        self.driver.implicitly_wait(.5)
        self.driver.maximize_window()

        self.rc = RemoveConsents(self.driver)
        self.fp = PatientsPage(self.driver)
        self.si = SignInPage(self.driver)
        yield
        self.driver.quit()

    def test_user_sees_patient_forms_modal(self):
        self.si.login(username="jon+admin@modento.io", password="9Eiynh9jaH77")
        self.fp.navigate_to_patient_forms_modal()
        self.fp.verify_patient_forms_modal_is_displayed() # Assert == True

        self.rc.add_new_consent()
        self.rc.verify_consent_is_present() # Assert == True

        self.rc.remove_added_consent()
        self.rc.verify_form_no_longer_displayed()
       