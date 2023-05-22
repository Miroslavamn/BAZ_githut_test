def obtener_nombre():
    #print ("Hola Baz")
    return "Hola baz"

mensaje = obtener_nombre()
print (mensaje)

def obtener_nombre(name):
    return "Hola Baz.Bienvenida " + name
name = 'Miroslava'
print(obtener_nombre(name))
print(obtener_nombre('Miroslava'))
