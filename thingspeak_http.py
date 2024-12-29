from sense_hat import SenseHat
import requests
import time
from led import get_led

sense = SenseHat()
deviceID = "deviceID"

# ThingSpeak settings
THINGSPEAK_WRITE_API_KEY = "BG5IVC2YU8GS7I5M"
THINGSPEAK_CHANNEL_URL = "https://api.thingspeak.com/update"

# Function to send data to ThingSpeak
def send_to_thingspeak(temperature,state):
    payload = {
        'api_key': THINGSPEAK_WRITE_API_KEY,
        'field1': temperature,
        'field2': led_status["ledcode"]
    }
  
    response = requests.get(THINGSPEAK_CHANNEL_URL, params=payload)

    if response.status_code == 200:
        print("Data sent to ThingSpeak.")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")
   

while True:
    # Read temperature and humidity from Sense HAT
    temperature = round(sense.get_temperature(),2)

    led_status = get_led()
    ledlight = led_status["ledlight"]
    ledcode = led_status["ledcode"]

    print(f"Temperature: {temperature} C, Light: {ledlight}")

    # print(led_status["ledcode"])

    # Send the data to ThingSpeak
    send_to_thingspeak(temperature,ledcode)

    # Wait before the next reading (ThingSpeak recommends 15-second intervals for free accounts)
    time.sleep(15)