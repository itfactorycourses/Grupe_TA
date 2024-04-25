"""
Cum functioneaza programarea?

Noi atunci cand scriem cod, il scriem astfel incat sa putem sa il citim noi.
Problema e ca sistemul nu intelege conceptul de litere si cifre.
Si atunci noi trebuie sa ii asiguram sistemului un traducator.
Acest traducator se numeste in python interpretor (sau o sa mai auziti
termenul de compilator).

Cum functioneaza interpretarea?
Codul pe care il scriem este tradus in cod ASCII si apoi in cod binar.
ASCII Code: https://www.ascii-code.com/

Fiecare numar are in spate un corespondent in tabelul ASCII. Acel corespondent
este un numar zecimal (un numar in baza 10)

Acel numar zecimal este transformat din baza 10 in baza doi.
Numerele care se afla in baza doi se numesc numere binare.

Sistemul intelege doar valori scrise in cod binar.

Spre exemplu 65 in binar este 1000001.
A -> 65 -> 1000001 -> pe asta il intelege sistemul
1000001 -> 65 -> A

Dimensiuni standard de stocare a datelor in programare:

- in general, atunci cand vorbim de dimensiunea anumitor adrese de memorie
vorbim despre numarul de valori binare care pot sa fie salvate la acea
adresa de memorie.
Cea mai mica unitate de masura este bit-ul.  Un bit este echivalentul
		unei singure cifre 0 sau 1 (valoare binara)

Urmatoarea unitate de masura dupa bit este un byte, care are 8 biti.
De aceeea atunci cand noi reprezentam un caracter care are o reprezentare
interna mai mica de 8 biti, restul de biti se vor completa cu cifra 0

De exemplu, reprezentarea interna a lui A (care in binar este 1000001)
va fi 10000010

0 x 2(0) + 1 x 2(1) + 00000 + 1 x 2(7)
0 + 2 + 0 + 128

Urmatoarea unitate de masura dupa byte este kilobyte care are 1024 de bytes
Urmatoarea unitate de masura dupa kb este megabyte care are 1024 de kb
Urmatoarea unitate de masura dupa mb este gigabyte care are 1024 de mb

Terminal = locul in care noi vom trimite comenzi de la tastatura in python
		si / sau locul in care vedem rezultatul executiei comenzilor

IDE = Integrated Development Environment -> locul in care scriem cod
			Pycharm este un IDE
			Eclipse sau Intellij este tot un IDE
"""

