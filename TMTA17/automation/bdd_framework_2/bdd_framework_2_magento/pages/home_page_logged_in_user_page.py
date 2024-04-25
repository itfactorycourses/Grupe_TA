


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Base_Page


class HomePageLoggedInUserPage(Base_Page):

    CREATE_ACCOUNT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')

    def check_account_created(self):
        current_url = self.driver.current_url
        # am folosit mai jos un explicit wait
        actual_message = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.CREATE_ACCOUNT_SUCCESS_MESSAGE)).text
        actual_message = self.driver.find_element(*self.CREATE_ACCOUNT_SUCCESS_MESSAGE).text

        # actual_message = self.driver.find_element(*self.CREATE_ACCOUNT_SUCCESS_MESSAGE)
        # actual_message = self.driver.find_element(*self.CREATE_ACCOUNT_SUCCESS_MESSAGE).text

        expected_message = 'Thank you for registering with Main Website Store.'
        assert 'create' not in current_url
        assert actual_message == expected_message, (f"Error: Expected message: {expected_message} Actual message: {actual_message}")
