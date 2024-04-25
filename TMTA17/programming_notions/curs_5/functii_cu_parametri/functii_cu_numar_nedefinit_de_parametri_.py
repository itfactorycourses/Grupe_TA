'''

functiile cu args - sunt folosite atunci cand vrem sa definim functii cu un numar indefinit de parametri

'''

# Exercitiu: calculeaza suma a x numere (al caror numar nu il stim de la inceput)
def suma_numere(*lista_parametri):
		suma = 0
		for numar in lista_parametri:
				suma += numar
		print(f"Suma calculata este: {suma}")


suma_numere()
suma_numere(2,3)
suma_numere(5,678,2345,21345)
suma_numere(12,4,6,3.23,2345,234567,234567)
suma_numere([12,4,6,3.23,2345,234567,234567])


