#DESARROLLO DE EJERCICIOS

#Ejercicio 01
Nombre_usuario = input("Por favor, ingresar nombre de usuario: ")
print(f"¡Hola {Nombre_usuario}!")

#Ejercicio 02
Consumo = float(input("¿Cuánto es el costo total de su consumo?: $"))
Porcentaje_propina = float(input("Qué porcentaje desea dejar de propina? (>=15%): "))
Propina = Consumo * (Porcentaje_propina/100)
print(f"Lo correspondiente de propina es ${Propina}")

#Ejercicio 03
Peso_payaso = 112
Peso_muñeca = 75
Número_payasos = float(input("Por favor, ingrese número total de payasos: "))
Número_muñecas = float(input("Por favor, ingrese número total de muñecas: "))
Peso_total_payasos = (Peso_payaso * Número_payasos)/1000
Peso_total_muñecas = (Peso_muñeca * Número_muñecas)/1000
print(f"Peso total de Payasos es {Peso_total_payasos} Kilogramos")
print(f"Peso total de Muñecas es {Peso_total_muñecas} Kilogramos")

#Ejercicio 04
Número_entero = int(input("Por favor, ingrese un número entero positivo: "))
#Calcular la suma de todos los enteros desde 1 hasta N
Suma =  ((Número_entero * (Número_entero+1))/2)
print(f"La suma de los N primeros enteros positivos es {Suma}")

#Ejercicio 05
Número_shows = int(input("Por favor, ingresar cuánto shows musicales ha visto en el último año : "))
El_usuario_ha_visto_más_de_3_shows = Número_shows > 3
print(f"El usuario ha visto más de 3 shows musicales, {El_usuario_ha_visto_más_de_3_shows}")

#Ejercicio 06
Edad_del_cliente = int(input("Por favor, ingrese la edad del cliente: "))
if Edad_del_cliente < 4:
    Precio = 0
elif 4 <= Edad_del_cliente <= 18:
    Precio = 5
else:
    Precio = 10
print(f"El precio de la entrada es: ${Precio}")

#Ejercicio 07