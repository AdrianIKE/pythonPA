import serial
import time
from manejoDatos import start_data_analisis

def lecturaDatos():
    
    '''Declaracion de variables globales'''
    
    #Tiempo
    tiempo = time.time()
    
    #Puerto USB a utilizar
    serialarduino = serial.Serial("/dev/ttyUSB0",115200,timeout=50) 
    
    #Bandera para obtener el folio
    bandera_folio = 0 
    
    #Almacenador de folio
    folio = '' 
    
     #Bandera para el stop del codigo
    bandera = 0
    
    #?
    interruptor = 0
    
    #ALmacenamiento de una lectura anterior a la actual
    lectura_anterior = "" 
    
    while bandera_folio == 0:
        lectura = serialarduino.readline().decode('ascii')
        if(lectura[0] == '*'):
            print(lectura);
            folio = lectura[7:-1]
            bandera_folio = 1
            
    archivo = open(folio.strip()+".csv", 'w')
    archivo.write('tiempo,yaw1,pitch1,roll1,yaw2,pitch2,roll2,yaw3,pitch3,roll3,yaw4,pitch4,roll4,yaw5,pitch5,roll5,yaw6,pitch6,roll6,paso,dist'+'\n')
    
    while True:
        lectura = serialarduino.readline().decode('ascii')
        
        
        #Calulos de los tiempos de ejecucion
        
        tiempo_raw = round((time.time() - tiempo),3)
        tiempo_ejecucion = str(round((time.time() - tiempo),3))
        
        #Inservibles
        print(lectura)
        print(tiempo_raw)
        print(bandera)
        
        
        
        #Se utilizan las lecturas para detener el programa
        
        if(lectura == lectura_anterior and lectura[0]== '{'):
            bandera = bandera + 1;
        else:
            bandera = 0
            
        
        #Guardamos lectura aneterior al final de cada iteracion
        lectura_anterior = lectura

            
        if (bandera > 1000):
            break;
            
        #Agregar datos al archivo
        if(lectura[0] == '{'):
            lectura = tiempo_ejecucion+','+lectura[1:-3]
            archivo.write(lectura.strip() + '\n')
            
        
        
        
        
    archivo.close()

    start_data_analisis(folio.strip())
    
