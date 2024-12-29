from sense_hat import SenseHat



def get_environmental_data(deviceID):
    # Initialize SenseHAT
    sense = SenseHat()
    
    # Retrieve temperature and humidity
    temp = sense.get_temperature()

    # Retrieve LED
    state=get_led()
    ledlight=state["ledlight"]
    ledcode=state["ledcode"]
    
    # Create a dictionary
    data = {
        "deviceID": deviceID,
        "temp": round(temp, 1),
        "ledlight": ledlight,
        "ledcode": ledcode
    }
    
    return data

# Allow standalone testing of this module
if __name__ == "__main__":
    # Example device ID and usage
    deviceID = "myDevice001"
    environmental_data = get_environmental_data(deviceID)
    # Print the data in JSON format for testing
    print(environmental_data)