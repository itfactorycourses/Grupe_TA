import time
from unittest import TestCase

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from seleniumbase import Driver

class Magento_login(TestCase):

		SEARCH_INPUT = (By.ID,'search')
		SEARCH_RESULTS = (By.XPATH,'//a[@class="product-item-link"]')
		SORT_DROPDOWN = (By.ID,'sorter')
		SEARCH_RESULTS_PRICES = (By.CSS_SELECTOR,'.price')
		ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR,'button[class="fc-button fc-cta-consent fc-primary-button"')

		def setUp(self) -> None:
				self.driver = Driver()
				self.driver.get('https://magento.softwaretestingboard.com/')
				self.driver.maximize_window()
				self.driver.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

		def tearDown(self) -> None:  # functie care defineste instructiunile care trebuie sa se execute dupa executarea testelor
				self.driver.quit() # inchide driverul si incheie orice instanta a browserului deschisa automat.
		# 	self.driver.close() # inchide doar fereastra curenta, activa, celelalte raman active

		def test_sorting_by_price_descending(self):
				self.driver.find_element(*self.SEARCH_INPUT).send_keys('capri')  # self.driver.find_element(By.ID,'search')
				self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
				sort_dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
				# sort_dropdown.select_by_visible_text("Price")
				sort_dropdown.select_by_value("price")
				search_results_prices = self.driver.find_elements(*self.SEARCH_RESULTS_PRICES)
				is_product_list_sorted_by_price = True
				for i in range(len(search_results_prices)-1): # 0,1,2,3,4,5,6
						for j in range(i+1,len(search_results_prices)): # 1,2,3,4,5,6,7
								if float(search_results_prices[i].text.replace("$","")) < float(search_results_prices[j].text.replace("$","")):
										is_product_list_sorted_by_price = False
										break
				assert is_product_list_sorted_by_price == True, 'Error: sorting is not working properly'

		# def test_check_search_results(self):
				# instructiunea de mai jos nu e corecta pentru ca metoda find_element trebuie sa primeasca
				# doua argumente: tipul selectorului și valoarea selectorului
				# în cazul de mai jos primește drept argument o singură valoare de tip tuplu
				# self.driver.find_element(self.SEARCH_INPUT) # self.driver.find_element((By.ID,'search'))
				# instructiunea de mai jos e corecta pentru ca prin caracterul '*' se despacheteaza tuplul,
				# adică se extrag elementele din interiorul lui

				# am apelat metoda find_element prin intermediul obiectului driver instantiat din clasa Driver
				# pentru a identifica casuta de search prin intermediul selectorului de tip id,
				# iar apoi la rezultatul metodei care este un element web
				# am apelat metoda send_keys care are rolul de a insera text intr-un element web de tip input
				# si am introdus pe acel camp de search valoarea 'capri'
				# self.driver.find_element(*self.SEARCH_INPUT).send_keys('capri')  # self.driver.find_element(By.ID,'search')
				# # am apelat metoda find_element din clasa Driver prin intermediul obiectului instantiat din clasa Driver
				# # pentru a identifica casuta input de cautare
				# # metoda find_element a returnat elementul web corespunzator casutei de input, pentru care
				# # am apelat metoda send_keys ca sa introducem tasta enter pentru a simula momentul in care apasam
				# # enter de la tastatura ca sa incepem cautarea
				# self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
				# am definit o variabila search_results care va stoca rezultatul returnului find_elements care reprezinta
				# o lista cu toate elementele care au titlul capri
				# search_results = self.driver.find_elements(*self.SEARCH_RESULTS)
				# # am scris un assert prin care am evaluat daca lista are cel putin un element (care se traduce in a verifica
				# # daca in urma cautarii a rezultat cel putin produs) - evaluam lungimea listei care lista contine
				# # titlul tuturor produselor returnate in urma apelarii metodei find_elements.
				# # Cate titluri atatea produse returnate
				# assert len(search_results) > 0, f'Expected length to be > 0, actual length: {len(search_results)}'

				# # am declarat o variabila care are ca valoare implicita valoarea True pentru ca pornim de la presumptia
				# # ca in urma cautarii ni se returneaza produsele corecte
				# is_product_title_correct = True
				#
				# # am vrut sa parcurgem intreaga lista care contine titlurile tuturor produselor. Am folosit functia len
				# # ca sa stim marimea listei si sa instruim sistemul de cate ori trebuie sa execute liniile de cod din for
				# for i in range(len(search_results)):
				#
				# 		# Daca textul capri nu se regaseste in rezultatul text[i] care ar trebui primul sa fie 0
				#
				# 		# Am accesat prin intermediul variabilei de iteratie i, care contine indexul elementului curent,
				# 		# elementul web care este stocat in lista in pozitia definita de variabila de iteratie
				# 		# si apoi la acel element web am aplicat proprietatea text care returneaza valoarea textului de pe un element
				# 		# web, care text a fost transformat in lowercase ca sa evitam nepotrivirile din cauza diferentei de case
				# 		# si apoi am evaluat daca textul 'capri' se afla in textul rezultat
				# 		if 'capri' not in search_results[i].text.lower():
				# 				# daca cel putin un titlul al unui produs care respecta conditia din if (adica un produs
				# 				# al carui titlu sa nu contina textul capri) atunci variabila noastra is_product_title_correct va
				# 				# lua valoarea False, care inseamna ca asumptia noastra initiala a fost falsa
				# 				# si ca avem cel putin un produs care nu are titlul corect
				# 				is_product_title_correct = False
				#
				# 				break  # daca gasim cel putin un produs care are titlul in corect, nu vom mai executa celelalte iteratii
				#
				# # am facut un assert pentru a evalua daca prezumptia noastra initiala a fost corecta, adica daca produsele
				# # au titlul corect
				# assert is_product_title_correct == True, "Error: the product title is not correct"

