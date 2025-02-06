"""
Pupil has:


"""

alumnos = ["Pepe", "Garcia", 27, "calle xxx", ["Python", "JS"], 
           "Maria"]

alumnos = [["Pepe", "Garcia", 22, "calle xxx", ["Python", "JS"]],
           ["Maria", "UIO", 27, "calle xxx", ["Python", "JS"]]
           ]

# for a, b, c, d, e in alumnos:
#     print(a)    # ----------- Pepe   /// Maria

for nombre, apellido, edad, direccion, asignaturas in alumnos:
    print(f"{nombre}")

for nombre, apellido, edad, direccion, asignaturas in alumnos:
    print(f"El alumno {nombre} tiene {edad} años")

dic_alumno_1 = {"nombre": "Pepe", "edad": 22}
dic_alumno_2 = {"nombre": "Maria", "edad": 27}

mis_alumnos = [dic_alumno_1, dic_alumno_2]

print(dic_alumno_1["nombre"]) #Pepe

print(type(dic_alumno_1["nombre"])) #<class 'str'>

print(mis_alumnos[0]["nombre"])   #Pepe

dic_alumno_2["nombre"] = "Anna"
dic_alumno_3 = {"nombre": "Pol", "beca": True}

dic_alumno_1.update(dic_alumno_3)


print(dic_alumno_2) #{'nombre': 'Anna', 'edad': 27}
print(dic_alumno_3) #{'nombre': 'Pol', 'beca': True}

for props in dic_alumno_1:
    print(props) ##nombre  edad   beca


print(dic_alumno_1.keys())   #dict_keys(['nombre', 'edad', 'beca'])
print(dic_alumno_1.values())   ##dict_values(['Pol', 22, True])