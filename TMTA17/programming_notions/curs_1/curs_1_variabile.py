# # VARIABILE
#
# """
#
#
# variabila = adresa de memorie care stocheaza o valoare ce poate sa isi modifice valoarea
# 			pe tot parcursul executiei programului
# 			se numeste variabila pentru ca isi poate modifica valoarea (valoarea poate sa varieze)
# 			pe tot parcursul executiei programului
#
# Reguli de definire a variabilelor:
# 		- numele trebuie sa nu inceapa cu cifra
# 		- numele trebuie sa nu fie un cuvant cheie / rezervat (spre exemplu nu poate sa se numeasca int)
# 		- nu trebuie sa contina spatii
# 		- trebuie sa fie relevant pentru continutul acelei variabile
# 		- numele variabilei poate fi scris ori sub forma de camelCase ori sub forma de snake_case
#
# procesul de alocare a unei adrese de memorie pentru o variabila se numeste declarare
# procesul de salvare a unei valori initiale intr-o adresa de memorie a unei variabile se numeste initializare
# procesul de inlocuire a unei valori existente dintr-o variabila se numeste suprascrire
#
# Adresa de memorie care reprezinta variabila este identificata de un nume.
# Deci, numele variabilei este numele adresei de memorie la care este salvata informatia care
# 			poate sa varieze
#
# """
#
# # Declararea si initializarea unei variabile
# 		# mai jos am definit cateva variabile din diverse tipuri de date
# nume = "Anton Popescu" # am definit o adresa de memorie - variabila string
# varsta = 54 # am definit o adresa de memorie - variabila int
# salariu = 1056.78  # am definit o adresa de memorie - variabila float
# angajat = True # am definit o adresa de memorie - variabila bool
#
# # In python exista patru tipuri de date principale: int, string, float, bool
# 		# este o proprietate a unei adrese de memorie care defineste ce fel de valori
# 						# poti fi salvate la acea adresa de memorie
# 		# string = tip de data care permite salvarea caracterelor alfanumerice.
# 							# pentru ca o valoare sa fie considerata string, ea trebuie sa fie inconjurata
# 							# de ghilimele sau apostroafe
# 		# int = tip de data care permite salvarea caracterelor numerelor intregi
# 		# float = tip de date care permite salvarea caracterelor cu numere zecimale
# 		# bool = tip de date care permite salvarea valorilor True sau False
#
# # In python o variabila nu poate sa fie declarata fara sa fie si intializata in acelasi timp
# # In java putem sa declaram o variabila int in felul urmator: int varsta;
# # In python nu putem sa facem acelasi lucru pentru ca in python variabilele nu au tipul de date
# 			# specificat in mod explicit. Avantajul acestei abordari este faptul ca variabilele
# 			# pot sa isi schimbe tipul de date pe parcursul executiei
#
# """
# Java:
# int varsta;
# varsta = "Anton Popescu" -> ar returna eroare pentru ca sistemul stie ca variabila varsta
# 				poate sa stocheze doar valori intregi
#
# Python:
# varsta = 54
# varsta = "floricele" -> in python nu returneaza eroare pentru ca se poate schimba
# 				tipul de date al unei variabile printr-o simpla schimbare a valorii
# """
#
# # intrebare capcana:
# 	# ce problema am putea sa identificam mai jos
# 		# prin intermediul testarii statice?
# pret_bilet = 50 # tipul de date este int
# pret_bilet = 47.5 # tipul de date este float
#
# # R: Redefinirea unei variabile inainte sa fi fost folosita
#
#
# """
# Comentarii in python:
#
# In general limbajele de programare cunosc ceea ce se numeste sintaxa, adica totalitatea regulilor pe care
# 			acel limbaj de programare le cunoaste.
# 			Daca atunci cand scriem cod nu respectam sintaxa, vom primi ceea ce se numeste eroare de sintaxa
# Ca sa evitam acest lucru, ne vom folosi de ceea ce se numeste comentarii atunci cand vrem
# 		sa ne lasam explicatii in cod. Aceste comentarii vor fi ignorate de catre sistem la momentul compilarii
#
# In python exista doua tipuri de comentarii:
#
# - Comentarii single line - se scriu pe un singur rand, iar daca
# 			mergem pe randul urmator trebuie sa punem un nou marcator de comentariu
# 		 Comentariile pe un singur rand se fac cu caracterul #
#
# - Comentarii multiline - se pot scrie pe mai multe randuri
# 				si sunt definite fie de caracterele ''' fie de caracterele " " "
#
# 				Singura regula este sa incepem cu  niste caracytere si sa incheiem
# 				cu aceleasi caractere
# 				Adica, nu incepem comentariul cu ''' si terminam cu " " "
#
# """
#
# # CONSTANTE
#
# """
#
# In limbajele de programare o constanta este o adresa de memorie identificata de un nume care stocheaza o valoare
# 				care nu se poate modifica pe parcursul executiei programului (ramane CONSTANTA)
#
# In general, prin conventie, o constanta se scrie complet cu majuscule
# In python conceptul de constanta nu exista decat simbolic. Adica daca noi vrem sa avem o valoare
# 		nemodificata o sa definim o constanta cu litere mari, dar daca cineva totusi o sa incerce sa modifice]
# 		acea valoare nu va primi eroare
#
# """
#
# # Exemplu declarare si intitializare constanta:
# IMI_PLACE_LA_CURS = True
#
# # PRINTARE
#
# """
#
# Printarea inseamna afisarea in consola a anumitor informatii care sunt furnizate ca argument (vezi cursul 5)
# Cand printam o variabila sau o constanta de fapt citim valoarea de la adresa de memorie reprezentata
# de numele acelei variabile sau constante si o afisam pe ecran in consola (unde scrie Run)
#
# """
#
# print(IMI_PLACE_LA_CURS) # O sa printeze pe ecran valoarea True
#
# # Exercitiu: vrem sa printam pe ecran urmatoarea propozitie:
# 	# Anton Popescu are 54 de ani, este angajat True si are un salariu de 1056.78 lei
#
# # instructiunea de mai jos o sa dea eroare de sintaxa pentru ca sistemul nu stie sa uneasca
# 		# continutul variabilelor cu textul variabilelor
# # print(nume "are" varsta "de ani, este angajat " angajat "si are un salariu de " salariu "lei")
#
# # instructiunea semi-corecta este urmatoarea:
# # print(nume + "are" + varsta + "de ani, este angajat " + angajat +"si are un salariu de " + salariu + "lei")
#
# """
# Problema cu instructiunea de mai sus este urmatoarea:
#
# Noi am incercat sa concatenam continutul variabilelor cu textul dat de la tastatura.
# Concatenare inseamna alipirea unor informatii astfel incat sa rezulte un singur text
# Instructiunea de mai sus nu functioneaza pentru ca noi am incercat sa lipim string cu int.
# 			Acest lucru nu o sa mearga pentru ca semnul "+" pentru stringuri inseamna concatenare,
# 			iar pentru int si float inseamna adunare.
# 			In cazul asta ar fi o contradictie de instructiuni daca incerc sa folosesc caracterul +
# 			atunci cand in stanga lui este un string si in dreapta lui un int.
#
# """
#
# # Instructinea mai buna (dar nu perfecta) este urmatoarea:
# print(nume + " are " + str(varsta) + " de ani, este angajat " + str(angajat) +" si are un salariu de " + str(salariu) + " lei")
# """
# Ce am facut mai sus a fost ceea ce se numeste type casting sau conversie de tip
# Adica variabilele care in mod normal erau considerate ca fiind numerice sau booleene (varsta, angajat, salariu)
# 		au fost fortate sa fie considerate temporar ca fiind stringuri
#
# Atentie, sunt unele tipuri de casting care sunt incompatibile.
# Spre exemplu nu pot sa fac conversie de la string la int sau de la string la bool.
# """
#
# # Instructinea cea mai buna  este urmatoarea:
# print(f"{nume} are {varsta} de ani, este angajat {angajat} si are un salariu de {salariu} lei")
# """
# Ce am facut mai sus a fost sa punem caracterul f de la formatare in fata textului pe care vrem sa il printam
# 			ca sa anuntam sistemul ca in interiorul textului nostru or sa fie si variabile din care trebuie sa citeasca
# 			Pentru ca sistemul sa recunoasca aceste variabile ele trebuie sa fie plasate intre acolade
# """
#
# # FUNCTIA TYPE
# #  Functia type printeaza pe ecran tipul de date al variabilei data ca argument (vezi cursul 5)
# print(type(nume)) # printeaza pe ecran <class 'str'> pentru ca variabila este string
# print(type(salariu)) # printeaza pe ecran <class 'float'> pentru ca variabila este numar zecimal
# print(type(angajat)) # printeaza pe ecran <class 'bool'> pentru ca variabila este booleean
# print(type(varsta)) # printeaza pe ecran <class 'int'> pentru ca variabila este un numar intreg
#
# # TYPE CASTING
#
# # Casting catre string
# print(f"Variabila varsta are acum tipul de date {type(str(varsta))}") # am convertit variabila varsta de la int la string, apoi am apelat functia
# 				# type pentru a afla noul tip de date iar rezultatul l-am printat pe ecran
# print(f"Variabila salariu are acum tipul de date {type(str(salariu))}") # am convertit variabila salariu de la float la string, apoi am apelat functia
# 				# type pentru a afla noul tip de date iar rezultatul l-am printat pe ecran
# print(f"Variabila angajat are acum tipul de date {type(str(angajat))}")  # am convertit variabila angajat de la bool la string, apoi am apelat functia
# 				# type pentru a afla noul tip de date iar rezultatul l-am printat pe ecran
#
# # Casting catre int
# # print(f"Variabila nume are acum tipul de date {type(int(nume))}") # instructiunea o sa returneze eroare pentru ca
# # 				# nu putem sa convertim de la string la int
# print(f"Variabila salariu are acum tipul de date {type(int(salariu))} si are valoarea {int(salariu)} ") # instructiunea o sa ruleze cu succes,
# 				# dar daca facem conversie de la float la int, aceasta conversie se face cu pierderea zecimalelor
# print(f"Variabila angajat are acum tipul de date {type(int(angajat))} si are valoarea {int(angajat)} ")
# 					# instructiunea asta o sa functioneze, iar echivalentul lui True in int este 1, iar echivalentul lui False in int este 0
#
# # Casting catre bool
# print(f"Variabila nume are acum tipul de date {type(bool(nume))} si are acum valoarea {bool(nume)}")
# 					# conversia o sa mearga si o sa fie transformat textul din anton popescu in True
# 					# pentru ca in codul ASCII valoarea True este mai mare ca 0 si drept urmare orice e mai mare ca 0
# 					# o sa fie considerat True
#
# nume = ""
# print(f"Variabila nume are acum tipul de date {type(bool(nume))} si are acum valoarea {bool(nume)}")
# # conversia o sa mearga si o sa fie transformat textul din nimic in False
# 					# pentru ca in codul ASCII valoarea False este considerata 0 si drept urmare orice este 0
# 					# o sa fie considerat False
#
# print(f"Variabila salariu are acum tipul de date {type(bool(salariu))} si are acum valoarea {bool(salariu)}")
# print(f"Variabila varsta are acum tipul de date {type(bool(varsta))} si are acum valoarea {bool(varsta)}")
#
#
# # FUNCTIA INPUT
#
# """
# Este folosita pentru a cere date de la tastatura
# Functia input primeste ca argument textul care va fi afisat utilizatorului in consola
# 		si care il va anunta ce fel de valoare trebuie sa furnizeze

# Atentie, in mod implicit tipul de data returnat de functia input este string,
# 			chiar daca de la tastatura introducem valori numerice
# """
#
# # film_preferat = input("Va rugam sa introduceti numele filmului preferat ")
# # print(f"Filmul meu preferat este: {film_preferat}")

# CNP = input("Va rugam sa introduceti CNP-ul") # va rula dar nu ii va printa nimic utilizatorului

