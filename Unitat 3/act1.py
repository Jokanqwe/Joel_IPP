nom = input("Com el diuen?: ")
edat = input("Quants anys tens?: ")

try:
    with open("dades_usuari.txt", "w") as fitxer:
        fitxer.write(f"Nom: {nom}\n")
        fitxer.write(f"Edat: {edat}\n")
    print("Dades guardades correctament.")

except PermissionError:
    print("Error: No tens permisos per a escriure en el fitxer.")
except IOError:
    print("S'ha produït un error al escriure en el fitxer.")
try:
    with open("dades_usuari.txt", "r") as fitxer:
        contingut = fitxer.read()
        print("\nContingut del fitxer:")
        print(contingut)

except FileNotFoundError:
    print("Error: El fitxer no existeix.")
except PermissionError:
    print("Error: No tens permisos per a llegir el fitxer.")
except IOError:
    print("S'ha produït un error al llegir el fitxer.")

ciutat = input("Introduix una ciutat: ")

try:
    with open("dades_usuari.txt", "a") as fitxer:
        fitxer.write(f"Ciutat: {ciutat}\n")
    print("Nova dada afegida correctament.")

except PermissionError:
    print("Error: No tens permisos per a afegir dades en el fitxer.")
except IOError:
    print("S'ha produït un error al afegir dades en el fitxer.")
