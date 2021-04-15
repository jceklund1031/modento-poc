from pages.add_delete_forms import AddRemoveForms
from pages.forms_page import PatientsPage
from pages.sign_in_page import SignInPage
from pages.selected_forms import SelectedForms
from selenium import webdriver
import pytest

class TestSelectedForms:

    @pytest.fixture(autouse=True)
    def class_object_setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://office.modento.io/demo/login")
        self.driver.implicitly_wait(.5)
        self.driver.maximize_window()

        self.ar = AddRemoveForms(self.driver)
        self.fp = PatientsPage(self.driver)
        self.si = SignInPage(self.driver)
        yield
        self.driver.quit()

    def test_user_sees_patient_forms_modal(self):
        self.si.login(username="jon+admin@modento.io", password="9Eiynh9jaH77")
        self.fp.navigate_to_patient_forms_modal()
        self.fp.verify_patient_forms_modal_is_displayed()
        self.ar.remove_form_btn()
        self.ar.add_new_form()
        self.ar.verify_remaining_forms_are_present()
