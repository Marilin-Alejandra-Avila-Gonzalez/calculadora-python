
# funcion de suma
def sumar (a,b):
 return a + b
 
# funcion de resta
def restar (a,b):
  return a - b

#funcion de multiplicacion
def multiplicar (a, b):
 return a * b

#funcion de division
def dividir (a, b):
  return a / b

# mostrar el menu de opciones al usuario

print("1sumar\n2restar\n3multiplicar\n4dividir")

opcion = input("elige una operacion")

if opcion =="1":
  
    num1 = int(input("ingresa el primer numero"))
    num2 = int(input("ingresa el segundo numero"))
    print("Resultado:", sumar(num1,num2))

elif opcion == "2":

    num1= int(input("ingresa el primer numero"))
    num2= int(input("ingresa el segundo numero"))
    print("Resultado:", restar(num1,num2))
    

elif opcion == "3":
    num1= int(input("ingresa el primer numero"))
    num2= int(input("ingresa el segundo numero"))
    print("Resultado:", multiplicar(num1,num2))

elif opcion == "4":
    num1= int(input("ingresa el primer numero"))
    num2= int(input("ingresa el segundo numero"))
    if num2 == 0:
       print("Error: no se puede dividir entre cero")
    else:
       print("Resultado:", dividir(num1,num2))

else:
    print("opcion no valida")