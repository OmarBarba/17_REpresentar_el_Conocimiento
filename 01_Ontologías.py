from owlready2 import *

onto = get_ontology("http://www.example.org/ontology.owl")

class Persona(Thing):
    namespace = onto

class TieneEdad(Persona >> int, FunctionalProperty):
    namespace = onto

with onto:
    juan = Persona()
    juan.TieneEdad = 30

onto.save()
