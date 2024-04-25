from time import sleep

from selenium.webdriver.common.by import By
from pages.base_page import Base_Page


class Search_Results_Page(Base_Page):

		SEARCH_RESULTS = (By.XPATH, '//a[@class="product-item-link"]')

		def check_number_of_search_results(self,number_of_results):
				search_results = self.driver.find_elements(*self.SEARCH_RESULTS)
				assert len(search_results) >= int(number_of_results), f'Expected length to be >= {number_of_results}, actual length: {len(search_results)}'

		def check_that_results_are_correct(self,search_value):
				# Am folosit metoda sleep ca sa instruim sistemul sa astepte 10 secunde
				# 		 si apoi sa incerce sa caute elementul in scop
				#  in general sleep-ul nu este folosit decat ca ultima instanta
				# pentru ca poate sa incetinesca codul destul de mult
				sleep(10)
				search_results = self.driver.find_elements(*self.SEARCH_RESULTS)
				is_product_title_correct = True
				for i in range(len(search_results)):
						if search_value not in search_results[i].text.lower():
								is_product_title_correct = False
								break
				assert is_product_title_correct == True, "Error: the product title is not correct"

