from sense_hat import SenseHat

sense = SenseHat()
level = 10

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
    state = "red"
    set_sense_light = set_led(state)
    # Print the data in JSON format for testing
    print(set_sense_light)