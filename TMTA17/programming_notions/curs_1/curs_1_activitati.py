
# Creați o variabilă care să stocheze cu ce vă ocupați în momentul ăsta
job_actual_adina = "administrator"

# Creați câteva constante care să stocheze fiecare, pe rand, numele vostru,
# data nașterii, data la care v-ați înscris la curs. De ce le-am creat ca și constante
# în loc de variabile? Valorile se vor da de la tastatură prin intermediul funcției input.

# NUME = input("Va rugam sa introduceti numele")
# DATA_NASTERII = input("Va rugam sa introduceti data nasterii")
# DATA_INSCRIERE = input("Va rugam sa introduceti data inscrierii")
# varsta = int(input("Va rugam sa introduceti varsta "))
# print(type(varsta))

# Definiți o nouă variabilă numită procent_invatare care va stoca un procent ce va descrie
# nivelul de informații pe care credeți că ați ajuns să le stăpâniți de la începutul
# cursului de testare manuală și pânâ acum (ca un fel de auto-evaluare).
procent_invatare = "50%"
procent_invatare = 0.5

# Definiți o nouă variabilă care să se numească sunt_pregatit_de_examen
# și care să stocheze valoarea corespunzătoare.
sunt_pregatit_de_examen = False

# Ce tip de dată are fiecare din cele create?
# sunt_pregatit_de_examen => bool
# procent_invatare = 0.5 => float
# procent_invatare = "50%" => string
# job_actual_adina = "administrator" => string

# Printați pe ecran într-o singură propoziție toate informațiile de mai sus
# folosind trei tipuri de printare. Ce observați în fiecare caz?
# Cum am putea sa rezolvăm eventualele probleme?

"Adina are un job de administrator si are un procent de invatare de 50%. " \
"Este pregatita pentru examen? False"

# # printul asta o sa returneze eroare
# print("Adina are un job de " + job_actual_adina + " si are un procent de invatare de "
# 			+  procent_invatare + "Este pregatita pentru examen? " + sunt_pregatit_de_examen)

print("Adina are un job de " + job_actual_adina + " si are un procent de invatare de "
			+  str(procent_invatare) + "Este pregatita pentru examen? " + str(sunt_pregatit_de_examen))

print(f"Adina are un job de {job_actual_adina} si are un procent de invatare "
			f"de {procent_invatare}. Este pregatita pentru examen? {sunt_pregatit_de_examen}")

# O SA RAMANA CA TEMA PE LANGA CE AVETI LA STUDIUL IN ECHIPA

# Definiți o nouă constantă care să reprezinte valoarea unei excursii
# pe care ați achiziționat-o recent și respectiv una care să stocheze un
# eventual discount pe care l-ați avut (dacă nu a existat, acesta va fi 0).
# Valorile se vor da de la tastatură.
# În final, veți calcula valoarea finală a călătoriei folosind prețul de bază al
# biletului și valoarea discountului.
# Ce trebuie sa îi faceti funcției input pentru ca acest exercițiu să funcționeze?

VALOARE_EXCURSIE = float(input("Va rugam sa introduceti valoarea excursiei "))
PROCENT_DISCOUNT = float(input("Va rugam sa introduceti procentul de discount aplicat "))
VALOARE_DISCOUNT = VALOARE_EXCURSIE * PROCENT_DISCOUNT
valoare_excursie_cu_discount = VALOARE_EXCURSIE - VALOARE_DISCOUNT
print(f"Valoare initiala excursie: {VALOARE_EXCURSIE}")
print(f"Procent discount: {PROCENT_DISCOUNT}")
print(f"Valoare discount: {VALOARE_DISCOUNT}")

print(f"Valoarea excursiei cu discount este {valoare_excursie_cu_discount}")
# Adăugați comentarii înaintea fiecărei linii de cod și explicați ce face