salariu = 5000
# suma = salariu + 100
# suma = salariu - 100
# suma = salariu * 2
# suma = salariu / 0.05
rest = 11 % 2 	# returneaza 1
power = 2**3 # returneaza 8
suma = 10 // 3 # returneaza 3


power **= 2 # power = power ** 2

angajat = True
an_nastere = 1963

print(angajat == True) # conditie simpla
print(angajat==True and salariu >3000)
print(an_nastere>1060 or angajat==True)
print(not(angajat==True))
print(not angajat)# instructiunea asta este varianta mai scurta a celei anterioare

assert an_nastere == 1963
assert angajat == True, f"Error, valoarea obtinuta nu e corecta. Expected: True, actual: {angajat}"

x = 2
y = 3
if x > y:
 print(f"Numarul {x} este mai mare decat numarul {y}")  # in cazul asta sistemul nu va face nimic, deoarece condiția structurii alternative este evaluata ca fiind falsa, deci nu se va face print-ul

elif y>x:
 print(f"Numarul {y} este mai mare decat numarul {x}") # in cazul asta conditia este evaluata ca fiind adevarata, drept urmare se va printa aceasta propozitie pe ecran

else:
 print("Numerele sunt egale")
