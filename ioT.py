import RPi.GPIO as GPIO
import time

buttonup=True
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18,0)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16,0)

while True:
    
    if(GPIO.input(23)!=True):
            
        GPIO.output(16,1)
        time.sleep(5)
    
    GPIO.output(16,0)
        






