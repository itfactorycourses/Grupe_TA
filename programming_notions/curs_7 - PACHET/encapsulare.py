class Factura():
		"""
		Daca vorbim despre entitatea facturi, o factura este descrisa de atribute cum ar fi
    id-ul de factura, numarul de factura, valoarea, id-ul de client, perioada de
    facturare si data scadenta.
		"""

		# am marcat dictionarul facturi client ca fiind privat prin a scrie __ in fata numelui lui
		__facturi_client = {1:
				{
						"FACT01": {
								"valoare": 0,
								"inceput_facturare": "",
								"sfarsit_facturare": "",
								"data_scadenta": ""}
				}
		}

		__varsta_client = 0

		# mai jos am definit un atribut numit __nume_companie. Am pus _ in fata pentru ca am vrut
		# 		sa definim acest atribut ca fiind protected
		__nume_companie = "Microsoft"

		# mai jos am definit un atribut cu modificatorul de acces implicit, care este public
		an_infiintare = 1967


		def __init__(self, id_client, id_factura, valoare):
				while "FACT" not in id_factura:
						id_factura = input("Va rugam sa introduceti factura corecta. Trebuie sa inceapa cu FACT")
				# self.__facturi_client[id_client] = id_factura
				# self.__facturi_client[id_client][id_factura]["valoare"] = valoare
				self.__facturi_client.update({id_client:{id_factura:{"valoare":valoare}}})


		# atributele private nu pot fi accesate sub nicio forma prin intermediul obiectului.
		# Atunci va trebui sa cream metode specifice pe care sa le folosim ca sa jonglam cu aceste atribute



		# a) Definirea unui getter - adica a unei modalitati prin care sa accesam un atribut private

		@property
		def facturi_client(self):
				return self.__facturi_client

		# mai jos am implementat un setter prin intermediul caruia vom putea modifica
		# atributele dintr-o clasa - in cazul nostru atributul __facturi_client
		# facturi_client(1,"FACT02",34,"2024-03-01","2024-03-31","2024-04-30")
		# @facturi_client.setter
		# def facturi_client(self,tuplu_valori):
		# 		lista_parametri = ['id_client','id_factura','valoare','inceput_facturare','sfarsit_facturare','data_scadenta']
		# 		while tuplu_valori[2]<0:
		# 				valoare = float(input("Va rugam sa introduceti o valoare mai mare ca 0"))
		# 		if tuplu_valori[2] == 0:
		# 				pass
		# 		else:
		# 				self.__facturi_client[tuplu_valori[0]][tuplu_valori[1]]["valoare"] = tuplu_valori[2]
		# 				# self.__facturi_client[1]["FACT02"]["valoare"] = 34
		# 		if tuplu_valori[3] == "":
		# 				pass
		# 		else:
		# 				self.__facturi_client[tuplu_valori[0]][tuplu_valori[1]]["inceput_facturare"] = tuplu_valori[3]
		# 		if tuplu_valori[4] == "":
		# 				pass
		# 		else:
		# 				self.__facturi_client[tuplu_valori[0]][tuplu_valori[1]]["sfarsit_facturare"] = tuplu_valori[4]
		#
		# 		if tuplu_valori[5] != "":
		# 				self.__facturi_client[tuplu_valori[0]][tuplu_valori[1]]["data_scadenta"] = tuplu_valori[5]

		@property
		def varsta(self):
				return self.__varsta_client

		@varsta.setter
		def varsta(self, varsta_noua):
				while varsta_noua <0:
						varsta_noua = int(input("Va rugam sa introduceti varsta corecta "))
				self.__varsta_client = varsta_noua

		@property
		def nume_companie(self):
				return self.__nume_companie

		@nume_companie.setter
		def nume_companie(self,nume_companie):
				self.__nume_companie = nume_companie

		@nume_companie.deleter
		def nume_companie(self):
			self.__nume_companie = ""

		def calculeaza_factura(self, nr_kilowati_luna_curenta, pret_per_kilowat):
				return nr_kilowati_luna_curenta * pret_per_kilowat

		def actualizeaza_data_scadenta(self, id_client, id_factura, noua_data_scadenta):
				self.__facturi_client[id_client][id_factura]["data_scadenta"] = noua_data_scadenta

		def emite_factura(self, id_client, id_factura):
				print(f"Factura cu id-ul {self.__facturi_client[id_client][id_factura]} a fost emisa")
				factura_emisa = True
				return factura_emisa

		def trimite_catre_client(self, adresa_mail_client):
				print(f"Factura pentru clientul {adresa_mail_client} a fost trimisa")




factura_03 = Factura(1,"FACT01",356)
# Instructiunea de mai jos o sa returneze eroare: AttributeError: 'Factura' object has no attribute '__facturi_client'
# eroarea apare pentru ca dictionarul este privat si nu poate fi accesat prin intermediul obiectului
# print(factura_03.__facturi_client)

# Mai jos am folosit un atribut protected si unul public
# print(f"Numele companiei este: {factura_03.__nume_companie} si a fost infiintata in anul {factura_03.an_infiintare}")

# accesam getterul pentru dictionarul de facturi
print(factura_03.facturi_client)
# print(factura_03.__facturi_client)

# print(f"Numele companiei este: {factura_03.nume_companie}")
# factura_03.nume_companie = "IBM"
#
# print(f"Numele companiei este: {factura_03.nume_companie}")

# del factura_03.nume_companie
# print(f"Numele companiei este: {factura_03.nume_companie}")

# print(factura_03.__varsta_client)
factura_03.varsta = -67
print(factura_03.varsta)
