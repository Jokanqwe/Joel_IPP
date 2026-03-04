contador = 0

while True:
    contar= int(input("Introdueixme un numero (0 pa acabar):"))

    if contar == 0:
        break
    elif contar > 0:
        contador += 1

print("Has introduit", contador, "numeros positius antes que el 0")