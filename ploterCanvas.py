#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:46:59 2025

@author: lucioiracema
"""

import tkinter as tk
from tkinter import ttk
from random import randint as ri
import sys, os, threading, time

SENO45 = 0.707106781
CANVAS_LARGURA = 500
CANVAS_ALTURA = 500
temperatura, umidade, pressao = 10000, 100000, 1000000

def Cria_Eixos(largura, altura):
    xInicial = largura /3
    xFinal = largura
    yInicial = (altura/3)*2
    yFinal = 0
    
    eixoX = canvas.create_line(xInicial, yInicial, xFinal, yInicial, 
                               fill="red", width=3)
    eixoY = canvas.create_line(xInicial, yInicial, xInicial, yFinal,
                               fill="green", width=3)
    eixoZ = canvas.create_line(xInicial, yInicial, 0, altura,
                               fill="blue", width = 3)

def PlotaPonto(X,Y,Z):    
    
    xEquivalente= ((X-SENO45*Z) + CANVAS_LARGURA/3)
    yEquivalente = ((CANVAS_ALTURA/3)*2) + (SENO45*Z) - Y
    ponto = canvas.create_oval(xEquivalente-5, yEquivalente-5, xEquivalente+5,
                               yEquivalente+5, fill= "black",
                               width=2, outline="yellow")
    linhaX = canvas.create_line(xEquivalente, yEquivalente,
                                xEquivalente-X, yEquivalente, fill="white")
    linhaY = canvas.create_line(xEquivalente, yEquivalente, 
                                xEquivalente, yEquivalente + Y,
                                fill="White")
    linhaZ = canvas.create_line(xEquivalente,yEquivalente, 
                                xEquivalente+(Z*SENO45),
                                yEquivalente- (Z*SENO45), fill="white")
    linhaXparalelaXZ = canvas.create_line(xEquivalente, yEquivalente +Y,
                                        xEquivalente - X, yEquivalente +Y,
                                        fill= "white")
    linhaXparalelaXY = canvas.create_line(xEquivalente+(Z*SENO45),
                                          yEquivalente-(Z*SENO45),
                                          xEquivalente+(Z*SENO45)-X,
                                          yEquivalente-(Z*SENO45), fill="white")
    linhaYparalelaXY = canvas.create_line(xEquivalente+(Z*SENO45),
                                          yEquivalente-(Z*SENO45),
                                          xEquivalente+(Z*SENO45),
                                          yEquivalente-(Z*SENO45)+Y, fill="white")
    linhaYparalelaYZ = canvas.create_line(xEquivalente-X, yEquivalente,
                                          xEquivalente - X, yEquivalente +Y,
                                          fill="white")
    linhaZparalelaXZ = canvas.create_line(xEquivalente, yEquivalente + Y,
                                          xEquivalente+(Z*SENO45),
                                          yEquivalente-(Z*SENO45)+Y, 
                                          fill="white")
    linhaZparalelaYZ = canvas.create_line(xEquivalente+(Z*SENO45)-X,
                                          yEquivalente-(Z*SENO45),
                                          xEquivalente-X, yEquivalente, 
                                          fill="white")
    
    time.sleep(0.1)
    canvas.delete(  linhaX, linhaY, linhaZ, linhaXparalelaXY,linhaXparalelaXZ, 
                  linhaYparalelaXY,linhaYparalelaYZ, 
                  linhaZparalelaXZ,linhaZparalelaYZ)
    
def Cria_Valores():
    global temperatura, umidade, pressao    
    if temperatura>200:
        temperatura = ri(0,200) 
        umidade = ri(0,200) 
        pressao = ri(0, 200)
        print(temperatura)
        print(umidade)
        print(pressao)
    for i in range(1000):
        temperatura += ri(-5,5)
        if temperatura < 0:
            temperatura = 0
        umidade += ri(-5,5)
        if umidade < 0:
            umidade = 0
        pressao += ri(-5,5)
        if pressao < 0:
            pressao = 0
        PlotaPonto(temperatura, umidade, pressao)
        
        
        


raiz = tk.Tk()
frame = ttk.Frame(raiz,width=800, height=100)
frame.grid(row=0, column=0)
frame2 = ttk.Frame(raiz, width=800, height=400)
frame2.grid(row=1,column=0)
canvas = tk.Canvas(frame2, width=CANVAS_LARGURA, height=CANVAS_ALTURA, 
                   background="black")
canvas.grid()
frame3 = ttk.Frame(raiz, width=800, height=100)
frame3.grid()
Cria_Eixos(CANVAS_LARGURA, CANVAS_ALTURA)
th = threading.Thread(target=Cria_Valores)
th.start()
#Cria_Valores()
#PlotaPonto(100, 100, 100)

raiz.mainloop()
