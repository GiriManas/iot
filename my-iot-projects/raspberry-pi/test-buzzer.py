import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
BUZZER = 24
while True:
    GPIO.setup(BUZZER, GPIO.OUT)
    GPIO.output(BUZZER, False)

    GPIO.output(BUZZER, True)
