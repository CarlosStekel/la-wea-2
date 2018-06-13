#Dado 2 numeros y una operacion matematica basica entregar resultado
print("1 = Suma")
print("2 = Resta")
print("3 = Multiplicación")
print("4 = División")
o = int(input("Especificar operacion: " ))

if o > 4 :
        print("Operacion no disponible")
        
a = int(input("Dar primer numero: "))
b = int(input("Dar segundo numero: "))

if o == 1 :
    print("La suma es :", a + b)   
if o == 2 :
    print("La resta es :", a - b)
if o == 3:
    print("La multiplicacion es :", a*b)
if o == 4 :
    if b == 0:
        print("el denominador no puede ser 0")
    else:
        print("La division es :", a / b)
