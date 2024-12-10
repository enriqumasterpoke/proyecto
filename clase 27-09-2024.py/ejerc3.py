"""_summary_
Crear un algoritmo que pida dos numeros y me de la suma,la resta,la multiplicacion y la division segun la opcion elegida
"""

a=int(input("ingrese un numero:"))
b=int(input("ingrese un numero:"))

print("elija que operacion desea hacer:")
print("1-suma,2-resta,3-producto,4-cociente")
op=int(input("opcion:"))
res=0
if op==1:
    res=a+b
    print(f"la suma de {a}+{b}={res}")
elif op==2:
    res=a-b
    print(f"la resta de {a}-{b}={res}")
elif op==3:
    res=a*b
    print(f"el producto de {a}*{b}={res}")
elif op==4:
    if b==0:
        print("no se puede divir por cero..!!")
    else:
        res=a/b
        print(f"el cociente de {a}/{b}={res}")
else:
    print(f"la operacion{op}no es valida")