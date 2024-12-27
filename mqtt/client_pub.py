#!/usr/bin/python3

import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import time
from env_data import get_environmental_data
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
        "28:FF:3C:8F:93:B1"   # ATV
    ]

# Publish a message to temp every 15 seconds
while True:
    msgFromClient = get_environmental_data(DEVICE_ID)
    mqttc.publish(f"{BASE_TOPIC}/environment",str(msgFromClient))
    time.sleep(15)
    devices_found=find_mac_addresses(target_macs, "192.168.8.0/24")
    mqttc.publish(f"{BASE_TOPIC}/devices/macs",str(devices_found))