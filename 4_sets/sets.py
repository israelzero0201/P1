"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

print("\033c")

set1={"Python","SQL","Estructurado","SQL"}
print(set1)

for i in set1:
  print(i)

  
set2={"Hola",True,33,3.1416}
print(set2)

set2_respaldo=set2.copy()
set2.clear()
print(set2)
print(set2_respaldo)

set3={""}
print(set3)

set3.add("Hola")
set3.add(3)
set3.add(10.0)
set3.add("3")
print(set3)
set3.add(3)
print(set3)

set3.pop()
set3.pop()
print(set3)
set3.clear()
print(set3)
set3.add("33")
print(set3)

lista=[10,9.5,8.5,3.4,8.5,10]
print(lista)
conjunto=set(lista)
lista=list(conjunto)
print(lista)


#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar 
#en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1

email = input("Por favor ingresa el email")

set1 = {""} 
set1.add (email) 


lista_correos = []

print("- Registro de Alumnos UTD -")
print("Introduce los correos electrónicos. Escribe 's' para terminar.\n")


while True:
    email = input("Introduce el email del alumno: ").strip().lower()
    
  
    if email == 's':
      break
    
   
    if email != "":
      lista_correos.append(email)

correos_unicos = set(lista_correos) 


print(f"Total de correos capturados: {len(lista_correos)}")
print(f"Total de correos sin duplicados: {len(correos_unicos)}")

print("\nLista de correos únicos a procesar:")
for correo in correos_unicos:
    print(f"- {correo}")

list_emails=[]

opc="S"
while opc=="S":
   list_emails.append(input("Ingresa el email: ").lower().strip())
   opc = input ("Deseas ingresar otro email? (S/N) ").upper().strip()

set_emails=set(list_emails)
list_emails=list(set_emails)
print(list_emails)

 


#Solucion 2 #quiero que en lugar de que los elemntos se agreguen al principio de la lista y 
#y que trabaje con una variable logica




lista_correos = []
continuar_captura = True

print("- Registro de Alumnos UTD -")
print("Introduce los correos electrónicos. Escribe 'salir' para terminar.\n")


while continuar_captura: 
    email = input("Introduce el email del alumno: ").strip().lower()
    
   
    if email == 's':
        continuar_captura = False
    else:
        
        if email != "":
            lista_correos.insert(0,email) 



correos_unicos = set(lista_correos)



print(f"Total de correos capturados: {len(lista_correos)}")
print(f"Total de correos sin duplicados: {len(correos_unicos)}")


print("\nLista de correos únicos (sin duplicados):")
for correo in correos_unicos:
    print(f"- {correo}")
  



