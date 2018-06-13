a = int(input("Ingrese lado A: "))
b = int(input("Ingrese lado B: "))
c = int(input("Ingrese lado C: "))
if (a+b)>c and(a+c)>b and (c+b)>a:
    p = a + b + c
    s = p/2
    area = (s*(s-a)*(s-b)*(s-c))**.5
    if a != b != c:
        print ("El triangulo escaleno de perimetro= ",p,"y área= ",area)
    else:
        if (a == b == c):
            print("El triangulo equilatero de perimetro= ",p,"y área= ",area)
        else:
            print("El triangulo isoseles de perimetro= ",p,"y área= ",area)
    #llamar graficador
else:
   print ("No es triangulo")
