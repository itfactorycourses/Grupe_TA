'''

Polimorfism prin funcții cu un număr indefinit de argumente
Polimorfism prin funcții cu parametri inițializați cu valoare implicită
Polimorfism prin aceeași funcție cu același nume dar în clase diferite

'''

# Polimorfism prin funcții cu un număr indefinit de argumente
from abc import abstractmethod, ABC


def suma_numere(*lista_parametri):
		suma = 0
		for numar in lista_parametri:
				suma += numar
		print(f"Suma calculata este: {suma}")

suma_numere(1,4)
suma_numere(56,234567,2134567,23456,1,10,56)
suma_numere()

# Polimorfism prin funcții cu parametri inițializați cu valoare implicită

def calculeaza_pret_bilet(valoare_excursie=30,procent_discount=0.5):
	VALOARE_DISCOUNT = valoare_excursie * procent_discount
	valoare_excursie_cu_discount = valoare_excursie - VALOARE_DISCOUNT
	print(f"Valoare initiala excursie: {valoare_excursie}")
	print(f"Procent discount: {procent_discount}")
	print(f"Valoare discount: {VALOARE_DISCOUNT}")
	print(f"Valoare excursie cu discount: {valoare_excursie_cu_discount}")

calculeaza_pret_bilet()
calculeaza_pret_bilet(40,0.1)
calculeaza_pret_bilet(70)
calculeaza_pret_bilet(procent_discount=0.4)

# Polimorfism prin aceeași funcție cu același nume dar în clase diferite

class FormaGeometrica(ABC):
		aria = 0

		# pass # pass inseamna ca aceasta clasa nu are cod.
		# avand in vedere ca blocurile de cod in python sunt delimitate de indentare,
		# atunci cand nu vrem sa avem un bloc de cod, trebuie sa punem ceva
		# pentru ca altfel sistemul va returna eroare de sintaxa

		@abstractmethod
		def calculeaza_aria(self):
				pass

		def printeaza_aria(self):
				print(self.aria)

class Patrat(FormaGeometrica):
		latura = 0
		def calculeaza_aria(self):
				self.aria = self.latura ** 2
				return self.aria

class Dreptunghi(FormaGeometrica):
		lungime = 0
		latime = 0

		def calculeaza_aria(self):
				self.aria = self.lungime * self.latime
				return self.aria

patrat = Patrat()
patrat.latura = 5
dreptunghi = Dreptunghi()
dreptunghi.lungime = 3
dreptunghi.latime = 5
print(patrat.calculeaza_aria())
print(dreptunghi.calculeaza_aria())