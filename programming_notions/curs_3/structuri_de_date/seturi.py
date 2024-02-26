# Declararea si initializarea unui set gol
set_gol = set()

# Declararea si initializarea unui set populat
set_studenti_prezenti_astazi = {"Aurelian","Daniela","Dino","Roby","Alexandra","Garofita","Florin","Octavian","Lidia","Alex","Vali","Marian"}

# Declararea si intializarea unui set multitype
set_multitype = {"ana are mere",356,345.879,True}

# Accesarea unui element din set se face pe baza de valori (nu pe baza de index pentru ca nu avem index)
		# accesarea elementelor se poate face doar printr-o structura repetitiva pentru afisare

# Stergerea unui element din lista cu functia pop - sterge un element la intamplare
print(f"Setul inainte de pop este: {set_studenti_prezenti_astazi}")
set_studenti_prezenti_astazi.pop()
print(f"Setul dupa pop este: {set_studenti_prezenti_astazi}")

# Stergerea unui element din lista cu functia REMOVE - sterge un element specific
print(f"Setul inainte de remove este: {set_studenti_prezenti_astazi}")
set_studenti_prezenti_astazi.remove("Garofita")
print(f"Setul dupa remove este: {set_studenti_prezenti_astazi}")

# Putem adauga elemente in set folosind functia add
print(f"Setul inainte de add este: {set_studenti_prezenti_astazi}")
set_studenti_prezenti_astazi.add("Garofita")
print(f"Setul dupa add este: {set_studenti_prezenti_astazi}")

# superset inseamna ca setul de la care se pleaca contine toate elementele din setul care se verifica plus inca ceva
# subset inseamna ca setul de la care se pleaca este inclus in setul la care se ajunge
set_colinde = {"mere","pere","nuci","covrigi","si-o bucata de sorici"} # categorie
set_fructe = {"mere","pere"} # subcategorie
print(f"set_colinde este superset pentru set_fructe? {set_colinde.issuperset(set_fructe)}")
print(f"set_colinde este subset pentru set_fructe? {set_colinde.issubset(set_fructe)}")
print(f"set_fructe este superset pentru set_colinde? {set_fructe.issuperset(set_colinde)}")
print(f"set_fructe este subset pentru set_colinde? {set_fructe.issubset(set_colinde)}")

print(f"Elementele comune dintre cele doua seturi sunt: {set_colinde.intersection(set_fructe)}")
print(f"Elementele comune dintre cele doua seturi sunt: {set_fructe.intersection(set_colinde)}")

print(f"Elementele din set_colinde care nu se afla in set_fructe sunt: {set_colinde.difference(set_fructe)}")
print(f"Elementele din set_fructe care nu se afla in set_colinde sunt: {set_fructe.difference(set_colinde)}")

