import time
import unittest

from selenium.webdriver.common.by import By
from seleniumbase import Driver


class Test_Login(unittest.TestCase):
    ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, 'button[class="fc-button fc-cta-consent fc-primary-button"')
    SIGN_IN_LINK = (By.LINK_TEXT, 'Sign In')
    SIGN_IN_BUTTON = (By.XPATH, '//button[@class="action login primary"]')
    REQUIRED_FIELD_ERROR = (By.XPATH, '//*[@class="input-text mage-error"]//following-sibling::div')

    def setUp(self) -> None:
        self.driver = Driver()
        self.driver.get('https://magento.softwaretestingboard.com/')
        self.driver.maximize_window()
        self.driver.find_element(*self.ACCEPT_COOKIES_BUTTON).click()
        self.driver.find_element(*self.SIGN_IN_LINK).click()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_check_sign_in_not_possible_when_user_and_pass_empty(self):
        time.sleep(5)
        sign_in_button = self.driver.find_element(*self.SIGN_IN_BUTTON)
        sign_in_button.click()

        # metoda is_displayed valideaza daca elementul este vizibil pe pagina, nu daca exista in html
        # daca elementul nu exista in html se va returna eroarea NoSuchElement Exception
        required_field_errors = self.driver.find_elements(*self.REQUIRED_FIELD_ERROR)
        is_error_message_correct = True
        for i in range(len(required_field_errors)):
            if required_field_errors[i].text != 'This is a required field.':
                is_error_message_correct = False
        is_button_displayed = sign_in_button.is_displayed()
        try:
            assert is_button_displayed == True, "Error: The login button is not displayed"
            assert is_error_message_correct == True, "Error, at least one field is not marked as required"
        except AssertionError as msg:
            raise ValueError(msg)
