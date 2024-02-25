# # Definiți o adresă de memorie care să salveze data curentă.
# # Va fi o variabilă sau o constantă?
#
# CURRENT_DATE = '2024-01-03' """ va fi o constanta pentru ca data curenta ramane constanta,
# 					 foarte rar vor exista programe care sa ruleze de pe o zi pe alta sa aiba nevoie de
# 					 modificarea datei curente in timpul executiei"""
#
# # am printat tipul de date al constantei declarate
# print(type(CURRENT_DATE))
#
# # Am definit trei variabile diferite
# la_ce_curs_sunt = "Testare Automata"
# ce_zi_este = "Miercuri"
# la_ce_sesiune_de_curs_suntem = "Sesiunea 1"
#
# # Am stocat fiecare valoare din propozitie in cate un cuvant
# cuv1, cuv2, cuv3, cuv4, cuv5, cuv6 = "Ana","s-a","nascut","in","anul", 1990
#
# # Alta sugestie de rezolvare: folosirea metodei split si salvarea rezultatelor intr-o lista
# 		# listele se vor studia la cursurile viitoare
# propozitie = "Ana are mere"
# word_list = propozitie.split(" ")
#
# # Am folosit trei tipuri de printuri, dintre care primul va returna eroare
# print(cuv1 + cuv2 + cuv3 + cuv4 + cuv5 + cuv6) # va returna eroare din cauza incompatibilitatii de tip
# print(cuv1 + cuv2 + cuv3 + cuv4 + cuv5 + str(cuv6))
# print(f"{cuv1} {cuv2} {cuv3} {cuv4} {cuv5} {cuv6}")
#
# # # Am declarat cateva variabile populate prin functia input
# # nume = input("Va rugam sa introduceti numele")
# # prenume = input("Va rugam sa introduceti prenumele")
# # varsta = input("Va rugam sa introduceti varsta")
# # adresa_mail = input("Va rugam sa va introduceti adresa de email")
# # salariu = input("Va rugam sa va introduceti salariul")
