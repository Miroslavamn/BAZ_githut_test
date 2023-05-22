#Números
edad = 31;
nombre = 'Miroslava'
apellido = 'Miranda'
print(nombre, apellido, edad)

#Operaciones básicas
x = 10
y = 20
print ('Estas son operaciones aritmeticas')
print (x+y)
print (x-y)
print (x*y)
print (x/y)
print (x//y)

#Operador de módulo
print('\n')
print ('Esto es la utilización del operador módulo' )
print (x%y)

#Estructura de datos
nuevos_nombres = []
nombres_estudiantes = []
nombres_baz = ['Ricardo', 'Lore', 'Lety', 'Robert', 'Bety', 'Nacho', 'Mish', 'Miros']
print (nombres_baz)

#indices
print (nombres_baz[2])

#siles
print (nombres_baz[0:6:2])

# Añadir valores a una lista
nuevos_nombres.append('Carlos')
print (nuevos_nombres)

#Tuplas
nombres_estudiantes = ['Dave', 'Yoss']
nombres_estudiantes.append('Jesus')
print (nombres_estudiantes)
#print (nombres_estudiantes[1])

#Diccionarios
carros = {
    'carro01': {'marca': 'Toyota', 'Modelo': 2018, 'motor': 'eléctrico'},
    'carro02': {'marca': 'Nissan', 'Modelo': 2020, 'motor': 'gasolina'},
    'carro03': {'marca': 'BMW', 'Modelo': 2023, 'motor': 'hibrido'},
}

print (carros)
print (carros['carro03']['motor'])
print (carros['carro02']['marca'])
print (carros['carro02']['Modelo'])

#Metodo de los duccionarios
print ("Metos de los diccionarios")
print (carros.keys())
print (carros.values())
print (carros.items())

