# A) OPERATORI ARITMETICI

"""

Operatorii aritmetici sunt cei prin intermediul carora o sa putem sa facem calcule matematice

addition (+) -> efectuează operații de adunare: suma = salariu + 100
substraction (-) -> efectuează operații de scădere: suma = salariu - 100
multiplication (*) -> efectuează operații de înmulțire: suma = salariu * 2
division (/) -> efectuează operații de împărțire: suma = salariu / 0.05
modulo (%) -> returnează restul împărțirii dintre un deîmpărțit și un împărțitor: rest = 11 % 2 # returneaza 1
exponential (**) -> efectuează operații de ridicare la putere: power = 2**3 # returneaza 8
floor division (//) -> efectuează operații de împărțire după care taie zecimalele suma = 10 // 3 # returneaza 3

"""
# Adunare (addition) -> se face prin intermediul operatorului +
print(f"Suma intre 2 si 3 este {2+3}")
# Scadere (extraction) -> se face prin intermediul operatorului -
print(f"Diferenta intre 2 si 3 este {2-3}")
# Inmultire (multiplication) -> se face prin intermediul operatorului *
print(f"Produsul intre 2 si 3 este {2*3}")
# Impartirea (division) -> se face prin intermediul operatorului /
print(f"Impartirea intre 2 si 3 este {2/3}")
# Operatorul modulo returneaza restul impartirii unui deimpartit la impartitor, Se face prin intermediul operatorului %
print(f"Restul impartirii lui 10 la 3 este {10%3}")
# Ridicarea la putere se face prin intermediul operatorului **
print(f"2 la puterea a treia este {2**3}. 2 inmultit cu 3 este {2*3}")
# Operatorul floor division face o rotunjire in minus pana la primul numar intreg
print(f"Floor division intre 15 si 7 este {15//7}")

# B) OPERATORII DE ATRIBUIRE

"""
Acesti operatori sunt cei prin intermediul carora putem sa populam adresele de memorie
Cu alte cuvinte prin intermediul lor putem sa dam valoare variabilelor si constantelor
Prin intermediul operatorului = putem spre exemplu sa facem initializarea sau suprascrierea variabilelor
initializare = salvarea unei valori initiale unei variabile
suprascriere = inlocuirea valorii dintr-o variabila cu o alta valoare

= -> operatorul de atribuire simpla. Adica in variabla din stanga operatorului se atribuie valoarea din dreapta operatorului
+= -> operatorul de atribuire care intai aduna valoarea din stanga atributului 
					cu valoarea din variabila din dreapta atributului, apoi inlocuieste valoarea din variabila
-= -> operatorul de atribuire care intai scade valoarea din stanga atributului 
					din valoarea din variabila din dreapta atributului, apoi inlocuieste valoarea din variabila
*= -> operatorul de atribuire care intai inmulteste valoarea din stanga atributului 
					cu valoarea din variabila din dreapta atributului, apoi inlocuieste valoarea din variabila
/= -> operatorul de atribuire care intai imparte valoarea din stanga atributului 
					cu valoarea din variabila din dreapta atributului, apoi inlocuieste valoarea din variabila
**= -> operatorul de atribuire care intai ridica la putere valoarea din stanga atributului 
					cu valoarea din dreapta atributului, apoi inlocuieste valoarea din variabila
"""

varsta = 5 # am initializat o variabila varsta cu valoarea 5 prin intermediul operatorului de atribuire
print(f"Varsta dupa initializare este: {varsta}")
varsta += 7 # am adunat valoarea 7 din dreapta opertorului la valoarea
print(f"Varsta dupa adunarea lui 7 este: {varsta}")
					# din variabila din stanga operatorului si am inlocuit valoarea din variabila cu rezultatul calculat
varsta -= 2 # am scazut valoarea 2 din dreapta opertorului din valoarea
					# din variabila din stanga operatorului si am inlocuit valoarea din variabila cu rezultatul calculat
print(f"Varsta dupa scaderea lui 2 este: {varsta}")
varsta *= 3 # am inmultit valoarea 3 din dreapta opertorului la valoarea
					# din variabila din stanga operatorului si am inlocuit valoarea din variabila cu rezultatul calculat
print(f"Varsta dupa inmultirea cu 3 este: {varsta}")
varsta /= 10 #am impartit valoarea stanga opertorului cu valoarea
					# din dreapta operatorului si am inlocuit valoarea din variabila cu rezultatul calculat
print(f"Varsta dupa imaprtirea la 10 este: {varsta}")
varsta **= 3 #am ridicat la putere valoarea din stanga opertorului la valoarea
					# din dreapta operatorului si am inlocuit valoarea din variabila cu rezultatul calculat
print(f"Varsta dupa ridicarea la puterea a treia este: {varsta}")

# varsta + = 3 # instructiunea asta o sa da eroare de sintaxa pentru ca operatorul este luat in considerare
					# atunci cand operatorul aritmetic si operatorul de atribure sunt lipiti
					# altfel sunt considerati operatori separati carora le lipsesc operanzii numerici

# OPERATORI DE COMPARARE -> efectueaza compararea a doua siruri de caractere si returneaza o valoare boolean:

print(f"Este 2 < 3? {2<3}")
print(f"Este 3 > 10? {3>10}")
print(f"Este 2 <= 3? {2<=3}")
print(f"Este 3 >= 2? {3>=2}")
print(f"Este 5 diferit de 10? {5!=10}")
print(f"Este 45 egal cu 56? {45==56}")

# Atentie!!! nu confundati operatorul de atribuire "=" cu operatorul de comparatie "=="

# OPERATORI LOGICI - SUNT CEI PRIN INTERMEDIUL CARORA PUTEM SA CREAM CONDITII COMPUSE:

""""
AND -> atunci când folosim AND atât condiția din stânga operatorului cât și cea din dreapta operatorului trebuie să fie adevărată pentru ca întreaga condiție să fie adevărată.  Dacă cea din stânga este evaluată ca fiind falsă, sistemul nu va mai evalua condiția a doua
OR -> atunci când folosim OR fie condiția din stânga operatorului fie cea din dreapta operatorului trebuie să fie adevărată pentru ca întreaga condiție sa fie adevărată. Dacă cea din stânga este evaluată ca fiind adevărată, sistemul nu va mai evalua condiția a doua
NOT -> operatorul NOT returnează opusul rezultatului condiției (ex: NOT False = True)
"""

print(2<3 and 5>6) # se evalueaza 2<3 ca fiind true si apoi se evalueaza si 5>6
print(5>6 and 2<3) # 5>6 se evalueaza ca fiind false si apoi nu se mai evalueaza 2<3
print(2<3 or 5>6) # 2<3 se evalueaza ca fiind true si 5>6 nu se mai evalueaza
print(5>6 or 2<3) # 5>6 se evalueaza ca fiind false si apoi se evalueaza 2<3
print(not 5>6 or 2<3) # se evalueaza intai not 5>6 apoi 2<3 si apoi rezultatele se analizeaza cu or
print(not 5>6 and 2<3)
print(not (5<6 and not 2<3))

# ORDINEA PRIORITATII: NOT -> AND -> OR







