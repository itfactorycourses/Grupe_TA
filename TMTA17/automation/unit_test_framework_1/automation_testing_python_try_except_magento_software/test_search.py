import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from seleniumbase import Driver


class Magento_search(unittest.TestCase):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_RESULTS = (By.XPATH, '//a[@class="product-item-link"]')
    SORT_DROPDOWN = (By.ID, 'sorter')
    SEARCH_RESULTS_PRICES = (By.CSS_SELECTOR, '.price')
    ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, 'button[class="fc-button fc-cta-consent fc-primary-button"')

    def setUp(self) -> None:
        self.driver = Driver()
        self.driver.get('https://magento.softwaretestingboard.com/')
        self.driver.maximize_window()
        self.driver.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_sorting_by_price_descending(self):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys('capri')
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
        sort_dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        sort_dropdown.select_by_value("price")
        search_results_prices = self.driver.find_elements(*self.SEARCH_RESULTS_PRICES)
        is_product_list_sorted_by_price = True
        for i in range(len(search_results_prices) - 1):  # 0,1,2,3,4,5,6
            for j in range(i + 1, len(search_results_prices)):  # 1,2,3,4,5,6,7
                if float(search_results_prices[i].text.replace("$", "")) < float(
                        search_results_prices[j].text.replace("$", "")):
                    is_product_list_sorted_by_price = False
                    break
        try:
            assert is_product_list_sorted_by_price == True
        except AssertionError as msg:
            raise ValueError(msg)

    def test_check_search_results(self):
        self.driver.find_element(*self.SEARCH_INPUT).send_keys('capri')  # self.driver.find_element(By.ID,'search')
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)
        search_results = self.driver.find_elements(*self.SEARCH_RESULTS)
        assert len(search_results) > 0, f'Expected length to be > 0, actual length: {len(search_results)}'
        is_product_title_correct = True
        for i in range(len(search_results)):
            if 'capri' not in search_results[i].text.lower():
                is_product_title_correct = False
                break

        # am pus assertul pe un try (adica am instruit sistemul sa incerce sa execute assertul)
        try:
            assert is_product_title_correct == True, "The title is not correct for at least one product"
        # in caz ca assertul returneaza eroare, o sa instruim sistemul sa trateze acea eroare
        except AssertionError as msg:
            raise ValueError(msg)

#  try except este o modalitate prin care putem sa tratam exceptiile.
#  sunt unele situatii in care unele linii de cod nu se comporta asa cum ne-am dori,
# 		sau situatii in care unele erori sunt asteptate
#  de exemplu, daca vrem sa verificam ca dupa logare butonul de login nu mai este afisat,
# putem folosi metoda is_displayed(), dar aceasta metoda returneaza ceva doar daca
#  elementul exista in html. in caz contrar returneaza nosuchelement exception
# fiind o eroare asteptata, nu vrem sa ne crape testul din cauza asta. Si atunci
#  putem sa punem apelarea metodei intr-o structura try except, care pe scrurt
# inseamna ca instruim sistemul sa faca ceva (try) si in caz ca acea instructiune sau acel set
# 		de instructiuni returneaza eroare sa execute un alt set de instructiuni implicite (except)
