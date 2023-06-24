import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math as m
import psycopg2
#from google_prueba import upload_file
conn = psycopg2.connect(
    host="containers-us-west-54.railway.app",
    port="5793",
    username="postgres",
    password="WD5HsM0kK2TjH68XNDWl",
    database="railway"
)
def cadencia(df,tiempo):
    datos=0
    contador =0
    suavizado=10
    pasos = []
    paso_anterior = 0
    pasos_finales = []
    tiempos_paso = []
    for row in df.values:
        if(contador == suavizado):
            pasos.append(datos)
            contador = 0
        datos = row[19]
        contador = contador + 1
    for i in range(len(pasos)):
        if(pasos[i] != paso_anterior):
            pasos_finales.append(pasos[i])
            tiempos_paso.append(tiempo[i])
        paso_anterior = pasos[i]
        
        tiempos_final = []
        
    for j in range(len(tiempos_paso)-1):
        
        tiempos_final.append(tiempos_paso[j+1]-tiempos_paso[j])
            
    tiempo_mean = sum(tiempos_final)/len(tiempos_final)
    
    res = 60/tiempo_mean
    
    print(res)
        
    return res
   
def long_paso(df):
    datos=0
    contador =0
    suavizado=10
    datosDis=0
    distancias=[]
    pasos = []
    paso_anterior = 0
    pasos_finales = []
    distancia_paso = []
    distancias_final = []
    for row in df.values:
        if(contador == suavizado):
            pasos.append(datos)
            distancias.append(datosDis)
            contador = 0
        datos = row[18]
        datosDis = row[19]
        contador = contador + 1
    for i in range(len(pasos)):
        if(pasos[i] != paso_anterior):
            pasos_finales.append(pasos[i])
            distancia_paso.append(distancias[i])
        paso_anterior = pasos[i]
        
        
        
    for j in range(0,5):
        
        distancias_final.append(distancia_paso[j+1]-distancia_paso[j])
            
    distancia_mean = sum(distancias_final)/len(distancias_final)
    
    res = distancia_mean
    
    print(res)
        
    return res

def angulo_tobillo(df,columna_tobillo,columna_pie):
    angulos_tobillo = []
    datos1 = 0
    datos2 = 0
    contador=0
    suavizado = 10
    for row in df.values:
        if(contador == suavizado):
            if(datos1/suavizado >0 and datos2/suavizado <0):
                aux = 90 - abs(datos1/suavizado) - abs(datos2/suavizado)
                angulos_tobillo.append(aux)
                contador = datos1 = datos2 =0
            elif(datos1/suavizado<0 and datos2/suavizado >0):
                aux = 90 + abs(datos1/suavizado) + abs(datos2/suavizado)
                angulos_tobillo.append(aux)
                contador = datos1 = datos2 =0
            elif(datos1/suavizado>0 and datos2/suavizado >0):
                aux = 90 - abs(datos1/suavizado) + abs(datos2/suavizado)
                angulos_tobillo.append(aux)
                contador = datos1 = datos2 =0
            elif(datos1/suavizado<0 and datos2/suavizado <0):
                aux = 90 + abs(datos1/suavizado) - abs(datos2/suavizado)
                angulos_tobillo.append(aux)
                contador = datos1 = datos2 =0
            else:
                aux = 90 + abs(datos1/suavizado) + abs(datos2/suavizado)
                angulos_tobillo.append(aux)
                contador = datos1 = datos2 =0

        datos1 += row[columna_tobillo]
        datos2 += row[columna_pie]
        contador = contador + 1
    
    #plt.title("Angulos tobillo")
    #plt.plot(angulos_tobillo)
    #plt.show()
    return angulos_tobillo

def angulo_rodilla(df,columna_rodilla,columna_tobillo):
    angulos_rodilla = []
    datos1 = 0
    datos2 = 0
    contador=0
    suavizado = 10
    for row in df.values:
        if(contador == suavizado):
            if(datos1/suavizado <=0 and datos2/suavizado >=0):
                aux = 180 - abs(datos1/suavizado) - abs(datos2/suavizado)
                angulos_rodilla.append(aux)
                contador = datos1 = datos2 =0
            elif(datos1/suavizado >0 and datos2/suavizado >0):
                aux = 180 + abs(datos1/suavizado) - abs(datos2/suavizado)
                angulos_rodilla.append(aux)
                contador = datos1 = datos2 =0
            elif(datos1/suavizado<0 and datos2/suavizado <0):
                aux = 180 - abs(datos1/suavizado) + abs(datos2/suavizado)
                angulos_rodilla.append(aux)
                contador = datos1 = datos2 =0
            else:
                aux = 180 - abs(datos1/suavizado) - abs(datos2/suavizado)
                angulos_rodilla.append(aux)
                contador = datos1 = datos2 =0

        datos1 += row[columna_rodilla]
        datos2 += row[columna_tobillo]
        contador = contador + 1
    #plt.title("Angulos rodilla")
    #plt.plot(angulos_rodilla)
    #plt.show()    
    return angulos_rodilla
    #df = pd.DataFrame({"Angulo Rodilla":angulos_rodilla})
    #return df

def angulo_pie(df,pie,columna):
    angulos_pie = []
    datos = 0
    contador = 0
    suavizado =10
    unidad_pie = 1
    if(pie == "izquierdo"):
        unidad_pie  = -1
        
    for row in df.values:
        if(contador == suavizado):
            aux = unidad_pie*datos
            angulos_pie.append(aux/suavizado)
            contador = datos = 0

        datos += row[columna]
        contador = contador + 1
        
    #plt.title("Angulos pie")
    #plt.plot(angulos_pie)
    #plt.show()
    return angulos_pie
     
def extraccion_tiempo(df):
    tiempo = []
    datos = 0
    contador = 0
    suavizado =10
    
        
    for row in df.values:
        if(contador == suavizado):
            tiempo.append(datos)
            contador = 0

        datos = row[0]
        contador = contador + 1
        
    return tiempo

def start_data_analisis(folio):
    
    df = pd.read_csv(folio+'.csv')
    tiempo = extraccion_tiempo(df)
    #cadencia(df,tiempo)
    long_paso(df)
    
    angulos_pie_derecho = angulo_pie(df,"derecho",15)
    angulos_pie_izquierdo = angulo_pie(df,"izquierdo",0)
    angulos_rodilla_derecha =  angulo_rodilla(df,9,12)
    angulos_rodilla_izquierda =  angulo_rodilla(df,6,3)
    angulos_tobillo_derecho = angulo_tobillo(df,12,10)
    angulos_tobillo_izquierdo = angulo_tobillo(df,3,1)
    df = pd.DataFrame({"Tiempo":tiempo,"AnguloRodillaDerecha":angulos_rodilla_derecha,"AnguloRodillaIzquierda":angulos_rodilla_izquierda,"AngulosPieDerecho":angulos_pie_derecho,
                       "AngulosPieIzquierdo":angulos_pie_izquierdo,"AngulosTobilloDerecho":angulos_tobillo_derecho,"AngulosTobilloIzquierdo":angulos_tobillo_izquierdo})

    df.to_csv("./"+folio+"res.csv",index=False)
    
start_data_analisis("ABR1234")
start_data_analisis("ADR1234")
#start_data_analisis("ALE1234")
start_data_analisis("ALX1234")
start_data_analisis("CAR1234")
start_data_analisis("DIE1234")
start_data_analisis("EDU1234")
start_data_analisis("ERI1234")
start_data_analisis("NAT1234")
start_data_analisis("SOT1234")
    #upload_file(folio+"res.csv")
    
    