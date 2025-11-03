pes = float(input("Introdueix el teu pes (kg): "))
altura = float(input("Introdueix la teva altura (m): "))

imc = pes / (altura ** 2)
print("El teu IMC és:", round(imc, 2))

if imc < 18.5:
    print("Inferior al pes saludable.")
elif imc <= 24.9:
    print("Pes saludable.")
else:
    print("pes no saludable.")
