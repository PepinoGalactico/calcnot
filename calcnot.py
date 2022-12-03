from statistics import mean

print("Calculadora de notas Chile")

def vexigencia():
    while True:
        try:
            return int(input("¿Cuál es el procentaje de exigencia?: ")) / 100
        except ValueError:
            print("Debes ingresar un número entero")

def vpuntajeideal():
    while True:
        try:
            return int(input("¿Cuál es el puntaje ideal?: "))
        except ValueError:
            print("Debes ingresar un número entero")

def vpuntaje():
    while True:
        try:
            return int(input("¿Cuál es tu puntaje obtenido?: "))
        except ValueError:
            print("Debes ingresar un número entero")

def calcular():
    exigencia = vexigencia()
    puntajeideal = vpuntajeideal()
    puntaje = vpuntaje()
    if puntaje < exigencia * puntajeideal:
        nota = ((4 - 1) * (puntaje / (exigencia * puntajeideal))) + 1
    else:
        nota = ((7 - 4) * ((puntaje - exigencia * puntajeideal)/(puntajeideal * (1 - exigencia)))) + 4
    print(f"Tu nota es " "%.2f" % nota)

def promedio():
    notas = list(map(float, input("Escribe tus notas con un espacio de separacion y un punto en el decimal: ").split()))
    promedio = mean(notas)
    print(f"Tu promedio es " "%.2f" % promedio)
    

while True:
    funcion = input("Para calcular tu nota escribe calcular, para saber tu promedio de notas escribe promedio: ")
    if funcion == "calcular":
        calcular()
    elif funcion == "promedio":
        promedio()
    break
        