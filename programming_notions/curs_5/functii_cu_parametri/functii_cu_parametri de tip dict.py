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

dictionar_tyranosaourus=\
		{
		 		"tuplu_dinozauri_terestri" : ("tyranousaurus_rex","Eoraptor lunesis", "belusaurus sui", "dino"),
				"lista_dinozauri_aerieni": ["Pterodactylus","Pterodaustro","Moganopterus"],
				"set_dinozauri_marini":{"spinosaurus","hesperornis"}
		}

# Ca sa cream o functie care primeste un dictionar
# ca si argument trebuie sa specificam ** la definire
# Acelasi lucru trebuie sa se intample si la apelare,
# Adica precedam numele argumentului de **
def afiseaza_fotbalisti(**nume_dictionar):
	for key, value in nume_dictionar.items():
		for nume_fotbalist, atribute in fotbalisti_pe_echipe[key].items():
				for atribut in fotbalisti_pe_echipe[key][nume_fotbalist].keys():
						print(f"Jucatorul {nume_fotbalist} are {atribut} {fotbalisti_pe_echipe[key][nume_fotbalist][atribut]}")

afiseaza_fotbalisti(**fotbalisti_pe_echipe)