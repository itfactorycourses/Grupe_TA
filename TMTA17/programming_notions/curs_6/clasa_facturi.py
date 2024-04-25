# Ca sa definim o clasa ne folosim de cuvantul cheie class (echivalentul cuvantului
# 		cheie def de la functii) urmat de numele clasei
#     prin conventie numele clasei incepe cu litera mare si orice caracter care urmeaza va fi
# 		scris cu litera mica. Numele unei clase de regula urmeaza tiparul CamelCase
# 		La fel ca si la functii putem sa punem paranteze rotunde dupa numele clasei,
# 		insa acestea sunt obligatorii doar in anumite situatii (ex: mostenire - facem la cursul urmator)
# 		La fel ca la if, structuri repetitive si functii, blocul de cod dintr-o clasa este marcat de indentare
# 		anuntarea blocului de cod se face ca de obicei prin caracterul ":"

class Factura():
		"""
		Daca vorbim despre entitatea facturi, o factura este descrisa de atribute cum ar fi
    id-ul de factura, numarul de factura, valoarea, id-ul de client, perioada de
    facturare si data scadenta.
		"""
		facturi_client = {1:
												{
														"FACT01":{
																		"valoare": 0,
																		"inceput_facturare":"",
																		"sfarsit_facturare":"",
																		"data_scadenta":""}
												}
											}

		"""
		Constructorul este un element dintr-un limbaj de programare care este folosit
		pentru instantierea obiectelor dintr-o clasa
		
		De fiecare care data cand instantiem un obiect se va apela un constructor.
		
		Exista doua tipuri de constructori:
		- constructorul implicit -> cel existent in mod implicit in Python si care este apelat
															atunci cand nu am definit noi un constructor 

		- constructor explicit care este definit de catre dezvoltator atunci cand vrem sa controlam
					valorile cu care se instantiaza obiectele
					
		Definirea unui constructor in python se defineste intotdeauna cu numele __init__
		"""

		# factura_03 = Factura("floricele")

		def __init__(self, id_client,id_factura,valoare):
				while "FACT" not in id_factura:
						id_factura = input("Va rugam sa introduceti factura corecta. Trebuie sa inceapa cu FACT")
				self.facturi_client[id_client][id_factura]["valoare"] = valoare

		"""  
    Daca vorbim despre actiunile care pot fi facute pe o factura vorbim despre 
    calculul facturii, emiterea facturii, trimiterea ei catre client, si plata facturii
    """

		"""

				insert into facturi(1,"Ion Popescu", "FACT01","31-03-2024",emite_factura())
				insert into facturi(2,"Andrei Marinescu", "FACT02","31-02-2024",emite_factura())
				insert into facturi(3,"Maria Ionescu", "FACT03","31-02-2024",emite_factura())

					clienti

					facturi
					id_client,			nume_client, 				id_factura, 		data_scadenta			este_platita
					1								Ion popescu					FACT01					31.03.2024				NU
					2								Andrei Marinescu		FACT02					31.02.2024				NU
					3								Maria Ionescu				FACT03					31.02.2024				DA

					select * from facturi where este_platita = "NU" and data_scadenta<current_date() 

					"""

		# Vrem sa definim o functie care va folosi numarul de kilowati folositi de catre client in luna curenta
				# si respectiv pretul per kilowat. Functia va trebui sa calculeze valoarea facturii in functie de aceste valori

		# O functie care este definita intr-o clasa se numeste metoda

		# dupa cum observati mai jos, in interiorul listei de parametri am pus cuvantul cheie "self"
			# acest cuvant cheie anunta sistemul in cazul asta ca noi vrem sa definim un element specific clasei

		def calculeaza_factura(self,nr_kilowati_luna_curenta, pret_per_kilowat):
				return nr_kilowati_luna_curenta * pret_per_kilowat

		def actualizeaza_data_scadenta(self,id_client,id_factura,noua_data_scadenta):
				self.facturi_client[id_client][id_factura]["data_scadenta"] = noua_data_scadenta

		def emite_factura(self,id_client, id_factura):
				print(f"Factura cu id-ul {self.facturi_client[id_client][id_factura]} a fost emisa")
				factura_emisa = True
				return factura_emisa

		def trimite_catre_client(self,adresa_mail_client):
				print(f"Factura pentru clientul {adresa_mail_client} a fost trimisa")


# Pentru a instantia (echivalentul initializarii) un obiect dintr-o clasa o
# sa scriem numele obiectului urmat de caracterul "=" si apoi urmat de numele clasei
# din care facem instantierea si respectiv doua paranteze rotunde
# 			(in cazul asta numele clasei va fi tratat ca o functie)
#				daca nu punem paranteze rotunde sistemul va crede ca in adresa de memorie
# 			definita de numele obiectului pe care l-am creat vrem sa salvam
			# valoarea de la o alta adresa de memorie definita de numele clasei specificat in dreapta
			# operatorului de atribuire
			# in python merge si fara sa punem paranteze rotunde dupa numele clasei la instantiere
			# dar alte limbaje nu or sa fie la fel de permisive

# La linia de mai jos am instantiat un obiect din clasa Factura numit factura_01
# in mod implicit fiecare obiect va avea salvat pe atribute valorile implicite
# definite in clasa. Dar noi putem sa suprascriem aceste valori
# ca sa le suprascriem in primul rand le apelam si apoi le modificam valoarea prin intermediul
# operatorului de atribuire.
# accesarea atributelor din clasa se face INTOTDEAUNA prin intermediul obiectului
				# accesarea se va face prin specificara numelui obiectului urmat de caracterul "."
						# la fel ca la functiile structurilor de date
# factura_01 = Factura("FACT01")
# factura_01.id_client = 1
# print(f"Id-ul de factura pentru clientul {factura_01.id_client} este {factura_01.id_factura}")

# Instructiunea de mai jos va returna eroare: TypeError: Factura.__init__() missing 1 required positional argument: 'id_factura'
# Eroarea apare pentru ca din constructor asteapta sa primeasca un argument
	# pe care nu l-a primit
# factura_02 = Factura()
# factura_02.id_factura = "FACT02"
# factura_02.id_client = 2
# print(factura_02) # Va printa adresa de memorie la care este salvat obiectul

# lista_Test = ["Test1","test"]
# lista_facturi = [factura_01,factura_02]
#
# for factura in lista_facturi:
# 	print(f"Id-ul de factura pentru clientul {factura.id_client} este {factura.id_factura}")
#
# factura_01.emite_factura()
# # print(factura_01.trimite_catre_client("ion.popescu@gmail.com"))
# # factura_01.trimite_catre_client("ion.popescu@gmail.com")

factura_03 = Factura(1,"FACT",356)
print(f"Valoarea facturii este: {factura_03.facturi_client[1]['FACT01']}")