import esp32
import urequests as re
from machine import Pin, deepsleep
from time import sleep
import network

wlan = network.WLAN()

def do_connect():
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        #wlan.config(('10.0.1.34', '255.255.255.0', '10.0.1.138', '10.0.1.138'))
        wlan.connect("wifiulasicky", 'zBNHKsw55d')
        while not wlan.isconnected():
            pass
    if wlan.isconnected():
        print('network config:', wlan.ifconfig())


btn = Pin(13, Pin.IN)
esp32.wake_on_ext0(pin = btn, level = esp32.WAKEUP_ANY_HIGH)

try:
    wlan.connect()
    print("first try")
except Exception as ex:
    print(ex)
    do_connect()

def send_play_request():
    URL = "http://10.0.1.35:5555/play"
    response = re.get(url=URL)
    print(response.text)

def send_stop_request():
    URL = "http://10.0.1.35:5555/stop"
    re.get(url=URL)
    
def get_state_request():
    URL = "http://10.0.1.35:5555/state"
    return re.get(url=URL).text

state = get_state_request()

if state == "playing":
    send_stop_request()
    print("stopping")
    state = "stopped"

elif state == "stopped":
    send_play_request()
    print("playing")
    state = "playing"

sleep(1)
deepsleep()
