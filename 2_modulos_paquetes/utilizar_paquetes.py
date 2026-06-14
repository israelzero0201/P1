from paquete1 import modulos, modulo_paquete


modulos.borrarPantalla() 
nom_full = modulo_paquete.funcion4()

edad = modulo_paquete.edad() 

name_full = modulos.solicitar_nombre()  

print (f"El nombre es: {nom_full}, y tiene {edad} años")

print ("\033c") 

def calcular_area(b,a):
    area = b*a
    return area

base = float(input("Ingresa la base: "))
altura = float (input("ingresa la altura: "))

resultado = calcular_area (base,altura)

print (f"El area es {resultado}") 

