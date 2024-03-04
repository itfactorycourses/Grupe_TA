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

# Ca sa cream o functie care primeste un dictionar
# ca si argument trebuie sa specificam ** la definire
# Acelasi lucru trebuie sa se intample si la apelare,
# Adica precedam numele argumentului de **
# def afiseaza_fotbalisti(**nume_dictionar):
# 	for key, value in nume_dictionar.items():
# 		for nume_fotbalist, atribute in fotbalisti_pe_echipe[key].items():
# 				for atribut in fotbalisti_pe_echipe[key][nume_fotbalist].keys():
# 						print(f"Jucatorul {nume_fotbalist} are {atribut} {fotbalisti_pe_echipe[key][nume_fotbalist][atribut]}")

# afiseaza_fotbalisti(**fotbalisti_pe_echipe)

dictionar_tyranosaourus=\
		{
		 		"tuplu_dinozauri_terestri" : ("tyranousaurus_rex","Eoraptor lunesis", "belusaurus sui", "dino"),
				"lista_dinozauri_aerieni": ["Pterodactylus","Pterodaustro","Moganopterus"],
				"set_dinozauri_marini": {"spinosaurus","hesperornis"}
		}

# Exercitiu: Vrem sa afisam pe ecran urmatoarele fraze:
# Dinozaurul numarul 1 din structura tuplu_dinozauri_terestri este tyranousaurus_rex
# Dinozaurul numarul 2 din structura tuplu_dinozauri_terestri este Eoraptor lunesis
# Dinozaurul numarul 3 din structura tuplu_dinozauri_terestri este belusaurus sui
# Dinozaurul numarul 4 din structura tuplu_dinozauri_terestri este belusaurus dino
# Dinozaurul numarul 1 din structura lista_dinozauri_aerieni este Pterodactylus
# Dinozaurul numarul 2 din structura lista_dinozauri_aerieni este Pterodaustro
# Dinozaurul numarul 3 din structura lista_dinozauri_aerieni este Moganopterus
# Dinozaurul numarul 1 din structura set_dinozauri_marini este spinosaurus
# Dinozaurul numarul 2 din structura set_dinozauri_marini este hesperornis


def afiseaza_dinozauri(**kwargs):
		for dino_keys, dino_values in kwargs.items():
				i = 1
				for nume_dinozaur in dino_values:
						print(f"Dinozaurul {i} din structura {dino_keys} este {nume_dinozaur}")
						i += 1

afiseaza_dinozauri(**dictionar_tyranosaourus)