from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

LED1_PIN = 17 
LED2_PIN = 27 


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)

@app.route('/led1/<state>')
def led1_control(state):
    if state == 'on':
        GPIO.output(LED1_PIN, GPIO.HIGH)  
        return '<h3>LED 1 - ON</h3>'
    elif state == 'off':
        GPIO.output(LED1_PIN, GPIO.LOW)  
        return '<h3>LED 1 - OFF</h3>'
    else:
        return '<h3>Error: Invalid state!</h3>'

@app.route('/led2/<state>')
def led2_control(state):
    if state == 'on':
        GPIO.output(LED2_PIN, GPIO.HIGH)  
        return '<h3>LED 2 - ON</h3>'
    elif state == 'off':
        GPIO.output(LED2_PIN, GPIO.LOW)  
        return '<h3>LED 2 - OFF</h3>'
    else:
        return '<h3>Error: Invalid state!</h3>'

@app.route('/')
def index():
    return '<h3>LED Control - Use /led1/on or /led1/off, /led2/on or /led2/off</h3>'

if __name__ == "__main__":
    try:
        app.run(debug=True, host='0.0.0.0')
    finally:
        GPIO.cleanup()  
