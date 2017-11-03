from data import Data
from server import app
from flask import request
from threading import Thread, Event
import json,requests
import datetime

queue = []

@app.route('/sensor', methods=['POST'])
def sensor_register():
    pass

@app.route('/sound_data', methods=['POST'])
def recv_data():
    global queue
    db = request.get('dB')
    id = request.get('id')
    photo = request.get('photo')

    data = Data(db, id, photo)

    ctime = datetime.datetime.now()
    data['time'] = ctime
    queue.append(data)

def send_queue_data():
    global queue
    if len(queue) < 15: return

    data = queue[:15]
    url = ''
    resp = requests.post(url=url,params=data)
    data = json.loads(resp.text)

def routine_start():
    stopFlag = Event()
    thread = TimerThread(stopFlag, 3600)
    thread.start()

class TimerThread(Thread):
    def __init__(self, event, interval):
        Thread.__init__(self)
        self.stoped = event
        self.interval = interval
    def run(self):
        while not self.stopped.wait(self.interval):
            send_queue_data()

