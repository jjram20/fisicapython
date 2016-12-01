#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Simulaciones de física
Autor: José de Jesús Ramírez Jiménez
'''

import Tkinter as tk
import visual as vs
import visual.graph as vgraph
import numpy as np
import matplotlib.animation as animation

class Ventana(object):
    def __init__(self):
        ventana=tk.Tk()
        ventana.title(u"Simulaciones de física")
        label1=tk.Label(ventana,text=u"Seleccione una simulación").grid(row=0)
        boton1=tk.Button(ventana,text=u"Caída libre",command=self.viCaidalibre).grid(row=1)
        boton2=tk.Button(ventana,text=u"Movimiento armónico simple",command=self.viResorte).grid(row=2)
        boton3=tk.Button(ventana,text=u"Energía potencial",command=self.viEnergia).grid(row=3)
        ventana.mainloop()
    def viResorte(self):
        ventanaR=tk.Toplevel()
        ventanaR.title(u"Movimiento armónico simple")
        label1R=tk.Label(ventanaR,text=u"Inserte los valores iniciales").grid(row=0)
        label2R=tk.Label(ventanaR,text=u"Constante del resorte (N/m)").grid(row=1)
        self.kR=tk.Entry(ventanaR,bg="white")
        self.kR.grid(row=2)
        label3R=tk.Label(ventanaR,text=u"Masa (kg)").grid(row=3)
        self.masaR=tk.Entry(ventanaR,bg="white")
        self.masaR.grid(row=4)
        boton1R=tk.Button(ventanaR,text=u"Aceptar",command=self.sResorte).grid(row=5)
        ventanaR.mainloop()
    def viCaidalibre(self):
        ventanaCL=tk.Toplevel()
        ventanaCL.title(u"Caída libre")
        label1CL=tk.Label(ventanaCL,text=u"Inserte los valores iniciales").grid(row=0)
        label2CL=tk.Label(ventanaCL,text=u"Altura (m)").grid(row=1)
        self.alturaCL=tk.Entry(ventanaCL,bg="white")
        self.alturaCL.grid(row=2)
        label3CL=tk.Label(ventanaCL,text=u"Velocidad en el eje x (m/s)").grid(row=3)
        self.velocidadX=tk.Entry(ventanaCL,bg="white")
        self.velocidadX.grid(row=4)
        boton1CL=tk.Button(ventanaCL,text=u"Aceptar",command=self.sCaidalibre).grid(row=5)
        ventanaCL.mainloop()
    def viEnergia(self):
		ventanaE=tk.Toplevel()
		ventanaE.title(u"Energía potencial")
		label1E=tk.Label(ventanaE,text=u"Inserte los valores iniciales").grid(row=0)
		label2E=tk.Label(ventanaE,text=u"Altura (m)").grid(row=1)
		self.alturaE=tk.Entry(ventanaE,bg="white")
		self.alturaE.grid(row=2)
		label3E=tk.Label(ventanaE,text=u"Masa (kg)").grid(row=3)
		self.masaE=tk.Entry(ventanaE,bg="white")
		self.masaE.grid(row=4)
		boton1E=tk.Button(ventanaE,text=u"Aceptar",command=self.sEnergia).grid(row=5)
		ventanaE.mainloop()
    def sResorte(self):
        self.kR=self.kR.get()
        self.masaR=self.masaR.get()
        try:
            self.kR=float(self.kR)
            self.masaR=float(self.masaR)
        except:
            self.alerta()
        gdpos=vgraph.gdisplay(x=600,y=0,xtitle='Tiempo',ytitle='Posicion')
        plotpos=vgraph.gcurve(gdisplay=gdpos,color=vs.color.red)
        gdvel=vgraph.gdisplay(x=600,y=600,xtitle='Velocidad',ytitle='Tiempo')
        plotvel=vgraph.gcurve(gdisplay=gdvel,color=vs.color.blue)
        gdacl=vgraph.gdisplay(x=0,y=900,xtitle='Aceleracion',ytitle='Tiempo')
        plotacl=vgraph.gcurve(gdisplay=gdacl,color=vs.color.green)
        resorte=vs.helix(pos=(0,5,0),axis=(0,0,-1),radius=0.5,color=vs.color.red)
        resfera=vs.sphere(pos=(0,0,0),radius=0.7,color=vs.color.blue)
        t=0
        while t<=100:
            resorte.axis=(0,-5+3*np.cos(np.sqrt(self.kR/self.masaR)*t),-1)
            resfera.pos=(0,3*np.cos(np.sqrt(self.kR/self.masaR)*t),0)
            plotpos.plot(pos=(t,3*np.cos(np.sqrt(self.kR/self.masaR)*t)))
            plotvel.plot(pos=(t,-3*np.sqrt(self.kR/self.masaR)*np.sin(np.sqrt(self.kR/self.masaR)*t)))
            plotacl.plot(pos=(t,-3*(self.kR/self.masaR)*np.cos(np.sqrt(self.kR/self.masaR)*t)))
            t+=0.01
            vs.rate(100)
    def sCaidalibre(self):
        self.alturaCL=self.alturaCL.get()
        self.velocidadX=self.velocidadX.get()
        try:
            self.alturaCL=float(self.alturaCL)
            self.velocidadX=float(self.velocidadX)
        except:
            self.alerta()
        gdpos=vgraph.gdisplay(x=600,y=0,xtitle='Tiempo',ytitle='Posicion(y)')
        plotpos=vgraph.gcurve(gdisplay=gdpos,color=vs.color.red)
        gdvel=vgraph.gdisplay(x=600,y=600,xtitle='Velocidad',ytitle='Tiempo')
        plotvel=vgraph.gcurve(gdisplay=gdvel,color=vs.color.blue)
        gdacl=vgraph.gdisplay(x=0,y=900,xtitle='Aceleracion',ytitle='Tiempo')
        plotacl=vgraph.gcurve(gdisplay=gdacl,color=vs.color.blue)
        suelo=vs.box(pos=(0,-5,0),length=30,height=0.1,width=1,color=vs.color.blue)
        esferaC=vs.sphere(pos=(0,self.alturaCL,-2),radius=1,color=vs.color.red)
        T=np.sqrt(2*(self.alturaCL+5)/9.8)
        t=0
        while t<T:
            esferaC.pos=(self.velocidadX*t,self.alturaCL-9.8*t**2/2,-2)
            plotpos.plot(pos=(t,self.alturaCL-9.8*t**2/2))
            plotvel.plot(pos=(t,-9.8*t))
            plotacl.plot(pos=(t,-9.8))
            t+=0.001
            vs.rate(100)
    def sEnergia(self):
		self.alturaE=self.alturaE.get()
		self.masaE=self.masaE.get()
		try:
			self.alturaE=float(self.alturaE)
			self.masaE=float(self.masaE)
		except:
			self.alerta()
		gdenergia=vgraph.gdisplay(x=600,y=0,xtitle='Tiempo',ytitle='Energia')
		plotpot=vgraph.gcurve(gdisplay=gdenergia,color=vs.color.green)
		plotcin=vgraph.gcurve(gdisplay=gdenergia,color=vs.color.red)
		plottot=vgraph.gcurve(gdisplay=gdenergia,color=vs.color.blue)
		sueloE=vs.box(pos=(0,-1,0),length=30,height=0.1,width=1,color=vs.color.blue)
		esferaE=vs.sphere(pos=(0,self.alturaE,-2),radius=1,color=vs.color.red)
		T=np.sqrt(2*(self.alturaE)/9.8)
		t=0
		while t<=T:
			esferaE.pos=(0,self.alturaE-9.8*t**2/2,-2)
			plotpot.plot(pos=(t,9.8*self.masaE*(self.alturaE-9.8*t**2/2)))
			plotcin.plot(pos=(t,self.masaE*(9.8*t)**2/2))
			plottot.plot(pos=(t,9.8*self.masaE*(self.alturaE-9.8*t**2/2)+self.masaE*(9.8*t)**2/2))
			t+=0.01
			vs.rate(100)
    def alerta(self):
        v_alerta=tk.Toplevel()
        v_alerta.title("Error")
        l_alerta=tk.Label(v_alerta,text=u"Introduzca valores numéricos").grid(row=0)
        v_alerta.mainloop()
        

VENTANA=Ventana()
