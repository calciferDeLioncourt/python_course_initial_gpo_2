# Comentario en linea

'''
Comentario de bloque
Comentario multilínea
'''

# Tipos de dato

mi_variable = 10               # Entero integer
mi_variable_flotante = 10.5   # Flotante float
mi_variable_cadena = "Hola"    # Cadena de texto string
mi_variable_booleana = True    # Booleano



#print("Hola, mundo!")  # Imprimir en consola
print(type(mi_variable))

mi_lista = [1, 2, 3, 4, 5]  # Lista
print("Mi lista antes de modificar:", mi_lista)
mi_lista[2] = 40  # Modificar un elemento de la lista
print("Mi lista después de modificar:", mi_lista)


mi_tupla = (1, 2, 3, 4, 5)  # Tupla a dif de lista no se modifica
print("Mi tupla:", mi_tupla)

mi_diccionario = {"clave1": "valor1", "clave2": "valor2"}  # Diccionario

mi_set = {1, 2, 3, 4, 5}  # Sets

nombre: str = "Alberto"

print("Hola, " + nombre)  # Concatenación de cadenas
print(f"Hola, {nombre}")  # f-string para formateo de cadenas

# Operadores y expresiones
suma = 5 + 3
resta = 10 - 2
multiplicacion = 4 * 2
division = 8 / 2
modulo = 10 % 3
potencia = 2 ** 3
division_entera = 7 // 2

#Control de flujo
if mi_variable > 5:
    print("La variable es mayor que 5")
elif mi_variable == 5:
    print("La variable es igual a 5")
else:
    print("La variable es menor que 5")

#operador ternario
resultado = "Mayor que 5" if mi_variable > 5 else "No es mayor que 5"
print(resultado)

# Bucles
# for i in range(5):
#     print(f"Iteración {i}")

# for elemento in 'mi_lista':
#     print(f"Elemento: {elemento}")

'''
    Compresiones
'''
cuadrados: list = [x**2 for x in range(10)]
print(cuadrados)

#break y continue y else en bucles
for i in range(10):
    if i == 5:
        print("Se encontró el 5, saliendo del bucle.")
        break
    if i % 2 == 0:
        continue
    print(f"Número impar: {i}")