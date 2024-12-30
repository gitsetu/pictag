
import os 
import subprocess
import time
from led import *

def start():
    print("start")
    # Start the next files
    # os.system('python mqtt_client_pub.py') # Publishes to MQTT
    # os.system('python mqtt_client_sub.py') # Gets messages from MQTT
    # os.system('python thingspeak_http.py') # Sends data to ThingSpeak
    # os.system('python upload_image_button.py') # Starts camera
    # os.system('python blynk_image.py') # Starts Blynk server

    # Using system() method to execute shell commands
    subprocess.Popen('python mqtt_client_pub.py', shell=True) # Publishes to MQTT
    subprocess.Popen('python mqtt_client_sub.py', shell=True) # Gets messages from MQTT
    subprocess.Popen('python thingspeak_http.py', shell=True) # Sends data to ThingSpeak
    subprocess.Popen('python upload_image_button.py', shell=True) # Starts camera
    subprocess.Popen('python blynk_image.py', shell=True) # Starts Blynk server
    # subprocess.Popen('python presence_detector.py', shell=True) # Starts Blynk server



    # Web API starts on boot
    # os.system('python sense_api.py')


def led_test():
    print("led_test")
    set_led("white")
    time.sleep(2)
    set_led("red")
    time.sleep(2)
    set_led("green")
    time.sleep(2)
    set_led("blue")
    time.sleep(2)
    set_led("white")
    time.sleep(2)
    set_led("off")



# Allow standalone testing of this module
if __name__ == "__main__":
    led_test()
    start()
    # Print the data in JSON format for testing
    print("led_test")