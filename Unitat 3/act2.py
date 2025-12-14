fitxers = ["dades_usuari.txt", "dades_exercici.txt", "dades2.txt"]

try:
    with open("concatenat.txt", "w") as eixida:
        for nom_fitxer in fitxers:
            try:
                with open(nom_fitxer, "r") as entrada:
                    contingut = entrada.read()
                    eixida.write(contingut + "\n")
            except FileNotFoundError:
                print(f"El fitxer {nom_fitxer} no existix.")
            except PermissionError:
                print(f"No tens permisos per a llegir {nom_fitxer}.")
except PermissionError:
    print("No tens permisos per a crear el fitxer de eixida.")
except IOError:
    print("Error en escriure el fitxer de eixida.")

