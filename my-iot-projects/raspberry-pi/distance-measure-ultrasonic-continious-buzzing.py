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
distance = 10
isBuzzing = False
GPIO.output(BUZZER, False)

def get_Distance():
    GPIO.output(TRIG, False)
    GPIO.output(TRIG, True)
    # 10 micro sec
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print("Distance: ", distance, "cm")
    return distance


while True:
    distance = get_Distance()
    if distance < 5 and not isBuzzing:
        GPIO.output(BUZZER, True)
        print("Buzzing")
    else:
        GPIO.output(BUZZER, False)

GPIO.cleanup()

