class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Mamifero(Animal):
    def dar_a_luz(self):
        print(f"{self.nombre} da a luz a crías.")

class Ave(Animal):
    def poner_huevos(self):
        print(f"{self.nombre} pone huevos.")

perro = Mamifero("Perro")
perro.dar_a_luz()

canario = Ave("Canario")
canario.poner_huevos()
