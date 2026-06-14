'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

'''

tabla = int(input("ingrese un numero por favor: "))

print(tabla, "x 1 =", tabla * 1)
print(tabla, "x 2 =", tabla * 2)
print(tabla, "x 3 =", tabla * 3)
print(tabla, "x 4 =", tabla * 4)
print(tabla, "x 5 =", tabla * 5)
print(tabla, "x 6 =", tabla * 6)
print(tabla, "x 7 =", tabla * 7)
print(tabla, "x 8 =", tabla * 8)
print(tabla, "x 9 =", tabla * 9)
print(tabla, "x 10 =", tabla * 10) 


'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control solo while 
  2.- Sin funciones

'''


num=int (input("Por favor ingrese un numero: "))

for i in range (1,10 + 1):
    
   resultado = num * i 
   
   print (f"{num} x {i} = {resultado}" )



numero = int(input("Ingresa el numero de la tabla: "))

i = 1

while i <= 10:
    print(numero, "x", i, "=", numero * i)
    i += 1 

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control 
  2.- Con funciones

'''

def tabla(num_tab,n): 
    mul=num_tab*n
    print(f"{num_tab} x {n} = {mul}")
    n+=1
    return n 

num_tabla=int(input("Numero de la tabla de multiplicar: "))
num=1

n=tabla(num_tabla,num)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n)
n=tabla(num_tabla,n) 
n=tabla(num_tabla,n)

'''
  Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Con estructuras de control 
  2.- Con funciones

'''

def tabla(num_tabla,n):
    multi=num_tabla*n
    print(f"{num_tabla}  x {n}  = {multi} ")
    n+=1
    return n


num_tabla=int(input("Numero de tabla de multiplicar"))

num=1 

for i in range(10,0,-1):
    n=tabla(num_tabla,n)
    





