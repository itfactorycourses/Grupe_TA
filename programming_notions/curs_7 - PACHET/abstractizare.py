'''

Abstractizarea este o modalitate prin care putem sa ascundem anumite informatii la momentul
folosirii unei clase de catre un utilizator

Abstractizarea se face prin intermediul mostenirii clasei ABC (Abstract Base Classs)
Orice clasa care mosteneste clasa ABC implementeaza conceptul de abstractizare

O clasa abstracta poate sa aiba una sau mai multe metode abstracte.

O metoda se defineste ca fiind abstracta atunci cand este precedata de decoratorul @abstractmethod

O clasa care are DOAR metode abstracte se numeste interfata

O metoda este abstracta atunci cand nu are o implementare, adica atunci cand nu are logica
		de cod in corpul metodei

Atunci cand definim o metoda ca fiind abstracta, toate clasele care vor mosteni
		clasa abstracta vor fi obligate sa furnizeze o implementare pentru metoda abstracta,
		adica sa creeze logica de cod in interiorul metodelor care vor suprascrie metoda abstracta

'''

from abc import ABC, abstractmethod

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

		# In clasa patrat suntem obligati sa implementam metoda abstracta calculeaza_aria
				# in caz contrar ne va returna urmatoarea eroare:
								# TypeError: Can't instantiate abstract class Patrat with abstract method calculeaza_aria
		def calculeaza_aria(self):
				self.aria = self.latura**2

		def __init__(self, latura):
				while latura<=0:
						latura = int(input("Va rugam sa introduceti o valoare "
															 "pentru latura mai mare ca 0"))
				self.latura = latura

patrat = Patrat(2)
print(patrat.latura)

class Dreptunghi(FormaGeometrica):
		lungime = 0
		latime = 0

		def __init__(self, lungime,latime):
				while lungime <= 0 or latime<=0:
						if lungime<=0:
							lungime = int(input("Va rugam sa introduceti o valoare "
															 "pentru lungime mai mare ca 0"))
						if latime<=0:
							latime = int(input("Va rugam sa introduceti o valoare "
															 "pentru latime mai mare ca 0"))
				self.lungime = lungime
				self.latime = latime

		def calculeaza_aria(self):
				self.aria = self.lungime * self.latime

dreptunghi = Dreptunghi(3,5)
print(dreptunghi.calculeaza_aria())
print(dreptunghi.aria)

