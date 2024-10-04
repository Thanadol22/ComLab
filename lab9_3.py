from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)


LED1_PIN = 17  
LED2_PIN = 27  


GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)

@app.route('/', methods=['GET', 'POST'])
def control_led():
    led1_status = GPIO.input(LED1_PIN)
    led2_status = GPIO.input(LED2_PIN)

    if request.method == 'POST':
        if 'led1_on' in request.form:
            GPIO.output(LED1_PIN, GPIO.HIGH)  
        elif 'led1_off' in request.form:
            GPIO.output(LED1_PIN, GPIO.LOW)   
        elif 'led2_on' in request.form:
            GPIO.output(LED2_PIN, GPIO.HIGH)  
        elif 'led2_off' in request.form:
            GPIO.output(LED2_PIN, GPIO.LOW)   

  
    led1_status = GPIO.input(LED1_PIN)
    led2_status = GPIO.input(LED2_PIN)

    return render_template('lab9.3.html', led1_status=led1_status, led2_status=led2_status)

@app.route('/cleanup')
def cleanup():
    GPIO.cleanup()  
    return "GPIO cleanup done!"

if __name__ == "__main__":
    try:
        app.run(debug=True, host='0.0.0.0')
    finally:
        GPIO.cleanup()  
