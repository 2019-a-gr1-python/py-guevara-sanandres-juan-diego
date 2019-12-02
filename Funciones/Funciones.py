#Funciones
def hola_mundo():
	print("Hola estupida")
hola_mundo()
#Argumentos requeridos la f es chevere porque te permite de  todo
def sumar_dos_numeros(num1,num2):
	return num1+num2
print(f"Suma {sumar_dos_numeros(1,2)}")
#Opcionales
def imprimir_universidad(nombre='EPN'):
	print(f"{nombre}")
imprimir_universidad()
#Parametro por posicion 
def imprimir_carro(color,placa,hp,anio=1999):
	print(f"Color: {color}")
	print(f"Placa: {placa}")
	print(f"Hourse Power: {hp}")
	print(f"Año: {anio}")
imprimir_carro("rojo",123,23,2010)
#Name Parameters tu pones el nombre del atributo y luego le pones el valor
#todos los argumentos hay que mandar
#para opcionales los parametros requeridos y Luego los opcionales 
#No es necesario enviar los parametros opcionales 
#Si ya puse un nombrado, debe seguir siendo nombrado

imprimir_carro(placa=234,color="azulado",hp=2)

#PARAMETROS INFINITOS 

def sumar_numeros_infinita_veces(primer_numeros,*numeros):
	print(type(primer_numeros))
	print(type(numeros))
#	print(type(tuplas))
	long=len(numeros)
	if long==0:
		return primer_numeros
	else:
		suma=0+primer_numeros
		for numero in numeros:
			suma=suma+numero
		return suma
print(f"{sumar_numeros_infinita_veces(1,2,3)}")
#Parametros aun mas raros key work arguments
#Key_word_arguments son los parametros que no estan definidos en la funcion 
def imprir_configuracion(nombre,valor=10,*valor_carga,**key_word_rguments):
	print(type(key_word_rguments))
	print(key_word_rguments)
imprir_configuracion("config_1",20,tiempo_espera=10,conexiones=55)
