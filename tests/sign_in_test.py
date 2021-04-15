from selenium import webdriver
import time
# from selenium.webdriver.common.by import By
from pages.sign_in_page import SignInPage


class TestSignIn:

    def test_sign_in(self):
        driver = webdriver.Firefox()
        si = SignInPage(driver)
        
        driver.get("https://office.modento.io/demo/login")
        driver.implicitly_wait(.5)
        driver.maximize_window()

        si.enter_username("jon+admin@modento.io")
        si.enter_password("9Eiynh9jaH77")
        si.click_login_btn()

        time.sleep(3)
        
        si.handle_modal()
        si.verify_avatar_present()

        driver.quit()


        