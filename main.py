import wifimgr
import urequests as re
from machine import Pin
from time import sleep

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
#    while True:
#        pass  # you shall not pass :D


# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")


def send_play_request():
    URL = "http://10.255.254.146:5000/play"
    response = re.get(url=URL)
    print(response.text)

def send_stop_request():
    URL = "http://10.255.254.146:5000/stop"
    re.get(url=URL)
    
def get_state_request():
    URL = "http://10.255.254.146:5000/state"
    return re.get(url=URL).text
    
btn = Pin(13, Pin.IN)
on = True

while True:
    if btn.value() == 0:
        on = False
        pass
    if btn.value() == 1 and on == False:
        on = True
        state = get_state_request()
        if state == "playing":
            send_stop_request()
        elif state == "stopped":
            send_play_request()
        else:
            pass
