#logica del salto estación
# 0 para saltarla 1 para ejecutarla
stations=['Station_ASRS','Station_Inspection','Station_ASRS2']
run = [1,0,0,0,1]

if "Station_Lathe" in stations:
    run[1] = 1
if "Station_Melling" in stations:
    run[2] = 1
if "Station_Inspection" in stations:
    run[3] = 1

print(run)