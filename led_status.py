from sense_hat import SenseHat

sense = SenseHat()
pixel = sense.get_pixel(0, 0) #top_left_pixel
deviceID = "deviceID"
level = 10

def get_led():
    #check top left pixel value(==0 - off, >0 - on) 
    # print(pixel) 

    if (pixel[0] >= level and pixel[1] == 0 and pixel[2] == 0):
        ledlight = "RED"
        ledcode = "2"
        # return '{"state":"red"}'
    elif (pixel[0] == 0 and pixel[1] >= level and pixel[2] == 0):
        ledlight = "GREEN"
        ledcode = "3"
        # return '{"state":"green"}'
    elif (pixel[0] == 0 and pixel[1] == 0 and pixel[2] >= level):
        ledlight = "BLUE"
        ledcode = "4"
        # return '{"state":"blue"}'
    elif (pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0):
        ledlight = "OFF"
        ledcode = "0"
        # return '{"state":"off"}'
    elif (pixel[0] == pixel[1] == pixel[2] >= level):
        ledlight = "ON"
        ledcode = "1"
        # return '{"state":"on"}'
    else: 
        ledlight = "OTHER"
        ledcode = "5"
        # return '{"state":"other"}'
    
    # Create a dictionary
    data = {
        "deviceID": deviceID,
        "ledlight": ledlight,
        "ledcode": ledcode
    }
    
    return data


def set_led(state):

    if (state=="on"):
        sense.clear(level,level,level)
        return '{"state":"on"}'
    elif (state=="red"):
        sense.clear(level,0,0)
        return '{"state":"red"}'
    elif (state=="green"):
        sense.clear(0,level,0)
        return '{"state":"green"}'
    elif (state=="blue"):
        sense.clear(0,0,level)
        return '{"state":"blue"}'
    elif (state=="off"):
        sense.clear(0,0,0)
        return '{"state":"off"}'                
    else: 
        sense.clear(0,0,0)
        return '{"state":"off"}'
     



# Allow standalone testing of this module
if __name__ == "__main__":
    # Example device ID and usage
    deviceID = "myDevice001"
    environmental_data = light_get(deviceID)
    # Print the data in JSON format for testing
    print(data)