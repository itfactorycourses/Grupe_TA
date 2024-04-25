from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from seleniumbase import Driver

driver = Driver()
driver.get('https://www.ebay.com/')
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'Advanced').click()
driver.find_element(By.ID,'_nkw').send_keys('iphone')
dropdown_keyword_options = Select(driver.find_element(By.CSS_SELECTOR,'select[aria-label="Keyword options"]'))
dropdown_keyword_options.select_by_visible_text('All words, any order')
# driver.find_element(By.XPATH,'//button[@class="btn btn--primary" and @type="submit"]').click()
# driver.find_element(By.XPATH,'//button[contains(text(),"Search")]')
# driver.find_element(By.XPATH,'//button[text()="Search"]')
# driver.find_element(By.XPATH,'//fieldset[@class="adv-fieldset__keyword"]//button[text()="Search"]')
driver.find_element(By.XPATH,'//div[@class="field adv-keywords__btn-help"]//button[text()="Search"]').click()
