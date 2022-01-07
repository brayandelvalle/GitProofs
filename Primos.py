## Método de la Criba de Eratóstenes para calcular primos

import numpy as np

n=100		## Número hasta que vamos a encontrar primos

## Creamos la matriz 

N=[None]*(n-1)
for i in range(n-1):
	N[i] = [None]*2
	
## Generamos la matriz con números desde 2 hasta n

for i in range(2, n+1 , 1):
	N[i-2][0] = i 
	N[i-2][1] = True 
	

## Encontramos los compuestos de acuerdo al método de Eratostenes

lim = int(n/2)+1

for i in range( 0 , lim , 1):
	num = N[i][0]
#	valor = N[i][1]
	if ( N[i][1] is True ):
		for j in range ( i+2 , lim , 1 ):
			compuesto = num*j
			if ( compuesto > n ):
				j = lim 
			else:
				N[compuesto-2][1] = False

print ("Los números primos desde 1 hasta %i son:"%n)
for i in range ( 0 , n-1 , 1):
	if (N[i][1] is True):
		print (N[i][0])
		

