#! /usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np #Hacer uso de la librería numpy para cálculo numérico

archivo=open('caidapy.dat','w') #Se genera una instancia que crea un archivo en el cual se escriben los datos
dt=0.01 #Diferencial de tiempo (s)
g=-9.8 #Constante de aceleración gravitacional (m/s^2)
t=None #Se generan las variables de tiempo, posición en y, x y v será la velocidad instántanea en el eje y
y=None
v=None
x=None
v0=0 #Velocidad inicial en el eje y (m/s)
y0=4 #Posición inicial en el eje y (m)
izq=0 #Posición de la pared en el lado izquierdo (m)
der=3 #Posición de la pared en el lado derecho (m)
u0=5 #Velocidad en el eje x (m/s)
x0=0 #Posición inicial en el eje x (m)
for i in np.arange(0,1425): #arange genera un arreglo de 0 a 1425 de 1 en 1, 1425 dividido entre el diferencial de tiempo dará el tiempo total que se considera
	t=i*dt; #Dentro del bucle se calcula para cada instante de acuerdo al diferencial el tiempo, la posición en y, velocidad en y, posición en x correspondientes a debido instante
	y=0.5*g*dt**2+v0*dt+y0 #Unidades de y (m)
	v=g*dt+v0 #Unidades de v (m/s)
	x=u0*dt+x0 #Unidades de x (m)
	archivo.write("%f %f %f %f\n" % (t,y,v,x)) #Se escribe en el archivo con formato float los datos calculados anteriormente dentro del bucle en orden tiempo, posición x, velocidad y, posición x. Con \n cambia de renglón.
	x0=x #Se reubican los valores iniciales de la posición en x, posición en y, y velocidad en y para el siguiente instante
	y0=y #x0 en metros, y0 en metros, v0 en m/s
	v0=v
	if y<0: #Se declara un if para que la pelota bote cuando llegue al piso
		v0=-0.75*v0 #Se disminuye la velocidad del proyectil posterior al choque y se cambia el signo con la intención de que haga el efecto de bote
		y0=0 #Se ubica la posición inicial en y para el siguiente diferencial
	if x>der:
		u0=-0.75*u0 #Se declara un if para que la pelota bote cuando choque en la pared derecha, mismo algoritmo que para el rebote en el eje y, solo que aplicado al eje x
		x0=der
	elif x<izq: #Se declara un if para que la pelota bote cuando choque en la pared izquierda
		u0=-0.75*u0
		x0=izq 
archivo.close() #Se cierra la instancia que interactúa con el archivo para evitar errores
