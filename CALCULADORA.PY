        
# Comenzamos a pedir los datos personales como el nombre
nombre = input("Introduce tu nombre: ")
apellidop = input("Tu apellido paterno: ")
apellidom = input ("Tu apellido materno: ")

# Ponemos title en nombre para dar un formato mas profesional poniendo los nombres con mayuscula en dado caso de que el usuario no lo haga
print("Hola, " + nombre.title()+" " + apellidop + " " + apellidom+ ".")

# Mensaje de bienvenida
print ("Si deseas saber tu IMC, introduce los siguientes datos:")

#Usamos un while true para estatura y peso que no permita numeros negativos para poder hacer el calculo del IMC correcto
while True:
  try:
    estatura = float(input("Tu estatura en m: "))
    if estatura < 0:
      print("No puede ingresar numeros negativos")
    else:
      break
  except ValueError:
    print ("Error debe ingresar un numero pisitivo")

while True:
  try:
    peso= float(input("Tu peso en kg: "))
    if peso<0:
      print("No pude ingresar numeros negativos")
    else:
      break
  except ValueError:
    print("Error, debe ingresar un numero")  

# Ponemos la formula para sacar IMC
imc = peso / estatura**2

# Agregamos funcion round para que el resultado de imc sea con dos decimales despues del punto
a = round( imc,2)

# Pongo los datos datos del usuario incluyendo el resultado del IMC
# ponemos kg para dar mas formato al resultado
print("Peso: " + str(peso)+" kg") 

# ponemos m para dar mas formato al resultado
print("Estatura: " +str(estatura)+" m") 

# Resultado del IMC
print("IMC: "+ str(a))
# Validaciones para saber la condicion en la que se encuentra la persona segun la fuente del ISSSTE
if imc >= 0 and imc <= 18.9:

# Cumpliendo la condicion anterior salen los siguientes mensajes
  print ("-Peso bajo-")
  print ("¡Recuerda tu salud es primero!")
  print("¡Cuidate!")
elif imc >= 18.5 and imc <= 24.99:

# Cumpliendo la condicion anterior salen los siguientes mensajes
  print ("-Peso normal-")
  print ("¡Muy bien!")
  print ("¡Sigue cuidandote!")
elif imc >= 25.0 and imc <= 29.99:

# Cumpliendo la condicion anterior salen los siguientes mensajes
  print ("-Sobrepeso-")
  print ("¡Recuerda tu salud es primero!")
  print("¡Cuidate!")
elif imc >=30.0 and imc <= 34.99:

# Cumpliendo la condicion anterior salen los siguientes mensajes
  print ("-Obesidad leve-")
  print ("¡Recuerda tu salud es primero!")
  print("¡Cuidate!")
elif imc >= 35.0 and imc <=39.99:

# Cumpliendo la condicion anterior salen los siguientes mensajes  
  print ("-Obesidad media-")
  print ("¡Recuerda tu salud es primero!")
  print("¡Cuidate!")
elif imc >=40.0:

# Cumpliendo la condicion anterior salen los siguientes mensajes  
  print ("-Obesidad morbida-")
  print ("¡Recuerda tu salud es primero!")
  print("¡Cuidate!")



