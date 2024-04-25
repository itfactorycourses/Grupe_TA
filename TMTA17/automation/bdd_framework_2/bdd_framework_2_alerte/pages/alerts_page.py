from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AlertsPage(BasePage):

    ALERT_CONFIRM_BUTTON = (By.XPATH, '//button[contains(text(),"Click for JS Alert")]')
    ALERT_JS_CANCEL_BUTTON = (By.CSS_SELECTOR,'button[onclick="jsConfirm()"]')
    ALERT_JS_PROMPT_BUTTON = (By.CSS_SELECTOR,'button[onclick="jsPrompt()"]')
    ALERT_CONFIRM_RESULT_TEXT = (By.ID,'result')

    def click_javascript_alert(self):
        self.driver.find_element(*self.ALERT_CONFIRM_BUTTON).click()

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def check_alert_results_text(self, alert_text):
        actual_text = self.driver.find_element(*self.ALERT_CONFIRM_RESULT_TEXT).text
        assert alert_text == actual_text, f"Error: Expected text: {alert_text}, Actual text: {actual_text}"

    def click_js_confirm_alert(self):
        self.driver.find_element(*self.ALERT_JS_CANCEL_BUTTON).click()

    def cancel_alert(self):
        self.driver.switch_to.alert.dismiss()

    def click_js_prompt_button(self):
        self.driver.find_element(*self.ALERT_JS_PROMPT_BUTTON).click()

    def insert_prompt_text(self,input_prompt):
        alert_prompt = self.driver.switch_to.alert
        alert_prompt.send_keys(input_prompt)
        alert_prompt.acccept()







