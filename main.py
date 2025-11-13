#Calculadora
Numero1 = int (input ("ingresa el primer numero: "))
Numero2 = int (input ("ingresa el segundo numero: ")) 
Operacion = input("Que quieres hacer? Escribe la palabra (sumar, restar, multiplicar, dividir: )")
Resultado = float

#Operaciones
if Operacion == "sumar":
    print(Numero1 + Numero2)

if Operacion == "restar":
    print(Numero1 - Numero2)

if Operacion == "multiplicar":
    print(Numero1 * Numero2)

if Operacion == "dividir":
    print(Numero1 / Numero2)
