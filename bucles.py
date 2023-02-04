# todo bucle for

for _ in range(10):
    print("Hola Mundo")
print("finalizo el bucle")

# for num in range(10):
#    print(num)
#
# for num in range(1, 10, 2):
#     print(num)

# for i in range(1, 10):
#     if i == 5:
#         break
#     else:
#         print("Aun no llego a la vuelta diez", i)
#         continue

# c = 0
# sum = 0
# for i in range(5):
#     valor = int(input("Ingresar un valor:"))
#     c += 1
#     sum += valor
# print("Cantidad de valores ingresados", c)
# print("Suma de esos valores", sum)

# todo bucle while
# contraseña = "admin"
# cont = 0
# while True:
#     con = input("Ingrese la contraseña:")
#     if con == contraseña:
#         print("Contraseña correcta")
#         break
#     else:
#         print("Contraseña Errada")
#         cont += 1
#         if cont == 3:
#             print("Supero los intentos , vuelva dentro de 24 horas")
#             break
#         else:
#             print(f"Ud Lleva {cont} intentos")

# import random
# numero_secreto = random.randint(1, 100)
# intentos = 0
# while True:
#     numero = int(input("Cual es el numero secreto:"))
#     intentos += 1
#     if numero == numero_secreto:
#         print(f"Acertastes!!! {numero}")
#         print(f"Numero de intentos {intentos}")
#         break
#     else:
#         if numero_secreto > numero:
#             print(f"El Numero secreto {numero_secreto} es mayor al ingresado {numero} ")
#         else:
#             print(f"El Numero secreto {numero_secreto} es menor al ingresado {numero} ")

msj = "n"
sum = 0
while True:
    producto = input("Ingrese el producto a comprar:")
    precio = float(input("Ingrese el precio del producto:"))
    cantidad = int(input("Ingrese la cantidad del producto:"))
    subtotal = precio * cantidad
    sum = sum + subtotal
    msj = input("Desea Seguir Comprando:?(s/n")
    if msj.upper() == "N":
        print(f"el total a pagar {sum}")
        break
