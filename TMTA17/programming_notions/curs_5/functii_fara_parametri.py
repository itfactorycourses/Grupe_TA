# def printeaza_dalmatienii():
# 	for i in range(102):
# 		print(f"Dalmatianul curent are numarul {i}")

# Dupa ce am definit functia ea nu va face nimic pana in momentul in care nu o apelam
# Apelarea se face prin specificarea numelui functiei urmat de paranteze rotunde
# printeaza_dalmatienii()
#
# # daca scriem functia fara paranteze rotunde si incercam sa printam, sistemul
# 			# ne va printa adresaa de memorie la care se afla functia: <function printeaza_dalmatienii at 0x1088f1e10>
# print(printeaza_dalmatienii)
#
# # Daca o functie nu are instructiune de return, atunci cand vom printa rezultatul ei ne va printa None
# print(printeaza_dalmatienii())


# Exercitiu: Defineste o functie care printeaza pe ecran: Buna, numele meu este "Ion Popescu"
def printeaza_numele():
		nume = "Ion Popescu"
		print(f"Buna, numele meu este '{nume}'")

def calculeaza_pret_bilet():
	VALOARE_EXCURSIE = float(input("Va rugam sa introduceti valoarea excursiei "))
	PROCENT_DISCOUNT = float(input("Va rugam sa introduceti procentul de discount aplicat "))
	VALOARE_DISCOUNT = VALOARE_EXCURSIE * PROCENT_DISCOUNT
	valoare_excursie_cu_discount = VALOARE_EXCURSIE - VALOARE_DISCOUNT
	print(f"Valoare initiala excursie: {VALOARE_EXCURSIE}")
	print(f"Procent discount: {PROCENT_DISCOUNT}")
	print(f"Valoare discount: {VALOARE_DISCOUNT}")
	print(f"Valoare excursie cu discount: {valoare_excursie_cu_discount}")

calculeaza_pret_bilet()