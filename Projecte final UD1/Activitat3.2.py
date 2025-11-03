import math

def area_cercle(radi):
    return math.pi * (radi ** 2)

radi = float(input("Introduix el radi del cercle: "))
print("L'area del cercle és:", area_cercle(radi))
