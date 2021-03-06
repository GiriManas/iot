'''
BEEPING IF THE DISTANCE IS LESS THAN 5CM

'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG = 02
ECHO = 03
BUZZER = 24

print("Distance Measurement in Progress")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)
while True:
    GPIO.output(BUZZER, False)
    GPIO.output(TRIG, False)
    print("Let sensor take a breath")
    time.sleep(2)
    GPIO.output(TRIG, True)
    # 10 micro sec
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration =  pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance =  round(distance, 2)
    print("Distance: ", distance, "cm")
    if distance < 5:
        GPIO.output(BUZZER, True)
        time.sleep(1)
        print("Buzzing")
GPIO.cleanup()