#!/usr/bin/python3

import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import time
from led import get_led
from presence_detector import find_mac_addresses


# parse mqtt url for connection details. DON'T FORGET TO UPDATE YOUR_ID TO A UNIQUE ID
URL = urlparse("mqtt://broker.emqx.io:1883/gitsetu/home")
BASE_TOPIC = URL.path[1:]
DEVICE_ID = "device1"

# MQTT event callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print(f"Connection failed with code {rc}")

def on_publish(client, userdata, mid):
    print(f"Message ID: {mid} published successfully")

def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT broker")
    if rc != 0:
        print("Unexpected disconnection. Reconnecting...")
        client.reconnect()

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish


# check if useame and password in the url (there isn't in this basic example)
if (URL.username):
    mqttc.username_pw_set(URL.username, URL.password)
# Connect
mqttc.connect(URL.hostname, URL.port)
mqttc.loop_start()

target_macs = [
        "7C:61:93:84:15:ED",  # htc
        # "2C:BE:08:4C:24:00",  # iphone
        # "28:FF:3C:8F:93:B1",  # ATV
        "74:38:B7:00:EF:7C"   # canon
    ]

# Publish a message to temp every 15 seconds
while True:
    # Read LED from Sense HAT
    led = get_led()
    ledlight = led["ledlight"]
    ledcode = led["ledcode"]
    msgFromClient = ledlight
    mqttc.publish(f"{BASE_TOPIC}/environment",str(msgFromClient))
    time.sleep(15)
    devices_found=find_mac_addresses(target_macs, "192.168.8.0/24")
    # devices_found=find_mac_addresses(len(target_macs), "192.168.8.0/24")
    if len(devices_found) > 0:
        mqttc.publish(f"{BASE_TOPIC}/devices/macs",str((len(devices_found))))
        time.sleep(15)