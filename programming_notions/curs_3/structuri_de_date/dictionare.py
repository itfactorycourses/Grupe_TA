# Definire dictionar gol
dictionar_gol = {}
set_gol = {}

# Definire dictionar populat:
dictionar_cursanti_note = {
		"Daniela  Bodron": 10,
		"Alexandra Cuza": 10,
		"Aurelian Nae": 9,
		"Catalina Velicu": 8,
		"Paula Sime": 10,
		"Florin Ghetu": 9,
		"Serban Valentin": 9,
		"Alex Oprescu":10,
		"Lidia Rechesan":10,
		"Goja Adina":	10,
		"Gorgan Garofița - Aurora":	10,
		"Doboș Robert" :	10,
		"Dubovic Alexandra":	10,
		"Gabriel - Marian Blanariu":	10,
		"Griga Octavian" : 10
}

# 1. Accesarea elementelor din dictiona:
#
# 		1.1 Pe baza cheii (la fel ca la postman)

print(f"Robert a luat la testul intermediar nota {dictionar_cursanti_note['Doboș Robert']}")

# 		1.2 pe baza functiei get:

#  Functia get poate sa extraga un element din dictionar
print(dictionar_cursanti_note.get("Aurelian Nae"))

# 1.3 Putem sa extragem si elementele cheie:valoare sau doar cheile sau doar valorile pe baza
# 				functiilor keys(), values() sau items()
# # print(f"Cursantii care au dat testul sunt: {dictionar_cursanti_note.keys()}")
# # print(f"Notele care s-au luat la test sunt: {dictionar_cursanti_note.values()}")
# # print(f"Componentele dictionarului sunt: {dictionar_cursanti_note.items()}")
# # print(f"Componentele dictionarului sunt: {dictionar_cursanti_note}")ul carora putem sa interactionam cu un dictionar:

# 2. Functii prin intermediul carora putem interactiona cu dictionare

# 2.1 Extragerea elementelor din dictionar:
			# Metoda 1: Functia pop extrage un element din dictionar pe baza cheii
dictionar_cursanti_note.pop("Catalina Velicu")
print(dictionar_cursanti_note)
			# Metoda 2: Functia popitem care extragem ultimul element din dictionar
dictionar_cursanti_note.popitem()
print(dictionar_cursanti_note)
dictionar_cursanti_note.popitem()
print(dictionar_cursanti_note)

# 2.2. Actualizarea elementelor din dictionar
# Modalitati prin care putem sa actualizam elemente din dictionar:
# 		Metoda 1: Functia update care primeste care si argument perechea
# 						cheie: valoare unde cheia e cheia din dictionar care se va actualiza
# 						iar valoarea este noua valoare care se va pune pe acea cheie
dictionar_cursanti_note.update({"Aurelian Nae":10})
print(dictionar_cursanti_note)

			# Metoda 2: prin intermediul cheii si al operatorului de atribuire
dictionar_cursanti_note["Aurelian Nae"] = 9
print(dictionar_cursanti_note)

# 2.3 Adaugarea elementelor in dictionar
# Modalitati prin care putem sa adaugam elemente in dictionar:
# 		Metoda 1: Functia update nu doar modifica elemente,
# 							ci poate sa si adauge elemente atunci cand
# 							cheia furnizata ca si argument nu exista deja in dictionar
# 							Ea primeste care si argument perechea
# 						cheie: valoare unde cheia e cheia care se va adauga in dictionar
# 						iar valoarea este cea care se va pune pe acea cheie care vrem sa fie adaugata

dictionar_cursanti_note.update({"Marian Popescu":7})
print(dictionar_cursanti_note)

			# Metoda 2: prin intermediul cheii si al operatorului de atribuire
dictionar_cursanti_note["Adelina Patrascu"] = 4
print(dictionar_cursanti_note)

# dictionare imbricate
