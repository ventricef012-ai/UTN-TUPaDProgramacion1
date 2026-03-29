# Actividad 1
print ("Hola Mundo!")

#Actividad 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

#Actividad 3
nombre = input("Cual es su nombre?: ")
apellido = input("Cual es su apellido?: ")
edad = input("Cual es su edad?: ")
residencia = input("En que pais vive?: ")

print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}")

#Actividad 4
import math
radio = float(input("Cual es el radio del circulo que desea calcular su area y perimetro?: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print (f"El area del circulo es: {area}")
print (f"El perimetro del circulo es: {perimetro}")

#Actividad 5
segundos = int(input("Ingrese los segundos que desea convertir en horas: "))

horas = segundos / 3600

print(f"Equivalen a {horas} horas")

#Actividad 6
numero = int(input("Que tabla de multiplicar desea visualizar: "))
print(f"{numero} x 1 = {numero*1}")
print(f"{numero} x 2 = {numero*2}")
print(f"{numero} x 3 = {numero*3}")
print(f"{numero} x 4 = {numero*4}")
print(f"{numero} x 5 = {numero*5}")
print(f"{numero} x 6 = {numero*6}")
print(f"{numero} x 7 = {numero*7}")
print(f"{numero} x 8 = {numero*8}")
print(f"{numero} x 9 = {numero*9}")
print(f"{numero} x 10 = {numero*10}")


