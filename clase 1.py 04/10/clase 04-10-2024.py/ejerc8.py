"""_summary_
operaciones con cadenas
introduzca una cadena y muestre en minusculas y mayusculas
divide en cadena en una lista
"""

cadena=input("cadena:")#ingresar cadena

mayus=cadena.upper()#poner en mayuscula
minus=cadena.lower()#poner en minuscula
cap=cadena.capitalize()#capitalizar

print(mayus)#imprimir
print(minus)#imprimir
print(cap)#imprimir

lista=cadena.split("o")#dividir la cadena en una lista divida por "o"

print(lista)#imprimir lista