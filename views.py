import web_pages

from machine import Pin
import time

def WEB_PAGE():

    # Replace the block of Interactions Only
    interaction_block = (
        '''
        <p><a href="/OPEN_DOOR"><button class="button">Open Door</button></a></p>
        '''
    )

    response = web_pages.index.format(block=interaction_block)

    return response

# Set up on GPIO 5 - D1
def OPEN_DOOR(*args, **kwargs):
    LED = Pin(14, Pin.OUT)
    DOOR = Pin(5, Pin.OUT)

    # Getting Reversed Settings
    DOOR_ON = DOOR.off
    DOOR_OFF = DOOR.on
    
    DOOR_ON()
    LED.on()
    time.sleep(1)
    DOOR_OFF()
    LED.off()