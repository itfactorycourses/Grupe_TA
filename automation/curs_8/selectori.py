import time

from selenium.webdriver.common.by import By
from seleniumbase import Driver
					# am importat clasa Driver din fisierul seleniumbase

driver = Driver() # am instantiat un obiect din clasa Driver

# am instruit sistemul sa astepte 10 secunde inainte sa inchida browserul in mod automat
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
time.sleep(2)

''' Toate elementele HTML trebuie sa poata sa fie identificate 
pentru a putea interactiona cu ele. Un astfel de identificator se numeste selector. 

Un selector este un sir de caractere utilizat pentru identificarea elementelor 
html intr-o pagina web

Printre cei mai utilizati si reliable selectori este selectorul de tip id care este
un identificator unic al unui element intr-o pagina web

'''

username = driver.find_element(By.XPATH,'//input[@placeholder="Username"]')
password = driver.find_element(By.XPATH,'//input[@placeholder="Password"]')
time.sleep(1)
username.send_keys('Admin')
time.sleep(1)
password.send_keys('admin123')
time.sleep(1)
login_button = driver.find_element(By.XPATH,'//button[@type="submit"]')
login_button.click()
time.sleep(5)
admin_meniu_option = driver.find_element(By.XPATH,'//a[@href="/web/index.php/admin/viewAdminModule"]')
admin_meniu_option.click()
time.sleep(5)
add_user_button = driver.find_element(By.XPATH,'//button[@type="button" and @class="oxd-button oxd-button--medium oxd-button--secondary"]')
add_user_button.click()
time.sleep(5)
employee_name = driver.find_element(By.XPATH,'//form[@class="oxd-form"]//div[@class="oxd-form-row"]//input[@placeholder="Type for hints..."]')
employee_name.send_keys('praveen kumar ch')
username = driver.find_element(By.XPATH,'//form[@class="oxd-form"]//div[@class="oxd-form-row"]//input[@class="oxd-input oxd-input--active"]')
username.send_keys('jsmith')
# form_dropdown = driver.find_elements(By.XPATH,'//div[@class="oxd-grid-item oxd-grid-item--gutters"]//div[@class="oxd-select-text-input"]')
# form_dropdown[0].click()
password_list = driver.find_elements(By.XPATH,'//input[@class="oxd-input oxd-input--active" and @type="password"]')
password_list[0].send_keys("alabalaportocala1")
password_list[1].send_keys("alabalaportocala1")

lista_mesaje_required = driver.find_elements(By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"]')
is_message_correct = True
for i in range(len(lista_mesaje_required)):
		if lista_mesaje_required[i].text!="Required":
				is_message_correct = False
assert is_message_correct == True, "Error, not all fields are required"

