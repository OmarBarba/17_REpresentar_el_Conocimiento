class Marco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.atributos = {}

    def agregar_atributo(self, nombre, valor):
        self.atributos[nombre] = valor

evento = Marco("Evento")
evento.agregar_atributo("nombre", "Cumpleaños")
evento.agregar_atributo("fecha", "15 de octubre")
