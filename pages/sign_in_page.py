from base.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class SignInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username_field = "username"
    _password_field = "password"
    _login_button = "submit"
    _modal = "modal-content"
    _disable_notif = ".//button[@test-id='disablenotyfications']"
    _avatar = ".//img[@class='avatar']"

    def enter_username(self, username):
        username_field = self.driver.find_element(By.NAME, self._username_field)
        username_field.click()
        username_field.send_keys(username)

    def enter_password(self, password):
        pw_field = self.driver.find_element(By.NAME, self._password_field)
        pw_field.click()
        pw_field.send_keys(password)

    def click_login_btn(self):
        login_btn = self.driver.find_element(By.ID, self._login_button)
        login_btn.click()

    def handle_modal(self):
        """
        Upon a fresh login, user will see a 'Enable alerts' modal we want to dismiss
        """
        try:
            time.sleep(2)
            modal = self.driver.find_element(By.CLASS_NAME, self._modal)
            if modal:
                disable_notif = self.driver.find_element(By.XPATH, self._disable_notif)
                print("found the disable notif")
                disable_notif.click()
        except:
            print("modal not present")

    def verify_avatar_present(self):
        dashboard_element = self.driver.find_element(By.XPATH, self._avatar)
        print("Found avatar!")
        assert dashboard_element.is_displayed()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_btn()
        self.handle_modal()