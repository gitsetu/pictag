#!/usr/bin/python3

from flask import Flask, request, render_template
from flask_cors import CORS
from sense_hat import SenseHat
from led import *
from capture_image import capture_image
from upload_image import upload_image
import os
import time


sense = SenseHat()
deviceID="pi"
#clear sensehat and intialise light_state
sense.clear()
sense.low_light = True
level = 10

IMAGE_PATH="../images/sensehat_image.jpg"

TAGGED_IMAGE_PATH="tagged_images/"

TIMESTAMP = time.time()
JPG_EXT=".jpg"
SEPARATOR="_"

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
    print (ledstate)
    set_led(ledstate)
    # return '{"state":"ledstate"}'
    return render_template('status.html', ledlight=ledlight, ledcode=ledcode)

@app.route('/tag',methods=['POST'])
def tag_post():
    textField=request.args.get('textField')
    print (textField)
    sense.show_message("textField", text_colour=blue)

    TAGGED_IMAGE_COMPLETE_PATH=f"{TAGGED_IMAGE_PATH}{TIMESTAMP}{SEPARATOR}{textField}{JPG_EXT}"

    os.rename('IMAGE_PATH', 'TAGGED_IMAGE_COMPLETE_PATH')
    # return '{"tag":"tag"}' 
    return render_template('status.html')   

@app.route('/camera',methods=['POST'])
def takephoto_post():
    takephoto=request.args.get('takephoto')
    print (takephoto)
    capture_image(IMAGE_PATH)
    upload_image(IMAGE_PATH)
    sense.show_message("photo taken", text_colour=blue)
    # return '{"takephoto":"takephoto"}' 
    return render_template('status.html')

@app.route('/') 
def index():
    celsius = round(sense.temperature, 2)
    state=get_led()
    ledlight=state["ledlight"]
    ledcode=state["ledcode"]
    return render_template('status.html', celsius=celsius, ledlight=ledlight, ledcode=ledcode)

#Run API on port 5000, set debug to True
app.run(host='0.0.0.0', port=5000, debug=True)