from pyswip import Prolog

prolog = Prolog()

# Definir reglas
prolog.assertz("padre(juan, maria)")
prolog.assertz("madre(maria, luis)")
prolog.assertz("abuelo(X, Y) :- padre(X, Z), madre(Z, Y)")

# Consultar reglas
for solucion in prolog.query("abuelo(X, Y)"):
    print(f"{solucion['X']} es abuelo de {solucion['Y']}")
