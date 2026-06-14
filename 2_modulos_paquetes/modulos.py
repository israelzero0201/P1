# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).

#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():

     nombre=input ("Nombre: ").strip().upper()
     apellidos=input ("Apellido: ").strip().upper() 
     print (f"El nombre del alumno es;  {nombre} {apellidos}") 

   
def borrarPantalla ():
   print (f"\033c")   
   



  
#3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nombre,apellidos):

    print (f"El nombre del alumno es;  {nombre} {apellidos}") 
 

 #2.- Funcion que no recibe parametros y regresa valor

def funcion2():
    nombre=input("escribe el nombre").strip().upper()
    apellido=input("escribe los apellidos").strip().upper()

    return nombre,apellido
#nom,ape=funcion2()

print(f"El nombre completo del alumno es: {nom} {ape}")


 #4.- Funcion que recibe parametros y regresa valor

def funcion4(nom, ape):
    nombre = nom.strip().upper()
    apellido = ape.strip().upper() 

    return nombre,apellido 


#Invocar las funciones

funcion1()

nombre=input ("Nombre: ").strip().upper()
apellidos=input("Apellidos: ").strip().upper()
#funcion3(nombre, apellidos)

nombre,apellidos=funcion2()
print(f"El nombre del alumno es: ")

nombre=input("Nombre: ").strip().upper()
apellidos=input("Apellidos: ").strip().upper()
nom,ape=funcion4(nombre,apellidos)
print(f"El nombre del alumno es: {nom} {ape}")




