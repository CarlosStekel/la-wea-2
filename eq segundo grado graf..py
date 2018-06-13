from tkinter import *
def grafica(ca,cb,cc,fc):
    x0 = 400
    y0 = 400
    canvas = Canvas(width=800, height=800, bg='white')
    for x in range(-100,100):
        y=ca*x**2+cb*x+cc
        y1 = y-1
        y2 = y+1
        x1 = x-1
        x2 = x+1
        canvas.create_line(x1,y1,x2,y2)
    return
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a > 0:
    d = b**2-4*a*c
    if d == 0:
        x = -b/(2*a)
        print ("raices iguales",x)
    elif d>0:
        x1 = (-b + d**.5)/(2*a)
        x2 = (-b - d**.5)/(2*a)
        print ("x1: ", x1," x2: ",x2)
    else:
        print ("raices imaginarias")
