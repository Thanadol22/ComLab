import RPi.GPIO as GPIO
import time
 
LED = 21
SW = 22
led_state = False  
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
 
try:
    while True:
        if GPIO.input(SW) == GPIO.LOW:  
            led_state = not led_state  
            GPIO.output(LED, led_state)  
            print(f"LED => {'OFF' if led_state else 'ON'}")
           
            while GPIO.input(SW) == GPIO.LOW:
                time.sleep(0.1)  
           
except KeyboardInterrupt:
    GPIO.cleanup()
 
print("\nBye...")