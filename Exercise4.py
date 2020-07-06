def diaSiguienteA (fecha):
    dian = 0
    mesn = ""
    anion = 0
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    bisiesto = False
    if fecha[2] % 4 or fecha[2] % 400:
        bisiesto = True
    if fecha[1] in ("Ene", "Mar", "May" ,"Jul" ,"Ago" ,"Oct" ,"Dic"):
        diames = 31
    elif fecha[1] == "Feb":
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
        temp = False
        for i in meses:
            if temp == True:
                mesn = i
                break
            if fecha[1] == i:
                temp = True
    if fecha[1] == "Dic":
        mesn = "Ene"
        anion = fecha[2] + 1
    else:
        anion = fecha[2]
    return (dian, mesn, anion)

print(diaSiguienteA((15,"Ene",2020)))
print(diaSiguienteA((31,"Ene",2020)))
print(diaSiguienteA((28,"Feb",2020)))
print(diaSiguienteA((31,"Dic",2020)))
