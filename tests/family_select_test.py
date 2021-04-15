from pages.forms_page import PatientsPage
from pages.sign_in_page import SignInPage
from pages.family_select import FamilySelect
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pytest

class TestFamilySelect:

    @pytest.fixture(autouse=True)
    def class_object_setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://office.modento.io/demo/login")
        self.driver.implicitly_wait(.5)
        self.driver.maximize_window()

        self.fs = FamilySelect(self.driver)
        self.fp = PatientsPage(self.driver)
        self.si = SignInPage(self.driver)
        yield
        self.driver.quit()




    def test_kiosk_features(self):
        self.si.login(username="jon+admin@modento.io", password="9Eiynh9jaH77")
        self.fp.navigate_to_patient_forms_modal()
        self.fp.verify_patient_forms_modal_is_displayed()
        time.sleep(1)
        self.fs.family_initial_setup()
        self.fs.family_send_and_close_button()
        self.fs.verify_form_sent_to_family

      