"""
Devolver la edad a partir de dos fechas

Params
fecha_nacimiento: str -> "dd/mm/aaaa"
fecha_actual: str -> "dd/mm/aaaa"

Return
edad: int

Codigos de error:
-1 : dia o mes o año incorrecto
-2 : la fecha de nacimiento debe ser igual o menor que la actual
"""

def calcula_edad(fecha_nacimiento : str, fecha_actual : str) -> int:
    """
    Devolver la edad a partir de dos fechas

    Params
    fecha_nacimiento: str -> "dd/mm/aaaa"
    fecha_actual: str -> "dd/mm/aaaa"

    Return
    edad: int

    Codigos de error:
    -1 : dia o mes o año incorrecto
    -2 : la fecha de nacimiento debe ser igual o menor que la actual
    """

    # fecha_actual = "18/02/2025"
    fecha_act = fecha_actual.split("/")
    actual = {"dia": int(fecha_act[0]), "mes" : int(fecha_act[1]), "año" : int(fecha_act[2])}
    # fecha_nacimiento = input("La fecha de nacimiento es: ----> ")

    fecha_nac = fecha_nacimiento.split("/")
    nac = {"dia": int(fecha_nac[0]), "mes": int(fecha_nac[1]), "año" : int(fecha_nac[2])}
    # fecha_nacimiento.split("/") = {"dia" : dia, "mes" : mes, "año" : año}

    if (nac["año"], nac["mes"], nac["dia"]) > (actual["año"], actual["mes"], actual["dia"]):
        return -1
    
    dif_anyos = actual["año"] - nac["año"]
    if dif_anyos < 0:
        return -1
    
    if nac["mes"] > actual["mes"] or (nac["mes"] == actual["mes"] and nac["dia"] > actual["dia"]):
        dif_anyos -= 1

    
    # if (not 1 < nac["año"] <= 12) \
    #     or (not 1 <= nac["año"] <= 12) \
    #         or (not 1 <= actual["mes"] <= 30) \
    #             or (not 1<= nac["mes"] <= 30):
    #     return -2

    dias_nac = nac["año"] * 360 + nac["mes"] * 30 + nac["dia"]
    dias_act = actual["año"] * 360 + actual["mes"] * 30 + actual["dia"]

    edad = (dias_act - dias_nac) // 360
    return edad

print(calcula_edad("18/01/2000", "18/02/2025"))
    

# def calcula_edad(fecha_nacimiento : str, fecha_actual : str) -> int:

#     """
# Devolver la edad a partir de dos fechas

# Params
# fecha_nacimiento: str -> "dd/mm/aaaa"
# fecha_actual: str -> "dd/mm/aaaa"

# Return
# edad: int

# Codigos de error:
# -1 : dia o mes o año incorrecto
# -2 : la fecha de nacimiento debe ser igual o menor que la actual
# """

#     fecha_actual = fecha_actual.split("/")
#     dia_actual = int(fecha_actual[0])
#     mes_actual = int(fecha_actual[1])
#     anyo_actual = int(fecha_actual[2])

#     fecha_nacimiento = fecha_nacimiento.split("/")
#     dia_nacimiento = int(fecha_nacimiento[0])
#     mes_nacimiento = int(fecha_nacimiento[1])
#     anyo_nacimiento = int(fecha_nacimiento[2])

#     if (not 1<= mes_actual <= 12) \
#         or (not 1<= mes_nacimiento <= 12) \
#             or (not 1<= dia_actual <= 30) \
#                 or (not 1<= dia_nacimiento <= 30):
#         return -1

#     # No se puede calcular la edad si la fecha de nacimiento es posterior a la actual
#     dif_anyos = anyo_actual - anyo_nacimiento
#     dif_meses = mes_actual - mes_nacimiento
#     dif_dias = dia_actual - dia_nacimiento
#     if (dif_anyos < 0) \
#         or (dif_anyos == 0 and dif_meses == 0 and dif_dias < 0):
#         return -2
    
#     # Calculo de la edad
#     if (mes_nacimiento > mes_actual) :
#         return dif_anyos - 1
#     elif (mes_actual == mes_nacimiento and dia_nacimiento > dia_actual):
#         return dif_anyos - 1
#     else:
#         return dif_anyos


# edat = calcula_edad("18/04/2000", "18/02/2025")
# print(edat)