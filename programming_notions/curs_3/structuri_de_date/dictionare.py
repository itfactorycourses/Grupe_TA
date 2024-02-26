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

# Accesarea elementelor din dictionar se face pe baza cheii (la fel ca la postman)

print(f"Robert a luat la testul intermediar nota {dictionar_cursanti_note['Doboș Robert']}")
print(f"Cursantii care au dat testul sunt: {dictionar_cursanti_note.keys()}")
print(f"Notele care s-au luat la test sunt: {dictionar_cursanti_note.values()}")
print(f"Componentele dictionarului sunt: {dictionar_cursanti_note.items()}")
print(f"Componentele dictionarului sunt: {dictionar_cursanti_note}")

# -- pop, update (adaugare si actualizare de elemente), get, popitem, dictionare imbricate
