#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_cors import CORS
from sense_hat import SenseHat
from led_status import get_led
from set_led import set_led

sense = SenseHat()
deviceID="device1"
#clear sensehat and intialise light_state
sense.clear()
sense.low_light = True

#create Flask app instance and apply CORS
app = Flask(__name__)
CORS(app)

@app.route('/sensehat/environment',methods=['GET'])
def current_environment():
    temperature=round(sense.temperature,2)
    humidity=round(sense.humidity,2)
    msg = {"deviceID": deviceID,"temp":temperature,"humidity":humidity}
    return str(msg)+"\n"

@app.route('/sensehat/light',methods=['GET'])
def light_get():
    state=get_led()
    ledlight=state["ledlight"]
    ledcode=state["ledcode"]
    msg = {"deviceID": deviceID,"ledlight":ledlight,"ledcode":ledcode}
    return str(msg)+"\n"
    #return render_template('status.html', ledlight=ledlight, ledcode=ledcode)

@app.route('/sensehat/light',methods=['POST'])
def light_post():
    ledstate=request.args.get('state')
    print (state)
    set_led(state)
    return '{"state":"ledstate"}'

@app.route('/') 
def index():
    celsius = round(sense.temperature, 2)
    fahrenheit = round(1.8 * celsius + 32, 2)
    humidity = round(sense.humidity, 2)
    state=get_led()
    ledlight=state["ledlight"]
    ledcode=state["ledcode"]
    return render_template('status.html', celsius=celsius, fahrenheit=fahrenheit, humidity=humidity, ledlight=ledlight, ledcode=ledcode)

#Run API on port 5000, set debug to True
app.run(host='0.0.0.0', port=5000, debug=True)