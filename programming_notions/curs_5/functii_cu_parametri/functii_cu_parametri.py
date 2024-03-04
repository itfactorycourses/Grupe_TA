# Functia cu parametrii este utila atunci cand vrem sa folosim valori din exterior
				# in interiorul functiei



# def printeaza_numele(nume):
# 		print(f"Buna, numele meu este '{nume}'")
#
# nume = input("Va rugam sa introduceti numele ")
# printeaza_numele(nume)
# printeaza_numele("Alexandra Cuza")
# printeaza_numele("Marian Blanariu")

def calculeaza_pret_bilet(valoare_excursie,procent_discount):
	VALOARE_DISCOUNT = valoare_excursie * procent_discount
	valoare_excursie_cu_discount = valoare_excursie - VALOARE_DISCOUNT
	print(f"Valoare initiala excursie: {valoare_excursie}")
	print(f"Procent discount: {procent_discount}")
	print(f"Valoare discount: {VALOARE_DISCOUNT}")
	print(f"Valoare excursie cu discount: {valoare_excursie_cu_discount}")

# pret_bilet = int(input("Va rugam sa introduceti valoarea biletului "))
# discount = float(input("Va rugam sa introduceti valoarea discountului "))
# calculeaza_pret_bilet(pret_bilet,discount)
# pret_bilet = int(input("Va rugam sa introduceti valoarea biletului "))
# discount = float(input("Va rugam sa introduceti valoarea discountului "))
# calculeaza_pret_bilet(pret_bilet,discount)

# instructiunea de mai jos returneaza eroare: TypeError: calculeaza_pret_bilet() missing 2 required positional arguments: 'valoare_excursie' and 'procent_discount'
# Eroarea este returnata pentru ca functia este definita cu doi parametri si noi nu i-am dat niciun argument
# calculeaza_pret_bilet()

# instructiunea de mai jos returneaza eroare: TypeError: calculeaza_pret_bilet() takes 2 positional arguments but 3 were given
# Eroarea este returnata pentru ca functia este definita cu doi parametri si noi i-am dat trei argumente
# functia nu stie ce sa faca cu al treilea argument
# calculeaza_pret_bilet(30, 0.1,"margareta")


