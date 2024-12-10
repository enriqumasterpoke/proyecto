"""
calcular el perimetro y area de un triangulo
"""
import math
#Funcion para calcular el perimetro de un triangulo
def perimetro_triangulo(lado1,lado2,lado3):
    return lado1+lado2+lado3

#funcion para calcular el area de un trangulo(formula de heron)
def area_triangulo(lado1,lado2,lado3):
    s=(lado1+lado2+lado3)/2
    return math.sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))

#funcion para determinar si es un triangulo
def es_triangulo(lado1,lado2,lado3):
    return lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1

def main():
    lado1=float(input("lado 1:"))
    lado2=float(input("lado 2:"))
    lado3=float(input("lado 3:"))
if es_triangulo(lado1,lado2,lado3):
    print(f"perimetro de un triangulo es:{perimetro_triangulo(lado1,lado2,lado3):.2f}")
    print(f"area de un triangulo es:{area_triangulo(lado1,lado2,lado3):.2f}")
else:
    print ("no es un triangulo")

if _name_== "_main_":
    main()