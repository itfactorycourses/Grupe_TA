"""
Ex_2 - Calculare discount seller

Compania X vinde mărfuri la punctele de vânzare pentru cumpărători wholesale și retail.
Clienții wholesale primesc o reducere de două procente la toate comenzile.
De asemenea, compania încurajează atât clienții wholesale, cât și clienții cu amănuntul
să plătească ramburs cash la livrare, oferind o reducere de două procente pentru această metodă de plată.
Încă o reducere de două procente este acordată pentru comenzile de 50 sau mai multe unități.

"""

tip_client = input("Va rugam sa introduceti tipul clientului")
pret_produs = float(input("Va rugam sa introduceti pretul pe bucata al produsului"))
nr_bucati = int(input("Va rugam sa introduceti numarul de bucati"))
tip_plata = input("Va rugam sa introduceti metoda de plata")

discount = 0
if tip_client == "wholesale":
		discount = 0.02
if tip_plata == 'cash':
		discount += 0.02
if nr_bucati >= 50:
		discount += 0.02

pret_final = pret_produs * nr_bucati
pret_final = pret_final - pret_final * discount #(pret_final = pret_produs * nr_bucati - pret_produs * nr_bucati * discount)
