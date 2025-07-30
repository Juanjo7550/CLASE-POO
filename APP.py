

class Perro:
    def __init__(self,nombre,raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f'{self.nombre}Esta ladrando')

class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

#Vamos a instanciar objetos 

miPerrito=Perro("Mia", "Golden") 
elperrodemihermano=Perro("Spyke","Labrador")       

mihermano=Persona("Marco","12","Masculino")

print("Ingrese los datos del tercer perro ")
nombre=input("Ingrese el nombre ")
raza=input("Ingrese la raza ")
mitercerperro=Perro(nombre,raza)



print(mihermano.nombre)
print(mihermano.edad)
print(mihermano.sexo)
print(miPerrito.nombre)
print(miPerrito.raza)
print(elperrodemihermano.nombre)
print(elperrodemihermano.raza)
print("Lo datos del tercer perro son")
print(mitercerperro.nombre)
print(mitercerperro.raza)
print("Ahora los perros van a ladrar")
miPerrito.ladrar()
elperrodemihermano.ladrar()
mitercerperro.ladrar()