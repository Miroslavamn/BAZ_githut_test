names = ['Hugo', 'Paco', 'Luis']
absence = []

for name in names:
    #print (name)
    if name == 'Paco':
        print("El alumnao si se encuentra en clase")
        print(name + " si se encuentra en clase")
    else:
        absence.append(name)

print ("\n")
print ("Esta es la lista de alumnos ausentes")
print (absence)


#Ciclo while
i=1
while i<4:
    print(1)
    if i==4:
        break
    i += i

names = ['Hugo', 'Paco', 'Luis']
if 'Gonzalo' not in names:
    print ("Gonzalo no esta en la lista")


#Comentar el resto del código para tener la salida correcta
for name in names:
    if name != 'Paco':
        absence.append(name)
    else:
        print(name + " si se encuentra en clase")
print (absence)


#Condiciones
age = 23 

if age <4:
    ticket_price = 0
elif age <18:
    ticket_price = 10
else:
    ticket_price = 15
print(ticket_price)

#Funciones
def evaluacion_edad(age):

    if age <4:
        ticket_price = 0
    elif age <18:
        ticket_price = 10
    else:
        ticket_price = 16
    print(ticket_price)

age = int(input("Ingresa tu edad: "))
evaluacion_edad(age)
