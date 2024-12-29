#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_cors import CORS
from sense_hat import SenseHat
from led_status import get_led
from set_led import set_led
from upload_image import upload_image

sense = SenseHat()
deviceID="device1"
#clear sensehat and intialise light_state
sense.clear()
sense.low_light = True
level = 10

#create Flask app instance and apply CORS
app = Flask(__name__)
CORS(app)

@app.route('/sensehat/environment',methods=['GET'])
def current_environment():
    temperature=round(sense.temperature,2)
    msg = {"deviceID": deviceID,"temp":temperature}
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

@app.route('/image/tag',methods=['POST'])
def tag_post():
    tag=request.args.get('tag')
    print (tag)
    sense.show_message("tag", text_colour=[0, level, 0])
    return '{"tag":"tag"}'    

@app.route('/camera',methods=['POST'])
def takephoto_post():
    takephoto=request.args.get('takephoto')
    print (takephoto)
    upload_image("../images/sensehat_image.jpg")
    sense.show_message("taking photo", text_colour=[level, 0, 0])
    return '{"takephoto":"takephoto"}' 

@app.route('/') 
def index():
    celsius = round(sense.temperature, 2)
    state=get_led()
    ledlight=state["ledlight"]
    ledcode=state["ledcode"]
    return render_template('status.html', celsius=celsius, ledlight=ledlight, ledcode=ledcode)

#Run API on port 5000, set debug to True
app.run(host='0.0.0.0', port=5000, debug=True)