def diaSiguienteA (fecha):
    dian = 0
    mesn = 0
    anion = 0
    bisiesto = False
    if fecha[2] % 4 or fecha[2] % 400:
        bisiesto = True
    if fecha[1] in (1, 3, 5 ,7 ,8 ,10 ,12):
        diames = 31
    elif fecha[1] == 2:
        if bisiesto:
            diames = 29
        else:
            diames = 28
    else:
        diames = 30
    if fecha[0] < diames:
        dian = fecha[0] + 1
        mesn = fecha[1]
    else:
        dian = 1
        mesn = fecha[1] + 1
    if fecha[1] == 12:
        mesn = 1
        anion = fecha[2] + 1
    else:
        anion = fecha[2]
    return (dian, mesn, anion)

print(diaSiguienteA((15,1,2020)))
print(diaSiguienteA((31,1,2020)))
print(diaSiguienteA((28,2,2020)))
print(diaSiguienteA((31,12,2020)))
