
"""
# atunci cand avem nevoie de niste informatii care deja au fost definite, putem sa le folosim
astfel incat sa nu trebuiasca sa le definim din nou.
Atunci cand aceste elemente exista intr-un alt fisier, ele trebuie sa fie importate
Importul se poate face in doua feluri:
1. Importul intregului fisier: import liste => acest import ne-ar aduce toate elementele din acel fisier
2. Importul elementului din fisier care ne intereseaza: from liste import lista_cursanti_prezenti_astazi
				=> acest import ne va aduce doar elementul specificat

Atunci cand fisierul care ne intereseaza sa fie importat se afla intr-un alt folder decat cel in care
			se afla fisierul in care vrem sa importam, atunci trebuie sa specificam toate folderele
			parinte in ierarhie incepand de la root pana in folderul in care se afla fisierul
			pe care vrem sa il importam. Cu alte cuvinte trebuie sa specificam path-ul fisierului
			In acel path fiecare folder copil va fi separat de folderul parinte prin caracterul "."

componentele structurii repetitive for:
- inceputul structurii repetitive - for
- numele variabilei de iteratie (de regula se va numi i de la index)
- cuvantul "in"
- intervalul de valori care se va parcurge (spre exemplu se poate folosi functia range)
- blocul de cod care se va executa atata timp cat nu am ajuns la finalul colectiei de valori
			blocul de cod, la fel ca si la if, se va marca cu indentare fata de marginea fisierului

"""

# Exercitiu: vrem sa parcurgem toata lista de cursanti prezenti si sa printam pe ecran
			# urmatoarea propozitie: "Cursantul nume_cursant este prezent la curs"

"""
Mai jos am facut o structura repetitiva de tip for care functioneaza in felul urmator:
- in variabila de iteratie i am salvat pe rand fiecare valoare din range-ul dat
- len(lista_cursanti_prezenti_astazi) returneaza numarul total de elemente din lista data
- range returneaza un interval de elemente care poate sa primeasca doua argumente:
						inceputul intervalului
						finalul intervalului
				Daca inceputul intervalului nu este mentionat, in mod implicit va fi 0
				Valoarea specificata ca final de interval va fi de fapt prima valoare din interval
				care nu va fi procesata
				
Definita functiei range: range(start, stop, step) - functioneaza ca la string slicing
start	Optional. An integer number specifying at which position to start. Default is 0
stop	Required. An integer number specifying at which position to stop (not included).
step	Optional. An integer number specifying the incrementation. Default is 1
"""

# Instructiunea de mai jos returneaza eroare: TypeError: 'list' object cannot be interpreted as an integer
				# eroarea este returnata pentru ca functia range asteapta ca si argument
# for i in range(lista_cursanti_prezenti_astazi):
# 		print(f"Cursantul {lista_cursanti_prezenti_astazi[i]} este prezent la curs")

# for i in range(len(lista_cursanti_prezenti_astazi)):
# 		print(f"Cursantul {lista_cursanti_prezenti_astazi[i]} este prezent la curs")

# Vreau sa printez pe ecran pe cei 101 dalmatieni

# for i in range(102):
# 		print(f"Dalmatianul curent are numarul {i}")

# Acelasi lucru, dar cu step - aici valoarea de start este obligatorie
for i in range(0,102,20):
		print(f"Dalmatianul curent are numarul {i}")