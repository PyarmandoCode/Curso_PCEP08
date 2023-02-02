# todo Tipo de datos primitivos
edad_per = 28
nombre_per = "Python"
precio_prod = 20.8
cantidad_prod = 100
estado_prod = True

# print(type(edad_per))
# print(type(nombre_per))
# print(type(precio_prod))
# print(type(str(cantidad_prod)))
# print(type(estado_prod))

listas_personas = ['JUAN', 200, 20.90]  # lIST
sueldos = (1990, 27768, 3545) #tuple
empleados = {'codigo':100,'nombre':"Curso PCEP"} #dic


print(type(sueldos))
print(type(listas_personas))
print(type(empleados))

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)