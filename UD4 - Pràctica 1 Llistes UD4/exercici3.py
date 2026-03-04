notes = [5, 7, 9, 4, 6, 3, 1, 8, 2, 10]

# Mostrar totes les notes una per una
for nota in notes:
    print(nota)

# Mostrar nomes les notes aprovades
for nota in notes:
    if nota >= 5:
        print(nota)    
        
#Contar i mostar els nombres d´aprovats i suspesos
aprovats = 0
suspesos = 0

for nota in notes:
    if nota >= 5:
        aprovats += 1
    else:
        suspesos += 1

print("Total aprovats:", aprovats)
print("Total suspesos:", suspesos)        