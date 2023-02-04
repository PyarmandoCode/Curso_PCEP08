"""
Comentarios en Varias
Lineas
DocString
"""

# todo Comentario en Una sola Linea

mentor = "Armando" # todo esto es una variable string
curso = "PCEP PYTHON"
edad = 43
salario = 1700

# todo concatenar variables
# print(mentor + str(edad))
# print(mentor, edad)
# print("%s tiene  %d años" % (mentor, edad))
# print(f"{mentor} tiene {edad} años")

# todo entrado de datos
# cliente = input("Ingrese el Nombre del cliente:")
# costo = float(input("Costo del producto:"))
# cantidad = int(input("cantidad del producto:"))
# total = costo * cantidad
# print(f"El total a pagar por el cliente {cliente} es {total}")
# print("El total a pagar es %.2f" % total)

#print("saltos de linea . Viene un salto \n\n")
#print("hola", "mundo", sep='<->')

#todo las palabras reservadas que tiene PYTHON y
# si las puedo usar como variables
import keyword
print(keyword.kwlist)
print(keyword.iskeyword('While'))


