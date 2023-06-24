import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def angulo_tobillo(df):
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

        datos1 += row[0]
        datos2 += row[1]
        contador = contador + 1

    #plt.title("Angulos tobillo")
    #plt.plot(angulos_tobillo)
    #plt.show()

def angulo_rodilla(df):
    angulos_rodilla = []
    datos1 = 0
    datos2 = 0
    contador=0
    suavizado = 1
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

        datos1 += row[0]
        datos2 += row[1]
        contador = contador + 1

    #plt.title("Angulos Rodilla")
    #plt.plot(angulos_rodilla)
    #plt.show()    

def main():
    df = pd.read_csv('AnguloRodilla.csv')
    #angulo_tobillo(df)
    angulo_rodilla(df)


main()