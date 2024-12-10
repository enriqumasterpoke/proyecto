import math

from ejerc1 import es_triangulo

from ejerc1 import perimetro_triangulo

from ejerc1 import area_triangulo

from ejerc2 import perimetro_cuadrado

from ejerc2 import area_cuadrado

import ejerc3

import ejerc4

#menu principal
def main():
    print("calculo de perimetros y areas de poligonos")
    print("1 trisngulo")
    print("2.cuadrado")
    print("3.rectangulo")
    print("4.circulo")
    print("5.salir")
    
    while True:
        opcion=int(input("\nselecciona una opcion:"))
        if opcion==1:
            lado1=float(input("ingrese el lado de 1:"))
            lado2=float(input("ingrese el lado de 2:"))
            lado3=float(input("ingrese el lado de 3:"))
            if es_triangulo(lado1,lado2,lado3):
                print(f"perimetro del triangulo:{perimetro_triangulo(lado1,lado2,lado3):.2f}")
                print(f"area del triangulo:{area_triangulo(lado1,lado2,lado3):.2f}")
            else:
                print("no es un triangulo")
        elif opcion==2:
            lado=float(input("ingrese el aldo de cuadrado:"))
            print(f)
                   
                