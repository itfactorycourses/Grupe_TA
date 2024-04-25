'''

Selectorii de tip XPATH sunt cei care sunt creati pe baza pozitiei elementului
		in codul HTML

Exista doua tipuri de selectori:
1. XPATH Absolut este cel care contine calea completa a elementului
		de la inceputul fisierului pana in momentul in care acesta este identificat
		Aceasta metoda nu va fi folosita NICIODATA pentru ca nu este reliable
		in ideea in care daca un alt element este adaugat inainte de elementul
		nostru, toata calea se va strica si va trebui sa rescriem xpath-ul.
2. XPATH Relativ


Particularitati
La XPATH relativ cautarea incepe intotdeauna cu //
Atunci cand cautam dupa XPATH prin pereche atribut = valoare, atributul trebuie sa fie precedat de caracterul @
Atunci cand cautam dupa XPATH prin pereche atribut = valoare unde atributul class
			si valoarea este formata din doua sau mai multe clase separate prin spatiu,
			trebuie sa fie specificate toate
Atunci cand vrem sa navigam in copilul direct (Adica un copil al elementului) vom scrie /
Atunci cand vrem sa navigam in orice urmar (adica inclusiv copiii copiilor sau copiii copiii copiilor etc)
				vom scrie //

 exemplu de XPATH Relativ
//*[@id="gh-ac"]

exemplu de XPATH Absolut
/html/body/div[3]/div/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div[1]/div/input[1]

1. Cautare dupa un tag specific sau dupa orice tag
		- atunci cand cautam dupa formatul //tag sistemul o sa caute toate elementele cu tag-ul specificat
		- atunci cand cautam dupa formatul //* sistemul o sa caute toate rezultatele indiferent de tag
						ex: //h1//span[@class="BOLD"][1] -> sistemul o sa caute toate elementele de tip h1
													care au un copil de tip span cu clasa BOLD
								//*//span[@class="BOLD"][1] -> sistemul o sa caute toate elementele care au un copil
													de tip span cu clasa BOLD indiferent de tag-ul lor
								//*[@class="srp-controls__count-heading"]//span[@class="BOLD"][1] -> acelasi lucru ca mai sus

2. Cautare dupa o pereche atribut=valoare
3. Cautare dupa copil prin navigare de sus in jos (adica din parinte in copil)
4. Cautare dupa parinte prin navigare de jos in sus
5. Cauta dupa fratele anterior prin navigare de jos in sus
				atunci cand facem cautare dupa fratele anterior putem sa ne folosim de index sa ii spunem pe al catalea
							frate sa il caute. Astfel, daca punem spre exemplu indexul 1 va lua primul frate pe care il gaseste
							in cautarea de jos in sus
6. Navigare dupa fratele ulterior prin navigare de sus in jos
				atunci cand facem cautare dupa fratele ulterior putem sa ne folosim de index sa ii spunem pe al catalea
							frate sa il caute. Astfel, daca punem spre exemplu indexul 1 va lua primul frate pe care il gaseste
							in cautarea de sus in jos
				Deci, la navigarea dupa frati, indexul va fi cel al primului element pe care il gaseste in directia de cautare
7. Cautare cu OR
8. Cautare dupa text

Diferente intre CSS Selector si XPATH:
- CSS selector este mai rapid decat XPATH
- La XPATH putem sa facem cautare si din parinte in copil si din copil in parinte

'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from seleniumbase import Driver
from time import sleep
driver = Driver() # am instantiat un obiect din clasa driver
driver.get('https://www.ebay.com/')

# # Identificam butonul de search key si scriem ceva in el
# driver.find_element(By.XPATH,'//input[@placeholder="Search for anything"]').send_keys('iphone')
#
# # Varianta de mai jos nu este eficienta pentru ca este un xpath lung care poate fi facut mai scurt
# 						# si pentru ca se foloseste de indexul unui element
# # driver.find_element(By.XPATH,'//table[@id="gh-search-wrap"]/tbody/tr/td[1]')
#
# # identificam butonul de search si dam click pe el
# driver.find_element(By.XPATH,'//table[@id="gh-search-wrap"]//td[@class="gh-td-s"]').click()
#
# # identificam numarul de rezultate si le salvam intr-o variabila
# number_of_results = driver.find_element(By.XPATH,'//h1//span[@class="BOLD"][1]').text
# # alta varianta de cautare prea lunga:
# # //div[@class="srp-rail__right"]//parent::div[@class="srp-main srp-main--isLarge"]//div[@id="mainContent"]//span[@class="BOLD"][1]



# -------------------------

#
driver.find_element(By.XPATH,'//label[@for="gh-ac"]//following-sibling::input[@type="text"]').send_keys('iphone') # sau //label[@for="gh-ac"]//following-sibling::input[1]

# //td[@id="gh-as-td"]//preceding-sibling::td[1] -> am cautat butonul de search

#  --------------------------

#  Cautare avansata
driver.find_element(By.LINK_TEXT,'Advanced').click()
# diverse modalitati de a identifica inputul Enter keywords or item number
# driver.find_element(By.XPATH,'//span[@class="BOLD"]//parent::label//following-sibling::span[@class="floating-label"]//input')
# driver.find_element(By.XPATH,'//span[contains(text(),\'Enter keywords or item number\')]//parent::label//following-sibling::span[@class="floating-label"]//input')
driver.find_element(By.XPATH,"//label[contains(text(),'Enter keywords or item number')]//following-sibling::span/input")
keyword_options = Select(driver.find_element(By.XPATH,'//select[@name="_in_kw"]'))
keyword_options.select_by_visible_text('All words, any order')