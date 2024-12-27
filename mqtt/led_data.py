from sense_hat import SenseHat

def get_environmental_data(deviceID):
    # Initialize SenseHAT
    sense = SenseHat()
    
    # Retrieve temperature and humidity
    temp = sense.get_temperature()
    pixel = sense.get_pixel(0, 0) #top_left_pixel

    if (pixel[0] >= 10 and pixel[1] == 0 and pixel[2] == 0):
        led = "RED"
    elif (pixel[0] == 0 and pixel[1] >= 10 and pixel[2] == 0):
        led = "GREEN"
    elif (pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0):
        led = "OFF"
    elif (pixel[0] == pixel[1] == pixel[2] >= 10):
        led = "ON"
    else: 
        led = "OTHER"



    
    
    # Create a dictionary
    data = {
        "deviceID": deviceID,
        "temp": round(temp, 1),
        "led": led
    }
    
    return data

# Allow standalone testing of this module
if __name__ == "__main__":
    # Example device ID and usage
    deviceID = "myDevice001"
    environmental_data = get_environmental_data(deviceID)
    # Print the data in JSON format for testing
    print(environmental_data)