

def elevado (num,exponente):
    potencia = num ** exponente
    return potencia




num1= float (input("Por favor ingrese el numero: "))

expo = int (input("Por favor ingrese el numero: "))

resultado = elevado(num1, expo)

print(f"El numero elevado es: {resultado}")  
def clean_screen ():
    print ("\033c")

def mostrarNombres (name,lastname): 
    nom = name .upper() .strip()
    ape = lastname .upper() .strip() 
    

    return nom,  ape



nombre = input ("Nombre: ")
 
apellidos = input ("Apellidos: ")

nombre_completo = mostrarNombres (nombre,apellidos)

print (f"{nombre_completo}") 

def tablas (num1,num2,):
    
    resultado = num1 * num2
    
    print (f"{num1} x {num2} = {resultado}") 
            #3    por  1     igual a 3 
    num2 += 1
    
    #Aqui num2 ya vale 2 porque es num2 es igual a 1 mas 1
    #Nos regresa el valor de num2 que ahora es 2 
    return num2 

numero = int (input("numero a multiplicar"))

n2 = 1


num2 = tablas (numero,n2) 
num2 = tablas (numero,num2) 
num2 = tablas (numero,num2) 
num2 = tablas (numero,num2) 
num2 = tablas (numero,num2) 
num2 = tablas (numero,num2) 
num2 = tablas (numero,num2) 
num2 = tablas (numero,num2) 
num2 = tablas (numero,num2) 
num2 = tablas (numero,num2) 


print (f"------{num2}-----") 











   