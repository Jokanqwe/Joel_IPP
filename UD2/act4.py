suma = 0
comptador_parells = 0

for i in range(1, 7):
    if i % 2 == 0:
        suma = suma + i
        comptador_parells = comptador_parells + 1
    else:
        suma = suma - 1

print("Resultat final:")
print("suma =", suma)
print("comptador_parells =", comptador_parells)

# i  parell? suma  comptador parells
# 1  no      -1    0
# 2  sí      1     1
# 3  no      0     1
# 4  sí      4     2
# 5  no      3     2
# 6  sí      9     3