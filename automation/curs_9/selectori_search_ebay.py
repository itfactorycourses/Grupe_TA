# atunci cand cautam un element in html dupa o pereche atribut=valoare, ele trebuie puse intre []
# perechile atribut valaore sunt intotdeauna puse pe tag-ul de inceput al elementului web
			# si ele sunt separate de caracterul =
			# ele serversc fie drept identificatori pentru element (id) , fie au rol de stilizare (clasa)
			# sau rol de definire (placeholder)

# Cateva dintre aceste perechi atribut=valaore sunt:
# - id
# - classname
# - name
# - aria-label
# - role
# - type

# CAUTARE DUPA NUME
# Scenariu: Vrem sa identificam un element de tip input de pe ebay care are rolul de cautare si sa introducem o valoare de cautare
from selenium.webdriver.common.by import By
from seleniumbase import Driver
from time import sleep

driver = Driver() # am instantiat un obiect din clasa driver
driver.get('https://www.ebay.com/')
driver.find_element(By.NAME,'_nkw').send_keys('iphone')

# Cautarea dupa tag name
# un tag este eticheta care da numele elementului HTML. Exemple de tag-uri:
# div, p (paragraph), a (anchor), table, tr (table row), td (table data), input, h1 (header)
# ul(unordered list), ol(ordered list), li(list item), form, span, tbdoy (table body), header, label

input_list = driver.find_elements(By.TAG_NAME,'input')
input_list[4].click()
sleep(4)
search_results = driver.find_elements(By.CLASS_NAME,'BOLD')
number_of_items_returned = search_results[16].text.replace(",","")
assert int(number_of_items_returned) >= 10000, f'Expected: 65000, Actual: {number_of_items_returned}'

# assert este traducerea in engleza pentru cuvantul verifica
# assertul de mai sus este tradus in felul urmator:
		# verifica faptul ca dupa conversia la numar intre, numarul de elemente returnate in urma cautarii
				# este >= 10000. Daca aceasta conditie nu este respectata,
				# atunci ne va returna eroare: f'Expected: 65000, Actual: {number_of_items_returned}'

