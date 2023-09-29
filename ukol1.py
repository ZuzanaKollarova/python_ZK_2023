jmeno = "Zuzana"
prijmeni = "Kollarova"
print(f"e-mailová adresa je {jmeno}.{prijmeni}@czechitas.cz")

velka_pismena = jmeno.upper(), prijmeni.upper()
print (f"Jméno velkými písmeny: {velka_pismena}")

mala_pismena = jmeno.lower(), prijmeni.lower()
print (f"Jméno malými písmeny: {mala_pismena}")

jmeno_prijmeni = input("Zadaj jméno a příjmení: ")
zmena_velka = jmeno_prijmeni.upper()
print (f"Jméno velkými písmeny, druhý pokus: {zmena_velka}")

zmena_mala = jmeno_prijmeni.lower()
print (f"Jméno malými písmeny, druhý pokus: {zmena_mala}")