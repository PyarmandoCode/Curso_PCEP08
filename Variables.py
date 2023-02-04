# todo Tipo de datos primitivos
edad_per = 28 # int
nombre_per = "Python" #str
precio_prod = 20.8 # float
cantidad_prod = 100 # int
estado_prod = True # bool
#todo camel case
CodigoProducto="100"
#todo snake case
codigo_producto="100"

# print(type(edad_per))
# print(type(nombre_per))
# print(type(precio_prod))
# print(type(str(cantidad_prod)))
# print(type(estado_prod))

#todo colleciones
listas_personas = ['JUAN', 200, 20.90]  # lIST
sueldos = (1990, 27768, 3545) #tuple
empleados = {'codigo':100,'nombre':"Curso PCEP"} #dic


print(type(sueldos))
print(type(listas_personas))
print(type(empleados))

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)