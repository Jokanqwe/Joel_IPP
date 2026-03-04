temperatura = float(input("Que temperatura fa? "))
nuvol = input("Fa nuvol? ")

if nuvol.lower() == "si":      #.lower fa que el programa torne a miniscula lo que li arriba
    nuvol = True
else:
    nuvol = False


if temperatura <= 0:
    print("Fa un fred polar!")
elif temperatura > 0 and temperatura <= 15:
    if nuvol:
        print("Fa fred i el dia esta trist")
    else:
        print("Fa fresqueta però el sol alegra el dia")
elif temperatura >= 16 and temperatura <= 25:
    if nuvol:
        print("Temperatura agradable, però potser ploga.")
    else:
        print("Dia perfecte per a eixir a passetjar!")
elif temperatura >= 26 and temperatura <= 35:
    print("Fa calor, millor buscar sombra.")
elif temperatura > 35:
    if nuvol:
        print("Calor i humitat... una combinació infernal!")
    else:
        print("Fa una calor que fon les pedres!")