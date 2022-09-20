from app import app
import requests
import subprocess as sp

@app.route('/')
@app.route('/index')
def index():
    return "index"


@app.route('/play')
def play():
    sp.call(["sh", "./wake_up.sh"])
    url = "http://127.0.0.1:8080/requests/status.xml?command=in_play&input=/Users/honzak/Downloads/video.mp4"
    headers = {
    'Authorization': 'Basic OjIzMzcy',
    'Content-Type': 'text/plain'
    }
    response = requests.request("GET", url, headers=headers, data=None)
    return response.text


@app.route('/stop')
def stop():
    url = "http://127.0.0.1:8080/requests/status.xml?command=pl_empty"
    headers = {
    'Authorization': 'Basic OjIzMzcy'
    }
    response = requests.request("GET", url, headers=headers, data=None)
    return "stop video"


@app.route("/state")
def state():
    url = "http://127.0.0.1:8080/requests/status.json"
    headers = {
    'Authorization': 'Basic OjIzMzcy'
    }
    response = requests.get(url, headers=headers, data=None)
    state = response.json()["state"]
    return state
