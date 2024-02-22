"""

structura alternativa if-elif-else este o modalitate prin care putem instrui codul
sa execute un set de instructiuni sau un alt set de instructiuni
in functie de rezultatul evaluarii unei conditii

Structura unui if:

inceputul ifului: if
conditia care se evalueaza pentru a lua decizia (foloseste operatorii de comparatie si, daca este nevoie, operatorii logici)
marcatorul care anunta sistemul ca urmeaza sa inceapa corpul if-ului - caracterul ":"
corpul if-ului -> marcat de o indentare fata de marginea fisierului
				indentare = spatiu intre marginea fisierului python si linia de cod
elif -> evaluarea unei conditii alternative in cazul in care conditia initiala din if nu a fost respectata
				existenta unui elif este optionala si putem sa avem oricate elif uri avem nevoie intr-un if
else -> instructiunile implicite care trebuie sa fie executate in cazul in care nicio conditie nu este respectata
"""

"""
Exercitiu: avem de calculat valoarea totala a unui bilet pe baza urmatoarelor criterii: 
Varstnici de 65 de ani si peste vor avea reducere de 15% la bilet
Persoanele sub 65 de ani vor avea reducere de 10% doar daca calatoresc 
			cu cel putin un copil
Toti calatorii vor avea o reducere aditionala de 10% la toate biletele 
					daca vor calatori iarna
Toti calatorii vor plati o taxa de lux de 3% daca calatoresc la clasa 1, sau doar
o taxa de 1% daca calatoresc la clasa a 2-a
"""

varsta = int(input("Va rugam sa introduceti varsta"))
clasa = int(input("Va rugam sa introduceti clasa la care calatoriti"))
pret_bilet = float(input("Va rugam sa introduceti pretul biletului"))
anotimp = input("Va rugam sa introduceti anotimpul in care calatoriti")
discount = 0
if varsta >= 65:
		discount = 0.15
else:
		nr_copii = int(input("Va rugam sa introduceti numarul de copii"))
		if nr_copii >=1:
			discount = 0.1
if anotimp == "iarna":
		discount += 0.1
		# discount = discount + 0.1
if clasa == 1:
		tax = 0.03
else:
		tax = 0.01

pret_bilet = pret_bilet - pret_bilet * discount + pret_bilet * tax
print(f"Pretul final al biletului este {pret_bilet}")