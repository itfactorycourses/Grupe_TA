def calculeaza_pret_bilet(valoare_excursie=30,procent_discount=0.5):
	VALOARE_DISCOUNT = valoare_excursie * procent_discount
	valoare_excursie_cu_discount = valoare_excursie - VALOARE_DISCOUNT
	print(f"Valoare initiala excursie: {valoare_excursie}")
	print(f"Procent discount: {procent_discount}")
	print(f"Valoare discount: {VALOARE_DISCOUNT}")
	print(f"Valoare excursie cu discount: {valoare_excursie_cu_discount}")

# In instructiunea de mai jos va calcula ce trebuie pentru ca va pune primul argument pe primul parametru
calculeaza_pret_bilet(30)

# In instructiunea de mai jos va calcula ce trebuie pentru ca va avea specificat
# in mod explicit pe care parametru vrem sa punem argumentul
calculeaza_pret_bilet(procent_discount=0.1)

# In instructiunea de mai jos nu se va calcula ce trebuie pentru ca prima valoare data ca argument
	# va fi pusa pe primul parametru
# calculeaza_pret_bilet(0.1)