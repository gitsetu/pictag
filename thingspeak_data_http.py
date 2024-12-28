from sense_hat import SenseHat
import requests
import time
from led_status import get_led
from presence_detector import find_mac_addresses

sense = SenseHat()
deviceID = "deviceID"

target_macs = [
        "28:FF:3C:8F:93:B1",  # ATV
        "7C:61:93:84:15:ED"   # htc
    ]

# ThingSpeak settings
THINGSPEAK_WRITE_API_KEY = "BG5IVC2YU8GS7I5M"
THINGSPEAK_CHANNEL_URL = "https://api.thingspeak.com/update"

# Function to send data to ThingSpeak
def send_to_thingspeak(temperature,state,pressence):
    payload = {
        'api_key': THINGSPEAK_WRITE_API_KEY,
        'field1': temperature,
        'field2': led_status["ledcode"],
        'field3': pressence
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
    led = led_status["led"]
    ledcode = led_status["ledcode"]

    devices_found = find_mac_addresses(target_macs, "192.168.8.0/24")
    # devices_found=find_mac_addresses(len(target_macs), "192.168.8.0/24")
    pressence=len(devices_found)

    print(f"Temperature: {temperature} C, Light: {led} ")
    # print(led_status["ledcode"])

    # Send the data to ThingSpeak
    send_to_thingspeak(temperature,ledcode,pressence)

    # Wait before the next reading (ThingSpeak recommends 15-second intervals for free accounts)
    time.sleep(15)