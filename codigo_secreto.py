'''Este codigo se contempla el juego de "Codigo secreto"
que mediante un codigo de 4 digitos de la maquina sean aleatorios
y sin repetir un digito; el jugador tendra que proponer
un codigo para decifrarlo'''

import random
#LISTA DE NÚMEROS
X = ('0','1','2','3','4','5','6','7','8','9')

A = ''
for i in range(4):
    Y = random.choice(X)
    while Y in A:
        Y = random.choice(X)
    A = A + Y #NOTA AQUI NINGUN NUMERO SE REPITE

#BIENVENIDA Y BUCLES
print('''Hola jugador/a bienvenido a Codigo Secreto! 
Nuestro objetivo es descubir el codigo de la maquina
para ello necesitamos 4 digitos. Debes considerar que cuando hay un
* Es que hay un digito en el codigo secreto y está en la misma posición
- Es que hay un digito en el codigo secreto pero en una diferente posición''')

C = input("¿Cuales son tus 4 digitos?")
Intentos =1
valores =""
while C != A: # COMPARACION CUANDO SEA DIFERENTE ENTRE USUARIO Y MAQUINA
    Intentos = Intentos + 1
    aciertos = 0
    coincidencias = 0

    for i in range(4):
        if C[i] == A[i]:
            aciertos = aciertos + 1
            valores +="*"
        elif C[i] in A:
            coincidencias = coincidencias + 1
            valores +="-"
        else:
            valores += " "
    c_valores= "[" + valores + "]"
    print("Tus digitos", C, c_valores," ~~~~~ tienes", aciertos, "*", "Y ", coincidencias, "-")
    valores =""
    #Siguiente intento
    seleccion = input("Intentemos otros 4: ")
print("Felicidades!!! el codigo es", A, "lo lograste en", Intentos,"intentos")