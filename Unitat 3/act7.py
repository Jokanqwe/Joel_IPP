import csv

dades = []

# Llegir fitxer CSV
try:
    with open("dades_exercici.csv", "r") as fitxer:
        lector = csv.reader(fitxer, delimiter='\t')
        for fila in lector:
            dades.append(fila)
except FileNotFoundError:
    print("Error: El fitxer CSV no existeix.")
except IOError:
    print("Error en llegir el fitxer CSV.")

# Mostrar dades
for fila in dades:
    print(fila)

# Afegir nova fila
nom = input("Introdueix el nom: ")
edat = input("Introdueix l'edat: ")
curs = input("Introdueix el curs: ")
dades.append([nom, edat, curs])

# Guardar dades modificades en un nou fitxer
try:
    with open("estudiants_modificat.csv", "w", newline='') as fitxer:
        escriptor = csv.writer(fitxer, delimiter='\t')
        escriptor.writerows(dades)
    print("Dades guardades al nou fitxer CSV correctament.")
except IOError:
    print("Error en escriure al fitxer CSV.")
