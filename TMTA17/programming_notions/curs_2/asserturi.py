'''

asserturile sunt componenta de baza a unui test. Ele reprezinta compararea
intre rezultatul asteptat si rezultatul actual

assert este traducerea in engleza a cuvantului evaluare

assertul in mod normal este ultima instructiune a unei metode de test
pentru ca scopul final al unui test este sa faca o evaluare

Structura unui assert:
Începutul assertului (keyword-ul assert)
Valoarea cu care se compară (expected result)
Valoarea care se compară (actual result)
Mesaj de eroare în cazul în care cele două nu sunt egale (opțional)
'''

expected_message = "Parola Invalida. Parola trebuie sa aiba cel putin 8 caractere si sa contina litere, cifre si caractere speciale"
actual_message = "Error"


# print("Definire corecta assert: ")
# assert expected_message == actual_message, f"Error: expected message: {expected_message}, actual message: {actual_message}"
#
# # In programare liniile de cod se ruleaza secvential in ordinea in care sunt scrise
# # In momentul in care un assert este failed, urmatoarele instructiuni dupa acel assert nu se vor mai executa
# # De exemplu, printul si assertul de mai jos nu se vor mai executa pentru ca eroarea returnata de assert
# # 		va opri executia codului
# print("Definire incorecta mesaj de eroare assert: ")
# assert expected_message == actual_message, expected_message

# Sa presupunem ca am raportat bug-ul cu mesajul incorect catre dezvoltare,
# si mesajul a fost actualiza la urmatorul:
actual_message = "Parola Invalida. Parola trebuie sa aiba cel putin 8 caractere si sa contina litere, cifre si caractere speciale"

# Vom reexecuta assertul (retesting) si vom vedea faptul ca bug-ul a fost fixat
assert expected_message == actual_message, f"Error: expected message: {expected_message}, actual message: {actual_message}"
