import RPi.GPIO as GPIO
import time
import subprocess
from ArduinoReading import lecturaDatos

def activar():
    print('El boton fue presionado')
    red.start((0/2.55))
    green.start((255/2.55))
    blue.start((0/2.55))
    lecturaDatos()
    time.sleep(0.2)
    
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

red= GPIO.PWM(23,75)
green= GPIO.PWM(24,75)
blue= GPIO.PWM(25,75)

try:
    while True:
        input_state = GPIO.input(18)
        red.start((255/2.55))
        green.start((0/2.55))
        blue.start((0/2.55))
        if input_state == False:
            activar()
except KeyboardInterrupt:
    red.stop()
    green.stop()
    blue.stop()
    GPIO.cleanup()
        #subprocess.call(something)
        # block until finished (depending on application)