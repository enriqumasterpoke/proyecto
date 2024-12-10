"""_summary_
colecciones de python
"""
#lista
lista=[1,2,3,4,5,6,7,8,9,10]
#metodos de lista
print("append",lista.append(10))#agrega un elemento
print(lista)
print("count",lista.count(10))#cuenta el elemento
print("tamaño",len(lista))#tamaño
print("insert",lista.insert(0,0))#inserta un elemento
print(lista)
print("remove",lista.remove(10))#elimina un elemento
print(lista)
print("pop",lista.pop())#elimina el ultimo elemento
print("lista")
print("sort",lista.sort())#organiza de menor a mayor
print("lista")
print("reverse",lista.reverse())
print("lista")#organiza de mayor a menor

#listas anidadas
listas_anidadas=[[1,2,3],[4,5,6],[7,8,9]]
print(listas_anidadas)

for f in listas_anidadas:
    print(f)


    #tuplas
    tupla=(1,2,3,4,5,6,7,8,9,10)
    t1=tuple("Hola,Mundo!")
    print(t1)

    #diccionarios
    diccionario={
        "ci":1,
        "nombre":"Juan",
        "edad":30,
        "estado civil":"S"
    }  
    print(diccionario)

    #Set
    set0={1,2,3,4,5,6,7,8,9,10}
    print(set0)  