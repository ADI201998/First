import RPi.GPIO as GPIO
import math
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
def gpio(x,y):
    X = (math.fabs(x)/255)*100
    Y = (math.fabs(y)/255)*100
    GPIO.PWM(18,X)
    GPIO.PWM(13,Y)
