from selenium.webdriver.common.by import By

from pages.base_page import Base_Page


class LoginPage(Base_Page):
    EMAIL_INPUT = (By.XPATH,'//input[@title="Email"]')
    PASSWORD_INPUT=(By.CSS_SELECTOR,'input[title="Password"]')
    LOGIN_BUTTON = (By.XPATH,'//fieldset//button[@id="send2"]')
    EMAIL_ERROR_MESSAGE = (By.XPATH,'//div[@id="email-error" and @class="mage-error"]')

    def insert_email(self,login_email):
        self.enter_text(*self.EMAIL_INPUT,login_email)
        # self.driver.find_element(*self.EMAIL_INPUT).send_keys(login_email)

    def insert_password(self,login_password):
        self.enter_text(*self.PASSWORD_INPUT,login_password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def check_email_error_message(self, error_message):
        actual_error_message = self.driver.find_element(*self.EMAIL_ERROR_MESSAGE).text
        assert error_message == actual_error_message, f"Error: Expected error message: {error_message}, actual error message: {actual_error_message}"
