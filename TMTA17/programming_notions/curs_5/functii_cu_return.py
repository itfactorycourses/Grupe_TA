def calculeaza_valoare_discount(valoare_excursie,procent_discount):
	VALOARE_DISCOUNT = valoare_excursie * procent_discount
	return VALOARE_DISCOUNT

valoare_excursie = int(input("Va rugam sa introduceti valoarea biletului "))
discount = float(input("Va rugam sa introduceti valoarea discountului"))
valoare_excursie_cu_discount = valoare_excursie - calculeaza_valoare_discount(valoare_excursie,discount)

print(f"Valoarea excursiei dupa aplicarea discountului este: {valoare_excursie_cu_discount}")