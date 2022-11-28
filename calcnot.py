print("Calculadora de notas Chile")

def e():
    while True:
        try:
            return int(input("¿Cuál es el procentaje de exigencia?: "))
        except ValueError:
            print("Debes ingresar un número entero")

def pmax():
    while True:
        try:
            return int(input("¿Cuál es el puntaje ideal?: "))
        except ValueError:
            print("Debes ingresar un número entero")

def p():
    while True:
        try:
            return int(input("¿Cuál es tu puntaje obtenido?: "))
        except ValueError:
            print("Debes ingresar un número entero")

e = e() / 100
pmax = pmax()
p = p()

if p < e * pmax:
    n = ((4 - 1) * (p / (e * pmax))) + 1
else:
    n = ((7 - 4) * ((p - e * pmax)/(pmax * (1 - e)))) + 4

print(f"Tu nota es {n:.2f}")