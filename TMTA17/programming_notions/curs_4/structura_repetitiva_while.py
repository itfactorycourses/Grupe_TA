"""

Componentele structurii repetitive while:
- inceputul structurii repetitive - while
- conditia de iteratie care se va verifica inainte sa se intre in blocul de cod
- blocul de cod care se va executa atata timp cat nu am ajuns la finalul colectiei de elemente
- incrementarea variabilei de iteratie

"""

from TMTA17.programming_notions.curs_3.structuri_de_date.liste import lista_cursanti_prezenti_astazi

i = 0
while i in range(len(lista_cursanti_prezenti_astazi)):
		print(f"Cursantul {lista_cursanti_prezenti_astazi[i]} este prezent la curs")
		i += 1

# while-ul de mai jos va returna eroare: IndexError: list index out of range
# i = 0
# while i <= len(lista_cursanti_prezenti_astazi):
# 		print(f"Cursantul {lista_cursanti_prezenti_astazi[i]} este prezent la curs")
# 		i += 1

# nu va printa nimic pentru ca "" nu exista in lista
# cursant = ""
# while cursant in lista_cursanti_prezenti_astazi:
# 		print(f"Cursantul {cursant} este prezent la curs")

# while-ul de mai jos va returna eroare
# cursant = "Aurelian"
# while cursant in lista_cursanti_prezenti_astazi:
# 		print(f"Cursantul {cursant} este prezent la curs")

