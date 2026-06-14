"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""


#Funciones más comunes en las listas
paises =["Mexico", "Canada", "EUA","Mexico","Brasil"]
numeros = [23,45,8,24]
varios = [33,3,1416,"Hola",True]
vacio= []


print ("\033c")
# #Imprimir el contenido de una lista

print(paises)
print(numeros)
print(varios)
print(vacio)
print(paises[0]+""+paises[3])


# #Recorrer la lista 
# #1er forma 
for i in paises:
    print (paises)


# # #2do forma 
paises =["Mexico", "Canada", "EUA","Mexica","Brasil"]
tamanio=len(paises) #Funcion "len" determina el tamaño de la lista 
for i in range (0,tamanio):
    print(paises[i]) 


print (paises)
#ordenar elementos de una lista
paises.sort()
print (paises)

#dar la vuelta a una lista
paises.reverse()
print(paises)



paises =["Mexico", "Canada", "EUA","Mexica","Brasil"]
print(paises)
#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
paises.append("Honuduras") 
print(paises)


#2da forma
paises.insert(1,"Argentina")
print(paises)
paises.insert(100,"Panama") 
print(paises)
paises.append(23)
paises.append(3)
print(paises)
paises.sort() #Solo cuando el tipo de datos sea igual.
print(paises)

#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop (4)
print (paises) 
len

# #2da forma 
paises.remove ("EUA")
print (paises)

# #Buscar un elemento dentro de la lista

buscar ="Brasil" in paises 
if buscar == True:
    print("Soy True")
else:
    print ("Soy False")    
print (buscar)


#Contar el numeros de veces que aparece un elemento dentro de una lista
numeros = [23,45,24,8,23,50,23]
x = int(input("dame un numero: "))
cuantas = numeros.count (x)
print (f"El numero {x} aparece: {cuantas} veces") 




# Conocer la posicion o indice en el que se encuentra un elemento de la lista
posicion = numeros.index(50)
print (f"Estoy en la posicion {posicion}")

#Unir el contenido de una lista dentro de otra lista
numeros1 = [23,45,24,8,23,50,23]
print (numeros1)
numeros2=[100,-100]
print(numeros2)
numeros1.extend(numeros2)
print (numeros1) 


#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente
numeros1.sort()
numeros1.reverse ()
print(numeros1)
resultante=numeros1+numeros2
resultante.sort(reverse=True)
print(resultante)



