"""

componentele structurii repetitive foreach:
- inceputul structurii repetitive - for
- numele variabilei de iteratie (de regula se va purta numele conceptului care se stocheaza in ea)
- cuvantul "in"
- gruparea de elemente care se va parcurge
- blocul de cod care se va executa atata timp cat nu am ajuns la finalul colectiei de elemente

"""

from TMTA17.programming_notions.curs_3.structuri_de_date.liste import lista_cursanti_prezenti_astazi

for cursant in lista_cursanti_prezenti_astazi:
		print(f"Cursantul {cursant} este prezent la curs")

