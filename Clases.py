#Clases
class car:
    def __init__(self, modelo, marca, anio) -> None:
        self.modelo = modelo
        self.marca = marca
        self.anio =anio
    
    def encender_motor(self):
        print("Este motor esta encendido")
    
    def apagar_motor(self):
        print("Este motor esta apagado")    

class Electric(car):
    def cargando_bateria(self):
        print ("Este auto esta cargando bateria")

class hibrido(car):
    def motor_hibrido(self):
        print ("Este motor funciona con gasolina y bateria")

#Atributos
print("Los atributos de la clase carro son:")
carro_01 = Electric('Prius', 'Toyota', 2023)
print (carro_01.modelo)
print (carro_01.marca)
print (carro_01.anio)

#Metodos
carro_01.encender_motor()
carro_01.apagar_motor()
carro_01.cargando_bateria()


print ("\n Este carro es hibrido")
carro_02 = hibrido('Prius', 'Toyota', 2023)
print (carro_02.modelo)
print (carro_02.marca)
print (carro_02.anio)

carro_02.encender_motor()
carro_02.apagar_motor()
carro_02.motor_hibrido()