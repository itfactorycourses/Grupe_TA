class Restaurant():
		numar_cutite = 0
		lista_mancaruri_servite = []
		nume_restaurant = ""
		adresa_restaurant = ""

		def toaca_ceapa(self):
				print("am tocat ceapa")

		def curata_cartofi(self):
				print("am curatat cartofii")

# mai jos clasa Chef mosteneste clasa Restaurant prin faptul ca am pus clasa mostenita intre paranteze
# in contextul de mai jos clasa Chef este clasa copil si clasa Restaurant este clasa parinte
# clasa Chef va avea acces la toate atributele si metodele clasei Restaurant prin intermediul
# 		unui obiect instantiat din clasa Chef.
# clasa Restaurant NU VA AVEA ACCES decat la metodele si atributele din clasa Restaurant,
# 			NU SI DIN CLASA Chef

class Chef(Restaurant):
		nume_chef = ""
		numar_telefon = ""
		data_angajare = ""
		pozitie = ""

		def pregateste_tort_red_velvet(self):
				print("am amestecat ingredientele si am copt tortul")

		def pregateste_gulas(self):
				print("am pregatit gulas unguresc")

# Am instantiat mai jos un obiect din clasa Restaurant si un obiect din clasa Chef
obiect_restaurant = Restaurant()
obiect_chef = Chef()
print(f"Restaurantul {obiect_restaurant.nume_restaurant} se afla la adresa {obiect_restaurant.adresa_restaurant}"
			f"serveste urmatoarele mancaruri: {obiect_restaurant.lista_mancaruri_servite} si are"
			f"{obiect_restaurant.numar_cutite} cutite")
obiect_restaurant.curata_cartofi()
obiect_restaurant.toaca_ceapa()

print(f"Chef-ul {obiect_chef.nume_chef} lucreaza la restaurantul {obiect_chef.nume_restaurant}"
			f"si s-a angajat la data de {obiect_chef.data_angajare} pe pozitia de {obiect_chef.pozitie}")