print ("Ax2+Bx+C")
a = float(input("ingrese A: "))
b = float(input("ingrese B: "))
c = float(input("ingrese C: "))
if a == 0:
    print("Por favor ingrese una equación cuadratica")
else:
    d = (b**2 - 4*a*c)
    if d < 0:
        print("Las raices no son reales")
    if d == 0 :
        print("Las raices son iguales: ", -b/(2*a))
    else:
        x1= (-b+(d**.5))/(2*a)
        x2= (-b-(d**.5))/(2*a)
        print ("Las raices son",x1," y ",x2)
