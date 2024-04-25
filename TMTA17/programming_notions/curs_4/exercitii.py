"""

Dictionare imbricate (embedded dictionaries / nested dictionaries)	 reprezinta dictionare
			in interiorul altor dictionare

"""

fotbalisti_pe_echipe=\
		{
				"Barcelona":{	"Dica": {"Nume complet":"Nicolae Dica",
									 							"Varsta":45,
								 								"Numar Tricou":10
										           },
										"Banel":  {	"Nume complet":"Banel Nicolita",
								 						    "Varsta":47,
														    "Numar Tricou":3
														   },
										"Dukadam": {
																"Nume complet":"Helmut Dukadam",
																"Varsta":65,
																 "Numar Tricou":7
															 }
										}
		}

# Exercitiul 1: Vrem sa printam toate cheile din dictionar
# print(fotbalisti_pe_echipe.keys())
# print(fotbalisti_pe_echipe["Barcelona"].keys())
# print(fotbalisti_pe_echipe["Barcelona"]["Dica"].keys())
# print(fotbalisti_pe_echipe["Barcelona"]["Banel"].keys())
# print(fotbalisti_pe_echipe["Barcelona"]["Dukadam"].keys())
#
# # Exercitiul 2: Vrem sa printam toate valorile din dictionar
# print(f"{fotbalisti_pe_echipe.values()} \n")
# print(fotbalisti_pe_echipe["Barcelona"].values())

# Exercitiul 3: Vrem sa printam numele fiecarui jucator impreuna cu atributele lui
#
for key, value in fotbalisti_pe_echipe.items():
		for nume_fotbalist, atribute in fotbalisti_pe_echipe[key].items():
				for atribut in fotbalisti_pe_echipe[key][nume_fotbalist].keys():
						print(f"Jucatorul {nume_fotbalist} are {atribut} {fotbalisti_pe_echipe[key][nume_fotbalist][atribut]}")

# fotbalisti_pe_echipe["Barcelona"]["Dica"]["Numar Tricou"]
# print(fotbalisti_pe_echipe["Barcelona"].items())

"""

Linia 39:
keys = Barcelona
value = {	"Dica": {"Nume complet":"Nicolae Dica",
									 							"Varsta":45,
								 								"Numar Tricou":10
									},
		    	"Banel":  {	"Nume complet":"Banel Nicolita",
								 						    "Varsta":47,
														    "Numar Tricou":3
														   },
					"Dukadam": {
																"Nume complet":"Helmut Dukadam",
																"Varsta":65,
																 "Numar Tricou":7
																}
										}


Linia 40:
fotbalisti_pe_echipe[key].items() va stoca valoarea:
		dict_items([('Dica', {'Nume complet': 'Nicolae Dica', 'Varsta': 45, 'Numar Tricou': 10}), ('Banel', {'Nume complet': 'Banel Nicolita', 'Varsta': 47, 'Numar Tricou': 3}), ('Dukadam', {'Nume complet': 'Helmut Dukadam', 'Varsta': 65, 'Numar Tricou': 7})])

nume_fotbalist va stoca pe rand valoarea: Dica, Banel, Dukadam

atribute va stoca pe rand valoarea: 
{"Nume complet":"Nicolae Dica",
									 							"Varsta":45,
								 								"Numar Tricou":10
}

{	"Nume complet":"Banel Nicolita",
								 						    "Varsta":47,
														    "Numar Tricou":3
}

{
																"Nume complet":"Helmut Dukadam",
																"Varsta":65,
																 "Numar Tricou":7
																}
}


"""

dictionar_tyranosaourus=\
		{
		 		"tuplu_dinozauri_terestri" : ("tyranousaurus_rex","Eoraptor lunesis", "belusaurus sui", "dino"),
				"lista_dinozauri_aerieni": ["Pterodactylus","Pterodaustro","Moganopterus"],
				"set_dinozauri_marini":{"spinosaurus","hesperornis"}
		}

print(dictionar_tyranosaourus["lista_dinozauri_terestri"][1])


