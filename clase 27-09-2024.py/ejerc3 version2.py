"""_summary_
Crear un arlgoritmo que pida dos numeros y me de la suma,la resta,la multiplicacion y la division segun la opcion elegida
"""

a=int(input("ingrese un numero:"))
b=int(input("ingresa un numero:"))

print("Elija que operacion desea hacer:")
print("1-suma,2-resta,3-producto,4-cociente")
op=int(input("opcion:"))

match op:
    case 1:
        print(f"la suma de {a}+{b}")
    case 2:
        print(f"la resta de {a}-{b}")
    case 3:
        print(f"el producto de {a}*{b}")
    case 4:
        if b==0:print("no se puede dividir por cero..!!")
        else:
            print(f"el cociente de {a}/{b}={a/b}")
    case _:
        print("las operacio  no es valida")

#ejemplo de match
"""def consulta():
   return(1,4180000,"Ana","Lezcano",234,236)
w=consulta
match w:
    case(1,4180000,"Ana","Lezcano",234,236):
        print("encontrado")
    case _:
        print("valore no encontardo")"""    