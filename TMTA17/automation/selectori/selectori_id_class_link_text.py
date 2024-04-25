'''

instructiuni import:

import nume_fisier
from nume_fisier import nume_clasa
from nume_fisier import nume_functie
from nume_fisier import nume_constanta
from nume_fisier import nume_variabila

'''
import time

from selenium.webdriver.common.by import By
from seleniumbase import Driver
from time import sleep

driver = Driver() # am instantiat un obiect din clasa driver
driver.get('https://www.ebay.com/') # metoda get este o metoda din clasa Driver si conform
																# regulilor de programare OOP putem sa accesam un atribut sau o metoda
																	# dintr-o clasa prin intermediul unui atribut instantiat din acea clasa
driver.maximize_window()
sleep(5)

# 1. CAUTARE DUPA ID
# scenariu: accept cookies ca sa evitam situatia in care elementele noastre sunt acoperite de bannerul de cookies
# vom face cautare dupa ID. ID-ul este cel mai reliable selector pentru ca in 99.9% din cauzuri este unic
# ca sa facem cautarea unui element ne folosim de metoda find_element care este accesata
			# prin intermediul obiectului instantiat din clasa Driver.
			# metoda find_element accepta doua argumente: tipul de selector si valoarea selectorului
			# tipul selectorului poate fi selectat din clasa By din libraria (fisierul) selenium.webdriver.common.by
			# metoda find_element identifica elementele web, dar nu si interactioneaza cu ele

# interactiunea cu elementul se poate face in doua feluri:
# a) prin a salva elementul web intr-o variabila si apoi prin a ne folosi de acea variabila ca sa accesam metodele de interactiune cu elementul
accept_cookies_button = driver.find_element(By.ID,'gdpr-banner-accept')
accept_cookies_button.click()
# b) prin a apela metoda de interactiune cu elementul direct in continuarea metodei find_element
driver.find_element(By.ID,'gdpr-banner-accept').click()
#  ca sa apelam o functie scriem numele functiei urmat de paranteze rotunde.
			# in functie de definitia functiei intre paranteze SE POT pune argumente (care sunt valori pentru parametri)
sleep(4)

# 2. CAUTARE DUPA LINK TEXT sau PARTIAL LINK TEXT
# un link text este textul care se afiseaza in loc linkului pe o pagina web pentru a face
 		# acel link mai prietenos pentru utilizatorul final
		# link text-ul se afla pe un element de tip ancora (adica un element cu tag-ul <a>)
		# si se afla intre tag-ul de deschidere (ex: <a href="https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&amp;sgfl=gh&amp;ru=https%3A%2F%2Fwww.ebay.com%2F" _sp="m570.l2620">)
		# 			si tag-ul de inchidere (ex: </a>)

		# diferenta intre intre link text si partial link text:
		# la link text daca dam doar o parte din link ca si argument ne va returna eroare: element not found
		# la partial link text va returna toate elementele care contin acea parte dintr-un link text
		# exemplu:
		# daca avem link textul: "Dati click aici pentru autentificare"
		# cautam dupa textul: Dati click aici pentru autentificare
		# la link text va returna doar elementele care contin exact textul asta
		# la partial link text va returna toate elementele care contin textul asta sau textul asta + ceva
					# ex: poate sa returneze si textul Dati click aici pentru autentificarea in aplicatie

# SCENARIU: Vrem sa dam click pe linkul de sign in ca sa ajungem pe pagina de login
driver.find_element(By.LINK_TEXT,'Sign in').click()
sleep(4)



# 3. Cautare dupa clasa
# clasa este folosita in dezvoltarea web pentru a grupa mai multe elemente
			# care trebuie sa aiba aceeasi formatare.
			# atunci cand vrem sa  modificam mai multe elemente care au aceeasi formatare (ex: acelasi font
			# aceeasi culoare sau aceeasi dimensiune a scrisului etc) modificam o singura data
			# proprietatile in clasa care reprezinta acele elemente, si modificarea se va face
			# automat pe toate elementele care sunt reprezentate de acea clasa
			# avand in vedere ca pot fi mai multe elemente cu aceeasi clasa este destul de greu
					# sa identificam in mod unic elementele web doar pe baza de clasa
					# in aceast caz ne putem folosi de metoda find_elements care identifica toate elementele
					# cu selectorul dat si returneaza o lista cu toate elementele gasite.

		# Diferenta intre find_element si find_elements:
		# - find_element returneaza un singur element web si daca elementul nu este gasit returneaza eroarea: element not found
		# - find_elements returneaza o lista cu elemente si daca nu gaseste nimic returneaza o lista goala
# in HTML un element poate sa fie reprezentat de mai multe clase. Aceste clase sunt separate prin spatiu
		# in automatizare atunci cand fac cautarea unui element dupa clasa trebuie sa fac cautare
				# dupa o singura din clasa (nu conteaza care dar sa fie una)
email_elements_by_class = driver.find_elements(By.CLASS_NAME,'textbox__control')
email_elements_by_class[0].send_keys("meet@itfactory.ro")
driver.find_element(By.ID,'pass').send_keys('test123@')
driver.find_element(By.ID,'sgnBt').click()


