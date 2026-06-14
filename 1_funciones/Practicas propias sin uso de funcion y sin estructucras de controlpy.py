#Ejercicio de un programa que imprima las tablas de multiplicar de un numero ingresado del 1 al 10 sin estructuras de control 
#Y sin funciones
def clean_screen():
    print ("\033c")



num = int(input("Por favor ingresa un numero a multiplicar: "))
clean_screen
print (f"{num} x 1 = {num * 1}")
print (f"{num} x 2 = {num * 2}")
print (f"{num} x 3 = {num * 3}")
print (f"{num} x 4 = {num * 4}")
print (f"{num} x 5 = {num * 5}")
print (f"{num} x 6 = {num * 6}")
print (f"{num} x 7 = {num * 7}")
print (f"{num} x 8 = {num * 8}")
print (f"{num} x 9 = {num * 9}")
print (f"{num} x 10 = {num *10}")
