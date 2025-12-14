import json
import csv
import os
import shutil

# Crear directori per fitxers antics si no existeix
directori_antics = "fitxers_antics"
os.makedirs(directori_antics, exist_ok=True)

# Llegir fitxer JSON existent
try:
    with open("dades_exercici.json", "r") as fitxer_json:
        dades_exercici = json.load(fitxer_json)
except FileNotFoundError:
    print("Fitxer JSON no trobat. Creant un nou llistat.")
    dades_exercici = []
except json.JSONDecodeError:
    print("Fitxer JSON invàlid. Iniciant llista buida.")
    dades_exercici = []

# Afegir nou estudiant
nom = input("Nom de l'estudiant: ")
edat = int(input("Edat: "))
nota = float(input("Nota: "))
assignatures = input("Assignatures separades per coma: ").split(",")
nou_estudiant = {"nom": nom, "edat": edat, "nota": nota, "assignatures": [a.strip() for a in assignatures]}
dades_exercici.append(nou_estudiant)

# Guardar JSON actualitzat
try:
    with open("dades_exercici.json", "w") as fitxer_json:
        json.dump(dades_exercici, fitxer_json, indent=4)
except IOError:
    print("Error en escriure al fitxer JSON.")

# Gestionar fitxer CSV existent
if os.path.exists("dades_exercici.csv"):
    shutil.move("dades_exercici.csv", os.path.join(directori_antics, "dades_exercici.csv"))

# Crear fitxer CSV amb la informació actualitzada
try:
    with open("dades_exercici.csv", "w", newline='') as fitxer_csv:
        escriptor = csv.writer(fitxer_csv)
        escriptor.writerow(["Nom", "Edat", "Nota", "Assignatures"])
        for e in dades_exercici:
            escriptor.writerow([e["nom"], e["edat"], e["nota"], ", ".join(e["assignatures"])])
    print("Fitxer CSV creat correctament.")
except IOError:
    print("Error en escriure al fitxer CSV.")