#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np #Se hace uso de los módulos numpy y matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


namefile='caidapy.dat'
#Toma la columna de datos correspondiente a la posición en x y almacena toda la columna como un arreglo
x=np.genfromtxt(namefile,usecols=(3))
#Mismo caso que x pero para eje y
y=np.genfromtxt(namefile,usecols=(1))
#Genera una figura y una instancia ax para manipulación de ciertos parámetros dentro de la gráfica
figura,ax=plt.subplots()
#Gráfica toda la trayectoria realizada por la partícula
plt.plot(x,y)
#Configura los ejes de la gráfica
ax.axis([min(x),max(x),min(y),max(y)])
plt.title(u'Simulación de caída libre')
plt.xlabel(u'Posición en x (m)')
plt.ylabel(u'Posición en y (m)')
#Genera una instancia que producirá el efecto de animación de la partícula
graph,=plt.plot(0,0,'o')
#Esta función actualiza la posición de la partícula, es necesaria para usarla después en la función FuncAnimation
def animacion(i,a,b):
    graph.set_xdata(a[i])
    graph.set_ydata(b[i])
    return graph,

#Genera la animación en la figura "figura", de acuerdo a la función animación, en un rango de 0 hasta la cantidad de datos x
#El rango lo que hace es utilizar cada valor tomado de la columna de datos del archivo .dat
anim=animation.FuncAnimation(figura,animacion,np.arange(0,len(x)),fargs=(x,y),blit=True,interval=0,repeat=True)
#La siguiente línea guardaría la animación en un archivo mp4, se ponen 120 fps para obtener una animación buena, que no se vea lenta
#anim.save('caidapy.mp4',fps=120,extra_args=['-vcodec','libx264'])
#Muestra la animación
plt.show()
