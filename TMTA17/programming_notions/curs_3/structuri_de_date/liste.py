# # 1. Declarea si initializarea unei liste goale
# lista_goala = []
#
# # 2.Declararea si initializarea unei liste populate
lista_cursanti_prezenti_astazi = ["Aurelian","Daniela","Dino","Roby","Alexandra","Garofita","Florin","Octavian","Lidia","Alex","Vali","Marian"]
#
# # 3. Declararea si initializare unei liste multitype (Adica cu elemente din mai multe tipuri de date)
# lista_multitype = ["ana are mere",356,345.879,True]
#
# # 4. Accesarea unui element de la un index specific din interiorul listei
# # 			Se poate face prin specificarea intre paranteze patrate a indexului acelui element
# # 			Exercitiu: vrem sa accesam elementul din pozitia 5 din lista lista_cursanti_prezenti_astazi
# # 			Vrem sa printam pe ecran urmatoarea: "Cursantul din pozitia 5 este nume_cursant"
# print(f"Cursantul din pozitia 5 este {lista_cursanti_prezenti_astazi[4]}")
# print("Cursantul din pozitia 5 este" + str(lista_cursanti_prezenti_astazi[4]))
#
# # FUNCTII CU CARE PUTEM INTERACTIONA CU LISTELE
# # 			Ca sa accesam functiile unei liste scriem numele listei, urmat de '.' si vom
# # 			primi o lista cu toate functiile disponibile pentru liste
#
#
# # 5. Adaugarea unui element in lista, la finalul listei -> APPEND
# print(f"Lista inainte de adaugarea Adinei este {lista_cursanti_prezenti_astazi}")
# lista_cursanti_prezenti_astazi.append("Adina")
# print(f"Lista dupa adaugarea Adinei este {lista_cursanti_prezenti_astazi}")
#
# # Adaugarea unui element in lista, la un anumit index -> INSERT
# print(f"Lista inainte de adaugarea Paulei este {lista_cursanti_prezenti_astazi}")
# lista_cursanti_prezenti_astazi.insert(0,"Paula")
# print(f"Lista dupa adaugarea Paulei este {lista_cursanti_prezenti_astazi}")
#
# # Stergerea ultimului element din lista:
# print(f"Lista inainte pop {lista_cursanti_prezenti_astazi}")
# # a) Stergerea unui element cu index implicit (ultimul)
# lista_cursanti_prezenti_astazi.pop()
# print(f"Lista dupa pop implicit {lista_cursanti_prezenti_astazi}")
# # b) Stergerea unui element cu index eximplicit (dat de la tastatura)
# lista_cursanti_prezenti_astazi.pop(0)
# print(f"Lista dupa pop explicit {lista_cursanti_prezenti_astazi}")
# # b) Stergerea unui element cu index mai mare decat lungimea listei - va returna eroare
# # lista_cursanti_prezenti_astazi.pop(15)
# # print(f"Lista dupa pop cu index mai mare este:  {lista_cursanti_prezenti_astazi}")
#
# # Stergerea unui element din lista pe baza de remove
# # 		- primeste ca argument valoarea elementului, nu indexul elementului:
# lista_cursanti_prezenti_astazi.remove("Octavian")
# print(f"Lista dupa remove {lista_cursanti_prezenti_astazi}")
#
# # Apelarea functiei remove pe un element care nu exista:
# # lista_cursanti_prezenti_astazi.remove("Liliana")
#
# # Aflarea indexului unui element din lista - METODA INDEX
# print(f"Alexandra se afla in lista la pozitia {lista_cursanti_prezenti_astazi.index('Alexandra')}")
#
# # # Sortarea listei - METODA SORT
# # lista_cursanti_prezenti_astazi.sort()
# # print(f"Lista dupa sortare este: {lista_cursanti_prezenti_astazi}")
# # print(f"Alexandra se afla in lista la pozitia {lista_cursanti_prezenti_astazi.index('Alexandra')}")
#
# # Folosirea functiei reverse - adica ia elementele de la coada la cap:
# lista_cursanti_prezenti_astazi.reverse()
# print(f"Lista dupa reverse este: {lista_cursanti_prezenti_astazi}")
#
# lista_multitype.reverse()
# print(f"Lista lista_multitype dupa reverse este: {lista_multitype}")
#
# # Functia copy eturneaza o copie a listei
# print(f"Lista inainte de copy este: {lista_cursanti_prezenti_astazi}")
# lista_cursanti_copy = lista_cursanti_prezenti_astazi.copy()
# print(f"Lista dupa de copy este: {lista_cursanti_prezenti_astazi}")
# lista_cursanti_prezenti_astazi.append("Adina")
# print(f"Lista dupa de append este: {lista_cursanti_prezenti_astazi}")
# print(f"Lista lista_cursanti_copy dupa de copy este: {lista_cursanti_copy}")
#
# # Functia extend => adauga lista dintre paranteze la lista initiala
# zile_sapt = ["luni","marti","miercuri","joi","vineri"]
# weekend = ["sambata","duminica"]
# print(f"Zilele de munca sunt: {zile_sapt}")
# print(f"Zilele de weekend sunt: {weekend}")
# zile_sapt.extend(weekend)
# print(f"Lista zile_sapt dupa apelarea metodei extent: {zile_sapt}")
#
# # METODA COUNT - numara de cate ori apare un element in lista
# print(f"Alexandra apare in lista de {lista_cursanti_prezenti_astazi.count('Alexandra')} ori")
#
# # Functia LEN - calculeaza dimensiunea listei - adica cate elemente sunt in lista
# print(f"Lista lista_cursanti_prezenti_astazi are {len(lista_cursanti_prezenti_astazi)} elemente")
#
# #  Functia CLEAR goleste lista
# lista_cursanti_prezenti_astazi.clear()
# print(f"Lista dupa golire este: {lista_cursanti_prezenti_astazi}")
#
# # stergerea adresei de memorie in care se afla lista:
# # del lista_cursanti_prezenti_astazi
#
# # Accesarea ulterioara a listei va returna eroare:
# # print(lista_cursanti_prezenti_astazi)
#
# print(type(set(lista_cursanti_prezenti_astazi)))

