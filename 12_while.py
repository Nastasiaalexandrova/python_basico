"""

Whhle (mientras)"""


##########11111111111111111111111111111111111
# num = 5
# while num > 0:
#     print(num)
#     num -= 1
# else:
#     print("Has entrado en el else")

#####################2222222222222222222222222222

print("#" * 20)
num = 5
while True:
    print(num)
    num -= 1
    if num == 0:
        break
else:
    print("Has entrado en el else")

monedas = 10
while True:
    prestamo = input("Cuantas monedas necesitas?")
    if int(prestamo) >= int(monedas) or int(prestamo) <= 0:
        print("Elige el numero mas que 0 a 10")
    else:
        print("Mañana te doy")
        break

    