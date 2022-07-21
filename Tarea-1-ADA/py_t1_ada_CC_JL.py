#-------------------------------------------------
# Jose Ignacio LeBlanc
# Christian Caceres
#-------------------------------------------------

#import matplotlib.pyplot as plt
#from matplotlib.collections import EventCollection
#import numpy as np
import time as time

#-------------------------------------------------

#CONSTANTES

FIN = 0

#-------------------------------------------------

#FUNCIONES GRAFICAS

def Fun1(n):
    
    suma = 0
    for i in range(n):
        suma = suma + 1

def Fun2(n):
    
    suma = 0
    for i in range(n):
        for j in range(n):
            suma = suma+1

def Fun3(n):
    print("3")

def Fun4(n):
    print("4")

def Fun5(n):
    if n < 1:
        return n
    return Fun5(n-1) + Fun5(n-1)

#-------------------------------------------------

#MENU BUCLE

def Menu():
    print("\t-MENU-")
    print("1) F(n) = n")
    print("2) F(n) = pow(n,2)")
    print("3) F(n) = Log(2) n")
    print("4) F(n) = nLog(2) n")
    print("5) F(n) = pow(2,n)")
    print(f"{FIN}) Salir")

    return int(input("Op: "))

#-------------------------------------------------

#OPERACION

def Operacion(op):

    n = int(input("[0-?]: "))

    start_timer = time.time()

    if op == 1:
        print("\tF(n) = n")
        Fun1(n) 
    elif op == 2:
        print("\tF(n) = pow(n,2)")
        Fun2(n)
    elif op == 3:
        print("\t3) F(n) = Log(2) n")
        Fun3(n)
    elif op == 4:
        print("\t4) F(n) = nLog(2) n")
        Fun4(n)
    elif op == 5:
        print("\t5) F(n) = pow(2,n)")
        Fun5(n)
    
    end_timer = time.time()
    execution_timer = end_timer - start_timer
    print("Tiempo de Ejecucion de la Funcion ", op,": ", execution_timer, " s")

#-------------------------------------------------

#PRINCIPAL

while True:
    op = Menu()
    
    if op >= 1 and op <= 5:
        Operacion(op)         
    elif op == FIN:
        break