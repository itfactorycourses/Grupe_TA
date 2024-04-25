import random

from selenium.webdriver.common.by import By

from pages.base_page import Base_Page


class CreateAccountPage(Base_Page):

    CREATE_ACCOUNT_LINK = (By.LINK_TEXT,'Create an Account')
    FIRST_NAME_INPUT = (By.ID,'firstname')
    LAST_NAME_INPUT = (By.ID,'lastname')
    EMAIL_INPUT = (By.ID,'email_address')
    PASSWORD_INPUT = (By.ID,'password')
    CONFIRM_PASSWORD_INPUT = (By.ID,'password-confirmation')
    CLICK_CREATE_ACCOUNT_BUTTON = (By.XPATH,'//button[@type="submit" and @title="Create an Account"]')


    def click_account_link(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_LINK).click()

    def insert_first_name_name(self,first_name):
        self.enter_text(*self.FIRST_NAME_INPUT,first_name)

    def insert_last_name_name(self,last_name):
        self.enter_text(*self.LAST_NAME_INPUT,last_name)


    def insert_create_account_email(self,email):
        number = random.randint(0,999999999999999999999999999999999999999999999999)
        email_input = str(number) + email
        self.enter_text(*self.EMAIL_INPUT,email_input)

    def insert_create_account_password(self,password):
        self.enter_text(*self.PASSWORD_INPUT,password)

    def insert_confirm_password(self, confirm_password):
        self.enter_text(*self.CONFIRM_PASSWORD_INPUT,confirm_password)

    def click_account_button(self):
        self.driver.find_element(*self.CLICK_CREATE_ACCOUNT_BUTTON).click()





