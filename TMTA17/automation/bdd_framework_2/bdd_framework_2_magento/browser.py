from seleniumbase import Driver

class Browser():
		driver = Driver()
		driver.maximize_window()

		# atunci cand folosim implicit wait instruim sistemul ca atunci cand cauta un element
		# 			web, in cazul in care nu il gaseste din prima sa incerce din nou
		#  timp de x secunde, unde x este specificat intre paranteze sub forma de numar
		# ca argument al metodei implicitly_wait
		driver.implicitly_wait(5)

		# metoda set_page_load_timeout se aplica la metoda get, si instruieste sistemul
		# 		 sa incerce sa creeze o conexiune la aplicatia web pentru o perioada mai lunga
		#  decat perioada standard. Daca pagina se incarca mai devreme nu se va mai astepta
		# restul de timp ramas
		driver.set_page_load_timeout(5)

		def close_browser(self):
				self.driver.quit()