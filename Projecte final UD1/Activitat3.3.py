def suma(num1, num2=5):
    return num1 + num2

num1 = float(input("Introdueix el primer número: "))

entrada = input("Introdueix el segon número (o apreta Enter per a usar el valor per defecte 5): ")

if entrada == "":
    num2 = 5
else:
    num2 = float(entrada)

resultat = suma(num1, num2)
print(f"la suma es: {resultat}")
