#Asincrona semana 09

#Desarrollar un programa que solicite los siguientes datos a un usuario nombre, apellido, edad y sexo y mostrarlos al final.

print("--------------------------------------------------")
print("== Bienvenido Ing. a nuestro programa ==")
print("--------------------------------------------------\n")

# indicar el inicio del programa
print("Inicio del programa.\n")
print("Ingrese sus datos para conocer en qué etapa está de su vida.")

#Peticion de datos
Nombre = input("\nEscriba su nombre: ")

Apellido = input("\nEscriba su apellido: ")

Edad = int(input("\nEscribe tu edad: "))

Sexo = input('''\n\tElija su sexo
             1- femenino
             2- masculino
             Escriba su sexo: ''').lower()

#Realizar la estucutura con el if poniendo las posibilidades antes dadas por el Ing. en el caso que el usuario sea femenino       

if Sexo =="femenino" or Sexo == "1" or Sexo == "mujer" or Sexo == "f":
      
         if Edad >= 0 and Edad <=2 :
               print(Nombre, Apellido, "Usted es una niña y está en la etapa de Bebé.")

         elif Edad >=3 and Edad <= 5:
               print(Nombre, Apellido, "Usted es una niña y está en la etapa de la Infancia.")

         elif Edad >=6 and Edad <= 11:
               print(Nombre, Apellido, "Usted es una niña y está en la etapa de la Niñez.")

         elif Edad >=12 and Edad <= 18:
               print(Nombre, Apellido, "Usted es una niña y está en la etapa de la Adolescencia.")

         elif Edad >=19 and Edad <= 26:
               print(Nombre, Apellido, "Usted es una señorita y está en la etapa de la Juventud.")

         elif Edad >=27 and Edad <= 40:
               print(Nombre, Apellido, "Usted es una señora y está en la etapa de la Adultez Joven")

         elif Edad >=41 and Edad <= 55:
               print(Nombre, Apellido, "Usted es una señora y estapa en la etapa de la Adultez.")

         elif Edad >=56 and Edad <= 65:
               print(Nombre, Apellido, "Usted es una Anciana y es una Persona mayor.")

         elif Edad >=66 or Edad <=100 :
               print(Nombre, Apellido, "Usted es una Anciana y está en la etapa de la Vejez.")

         else:
               print(Nombre, Apellido, "su edad no se encuentra en el registro")
               
#Realizar la estucutura con el if poniendo las posibilidades antes dadas por el Ing. en el caso que el usuario sea Masculino       
               
elif Sexo =="masculino" or Sexo == "2" or Sexo == "hombre" or Sexo == "m":

         if Edad >= 0 and Edad <=2 :
               print(Nombre, Apellido, "Usted es un niño y está en la etapa de Bebé.")

         elif Edad >=3 and Edad <= 5:
               print(Nombre, Apellido, "Usted es un niño y está en la etapa de la Infancia.")

         elif Edad >=6 and Edad <= 11:
               print(Nombre, Apellido, "Usted es un niño y está en la etapa de la niñez.")

         elif Edad >=12 and Edad <= 18:
               print(Nombre, Apellido, "Usted es un niño y está en la etapa de la Adolescencia.")

         elif Edad >=19 and Edad <= 26:
               print(Nombre, Apellido, "Usted es un caballero y está en la etapa de la Juventud.")

         elif Edad >=27 and Edad <= 40:
               print(Nombre, Apellido, "Usted es un señor y está en la etapa de la Adultez Joven")

         elif Edad >=41 and Edad <= 55:
               print(Nombre, Apellido, "Usted es un señor  y estpa en la etapa de la Adultez.")

         elif Edad >=56 and Edad <= 65:
               print(Nombre, Apellido, "Usted es un Anciano y es una Persona mayor.")

         elif Edad >=66 or Edad <=100 :
               print(Nombre, Apellido, "Usted es un Anciano y está en la etapa de la Vejez.")

         else:
               print(Nombre, Apellido, "su edad no se encuentra en el registro")


#En el caso de que el genero escrito no se encuentre en la base de datos previamente indicada, poner un mensaje indicandolo.  
         
else:
         print("Su Genero no se encuentra 'Disponible'. ")

#Por ultimo definir un sistema que interprete si la edad es par o impar-


if Edad % 2 == 0:
    print("\nLa edad de", Nombre, "es par.")
else:
    print("\nLa edad de", Nombre, "es impar.")

#indicar la finalizacion del programa en un print().

print("\nFin del programa")