# todo condicionale simples
edad = int(input("Ingrese la edad de la persona:"))
if edad > 18:
    print("La Persona es mayor de edad")
else:
    print("La Persona es menor de edad")

# todo condicionales multiples
# candidato = input("candidato a elegir:")
# if candidato.upper() == "A" or candidato.upper() == "D" or candidato.upper() == "D":
#     print("Usted voto por el partido Rojo")
# elif candidato.upper() == "B":
#     print("Usted voto por el partido Azul")
# elif candidato.upper() == "C":
#     print("Usted voto por el partido Verde")
# else:
#     print("Opcion Errada")

# todo
cant_preguntas = int(input("Ingrese la cantidad de preguntas:"))
cant_correctas = int(input("Ingrese la cantidad de preguntas respondidas correctamente:"))
porcentaje = cant_correctas * 100 / cant_preguntas
if porcentaje < 50:
    print("Debe realizar el examente nuevamente")
else:
    if porcentaje < 75:
        print("Nivel Regular Obtuvo su Certificado")
    else:
        if porcentaje < 90:
            print("Nivel Medio Obtuvo su Certificado")
        else:
            print("Nivel Maximo Felicitaciones respondio casi todas la preguntas!!")
