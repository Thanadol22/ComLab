import RPi.GPIO as GPIO
import time

red_pin = 21
green_pin = 20
blue_pin = 16
SW = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

def set_color(r, g, b):
    GPIO.output(red_pin, r)
    GPIO.output(green_pin, g)
    GPIO.output(blue_pin, b)

colors = [
    (1, 1, 1),  # White
    (1, 1, 0),  # Yellow
    (1, 0, 1),  # Magenta
    (1, 0, 0),  # Red
    (0, 1, 1),  # Cyan
    (0, 1, 0),  # Green
    (0, 0, 1),  # Blue
    (0, 0, 0)   # Off
]

current_color = 0 

try:
    while True:
        if GPIO.input(SW) == GPIO.LOW:  
            set_color(*colors[current_color])  
            print(f"LED color: {colors[current_color]}")
            current_color = (current_color + 1) % len(colors)  
            while GPIO.input(SW) == GPIO.LOW: 
                time.sleep(0.1)
            time.sleep(0.2) 
            
except KeyboardInterrupt:
    GPIO.cleanup()
    print("โปรแกรมหยุดทำงานแล้ว")
