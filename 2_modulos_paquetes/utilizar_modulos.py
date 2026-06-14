# # 1er utilizar los modulos 
import modulos


modulos.borrarPantalla()
modulos.funcion1()
modulos.borrarPantalla()

nom = "Daniel"
ape = "Carreon"

modulos.funcion3(nom,ape)

modulos.funcion3(nom,ape)

nom = "perro"
ape = "gatos"

nombre,apellidos=modulos.funcion4 (nom,ape)
print (f"Nombre: {nombre} \n"
       "Apelldios {apellidos}")





#2da formar de utilizar modulos
 
from modulos import borrarPantalla,funcion4

borrarPantalla()
nom="Daniel"
ape="Carreon"

nombre,apellidos = funcion4 (nom,ape)
print(f"Nombre : {nombre}\nApellidos: {apellidos}") 


