from sense_hat import SenseHat

sense = SenseHat()
pixel = sense.get_pixel(0, 0) #top_left_pixel
deviceID = "deviceID"

def get_led():
    #check top left pixel value(==0 - off, >0 - on) 
    # print(pixel) 

    if (pixel[0] >= 10 and pixel[1] == 0 and pixel[2] == 0):
        led = "RED"
        ledcode = "2"
        # return '{"state":"red"}'
    elif (pixel[0] == 0 and pixel[1] >= 10 and pixel[2] == 0):
        led = "GREEN"
        ledcode = "3"
        # return '{"state":"green"}'
    elif (pixel[0] == 0 and pixel[1] == 0 and pixel[2] >= 10):
        led = "BLUE"
        ledcode = "4"
        # return '{"state":"blue"}'
    elif (pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0):
        led = "OFF"
        ledcode = "0"
        # return '{"state":"off"}'
    elif (pixel[0] == pixel[1] == pixel[2] >= 10):
        led = "ON"
        ledcode = "1"
        # return '{"state":"on"}'
    else: 
        led = "OTHER"
        ledcode = "5"
        # return '{"state":"other"}'
    
    # Create a dictionary
    data = {
        "deviceID": deviceID,
        "led": led,
        "ledcode": ledcode
    }
    
    return data

# Allow standalone testing of this module
if __name__ == "__main__":
    # Example device ID and usage
    deviceID = "myDevice001"
    environmental_data = light_get(deviceID)
    # Print the data in JSON format for testing
    print(data)