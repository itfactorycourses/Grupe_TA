"""
Ce este un string? Un sir de caractere alfanumerice

String slicing? Este o modalitate prin intermediul careia putem sa "feliem" stringul nostru
pentru a extrage doar informatiile care ne intereseaza

Exemplu de situatie in care se poate folosi:
Avem un database url: jdbc:mysql://vodafonejdb:3306/mysql

Noi vrem sa verificam daca hostul (numele serverului) de baze de date e corect
sau putem sa extragem acel host ca as il punem intr-un framework de automatizare
pentru a ne conecta la acea baza de date.
In cazul asta pe noi ne-ar interesa strict bucata vodafonejdb
Ca sa ne folosim strict de bucata de cod care ne intereseaza o sa feliem stringul
astfel incat sa obtinem strict informatia de care avem nevoie

if 2 < 12$ -> if 2<12

Slicingul unui string se face prin intermediul
parantezelor patrate cu urmatoarele optiuni:
[inceput_extractie:final_extractie:pas_extractie]
"""
prop = "Ana are mere"
print(f"{prop[0:5:1]}") #-> incepe de la pozitia 0 si extrage pana la elementul din pozitia 3
					# la stringuri primul caracter din string se va afla intotdeauna in pozitia 0
					# la slicing indexul final al extractiei trebuie sa fie cu unul mai mare decat
									# indexul ultimului caracter pe care vrem sa il extragem
									# asta se intampla pentru ca indexul specificat ca si end index
									# este considerat ca fiind urmatorul dupa elementul care ne intereseaza.
									#indexul de final de extractie este indexul primului element pe care nu vrem sa il extragem
print(f"{prop[0:10:1]}") # avand in vedere ca daca la pas punem 1
									# se ia fiecare caracter in parte, atunci putem sa
									# sarim acest pas si sa nu punem nimic, pentru ca
									# in mod implicit valoarea de step este 1
print(f"{prop[0:10]}") # instructiunea asta va returna acelasi lucru ca mai sus
										# pentru ca va lua in mod implicit step-ul ca fiind 1

print(f"{prop[0:10]}") # in mod implicit, pasul initial de incepere a slicingului
									# este elementul cu indexul 0. In acest caz,
									# daca ne intereseaza sa facem slicing incepand de la primul
									# element, aceasta pozitie de start poate sa fie nespecificata
									# DAR MARCATA
print(f"{prop[10]}") # daca scriu doar instructiunea asta imi va printa
									# pe ecran caracterul cu indexul 10, nu toate elementele
									# de la pozitia 0 pana la pozitia 10.
print(f"{prop[:10]}") # in felul asta chiar daca nu am specificat in mod
									# explicit pozitia de start, am marcat-o cu caracterul :
									# astfel incat sistemul sa inteleaga ca ne intereseaza
									# un range de caractere si nu un singur caracter

print(f"{prop[3:12:3]}") # daca printez asa, imi va printa toate
									# elementele
									# incepand cu cel de la indexul 3 pana la indexul 11
									# cu un pas de 3
									# dar avand in vedere ca 12 este si finalul de string
									# noi putem sa omitem acest final
									# dar trebuie sa il marcam

print(f"{prop[3:3]}") # daca printez informatia in felul asta
										# o sa imi printeze un singur caracter de la pozitia 3
print(f"{prop[3::3]}") # in felul asta am omis specificarea explicita a
											# pozitiei de finish, dar am marcat aceasta pozitie
											# sa stie sistemul demarcajul intre pozitia de finish si step

# cum printam un string in reverse? Prin adaugarea caracterului - in fata pasului
print(f"{prop[::-3]}") # printeaza sirul in reverse cu un pas de 3
												# prin faptul ca am pus :: am anuntat sistemul
												# ca urmeaza sa facem slicing dar ca folosim valorile
												# implicite pentru start si end
												# printul echivalent cu specificarea valorilor explicite
												# ar fi urmatorul: print(f"{prop[12:0:-3]}")
print(f"{prop[12:0:-3]}")

"""
printare normala
[index_start,index_final, pas]
print(f"{prop[0:12:3]}") -> pleaca de la pozita 0 pana la indexul 11
						si extrage elementele cu un pas de 3
print(f"{prop[::3]}") -> acelasi lucru ca mai sus cu folosirea
				valorilor implicite
				
printare in ordine inversa -> se vor inversa pozita de start si endul
[index_final, index_start, pas]			
print(f"{prop[12:0:-3]}") -> pleaca de la pozita 11 pana la indexul 0
						si extrage elementele cu un pas de 3
print(f"{prop[::-3]}") -> acelasi lucru ca mai sus cu folosirea
				valorilor implicite
"""

print(prop[::]) # asta e echivalent cu a scrie print(prop)
prop1 = "johnny canta frumos"
print(f"propozitia 1 cu slicing: {prop[4:9:2]}, propozitia 2 "
			f"cu slicing: {prop1[2:10:5]}")

# intrebare: Ce facem daca vrem sa ne folosim de indexul
			# ultimului caracter dar nu stim cate caractere are stringul?
# exercitiu:  vrem sa extragem tot mai putin penultimul caracter
			# in cazul asta ne putem folosi de functia len
			# ca sa calculam in mod dinamic dimensiunea stringului

prop2 = "Ana are mere si este fericita ca mananca si ea un fruct in sfarsit" \
				"ca de asta iarna tot viseaza la el si saliveaza"

print(f"Textul fara ultimul caracter este:"
			f"{prop2[:len(prop2)-1]}")

# STRING METHODS:

"Exercitiu: vrem sa inlocuim diacriticele " \
"din textul: Ai introdus incorect numele de utilizator sau parola. " \
"Încearcă din nou."

text_de_inlocuit = "Ai introdus incorect numele de utilizator sau parola. Încearcă din nou."
print(f"Textul inainte de formatare este: {text_de_inlocuit}")

text_dupa_inlocuire = text_de_inlocuit.replace("Î","I").replace("ă","a")
print(f"Textul dupa formatare este: {text_dupa_inlocuire}")

print(f"Lungimea textului modificat este: {len(text_dupa_inlocuire)}")

# functia count calculeaza numarul de aparitii ale unui
			# anumit caracter in string
print(f"Caracterul Î apare in mesajul initial de {text_de_inlocuit.count('Î')} ")

# Functia split separa componentele unui text in functie de un separator dat
		# in mod implicit separatorul este caracterul " "
# text_ana_separat = prop.split()
text_ana_separat = prop.split("a")
print(text_ana_separat)

# Putem sa extragem indexul unui anumit element folosindu-ne de metoda index
print(f"Indexul caracterului Î in textul initial este: {text_de_inlocuit.index('Î')}")


