"""

css selector este o modalitate prin care putem sa identificam elemente in interfata web pe baza
caracteristicilor de formatare ale unui element (adica pe baza elementelor care servesc la formatare.

Cum se formeaza un CSS Selector?
1. Cautare dupa id: -≥ se face pe baza caracterului #
2. Cautare dupa clasa -≥ se face pe baza caracterului .
3. Daca precedam caracterul # sau caracterul . de numele unui tag atunci sistemul
		va returna toate elementele cu tag-ul respectiv care sunt identificate de
		perechea atribut=valoare (ex: id="gdpr-banner-accept" sau class_name="textbox__control")
4. Putem sa cautam primul copil al unui element cu caracterul >. Exemplu: div > a -≥ am cautat copilul de tip ancora al elementului div
5. Putem sa cautam  primul copil al unui element cu urmatoarea sintaxa: first-of-type
6. Daca vrem sa cautam ultimul copil al unui element cu urmatoarea sintaxa: last-of-type
7. Daca ne intereseaza sa cautam orice copil al unui element putem sa separam tag-ul parinte
		de tag-ul copiil pri caracterul " " (spatiu)
8. Daca vrem sa gasim un frate ulterior ne putem folosi de caracterul "+"

"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from seleniumbase import Driver
from time import sleep

driver = Driver() # am instantiat un obiect din clasa driver
driver.get('https://www.ebay.com/')
# CAUTARE SIMPLA
# driver.find_element(By.CSS_SELECTOR,'#gh-ac').send_keys('iphone')
# driver.find_element(By.CSS_SELECTOR,'.btn-prim').click()
# assert int(driver.find_elements(By.CSS_SELECTOR,'span.BOLD')[16].text.replace(",","")) >= 10000, f"Expected: 65000, Actual: {int(driver.find_elements(By.CSS_SELECTOR,'span.BOLD')[16].text.replace(',',''))}"
#
# # CAUTARE AVANSATA
# driver.find_element(By.CSS_SELECTOR,'#gh-ac').send_keys('iphone')
# dropdown = Select(driver.find_element(By.CSS_SELECTOR,'select[aria-label="Select a category for search"]'))
# dropdown.select_by_visible_text('Computers/Tablets & Networking')
# sleep(4)
# driver.find_element(By.CSS_SELECTOR,'.btn-prim').click()
# driver.find_element(By.CSS_SELECTOR,'button.fake-menu-button__button + span > ul > li > a')

# table#gh-search-wrap > tbody > tr > td:nth-of-type(4) sau table#gh-search-wrap > tbody > tr > td:last-of-type
