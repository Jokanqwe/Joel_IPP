import json

try:
    with open("dades_exercici.json", "r") as fitxer:
        dades = json.load(fitxer)

    nom_estudiant = input("Introdueix el nom de l'estudiant a modificar: ")
    nova_assignatura = input("Introdueix una nova assignatura: ")

    for estudiant in dades:
        if estudiant["nom"] == nom_estudiant:
            estudiant["assignatures"].append(nova_assignatura)

    with open("estudiants.json", "w") as fitxer:
        json.dump(dades, fitxer, indent=4)

except FileNotFoundError:
    print("El fitxer JSON no existeix.")
except json.JSONDecodeError:
    print("Error: el fitxer no conté dades JSON vàlides.")
