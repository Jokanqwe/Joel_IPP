elements = ["poma", "pera", "taronja", "plàtan"]
seleccio = None  # variable temporal

try:
    pos = int(input("Introdueix una posició (0-3): "))
    seleccio = elements[pos]
    print(f"L'element a la posició {pos} és: {seleccio}")

except ValueError:
    print("Tens que introduir un número enter.")

except IndexError:
    print("La posició indicada no existix en la llista.")

finally:
    seleccio = None
    print("Intent completat;")
    print(f"Longitud de la llista: {len(elements)}")
    print(f"Valor de seleccio reiniciat: {seleccio}")
