from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # This is where all the common locators and methods across ALL pages be
    def base_page_method(self):
        print(" hi im a base page method")