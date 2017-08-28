#!/usr/bin/python
from flask import Flask, render_template, request, redirect
import os
import subprocess
import time

CAMERA = '/home/pi/pi-camera-recorder/camera.py'
LOCK = '/home/pi/pi-camera-recorder/camera.lock'
ALREADY_RECORDING = 'A recording has already started.'
LOCK_FAILURE = 'Recording requested, but no lock obtained. SSH.'


app = Flask(__name__)

@app.route('/')
def main():
  recording = False
  if os.path.isfile(LOCK):
    recording = True

  template_data = {'recording': recording, 'error': None}
  return render_template('main.html', **template_data)

@app.route('/record/<int:record_time>')
def action(record_time):
  if os.path.isfile(LOCK):
    template_data = {'recording': True, 'error': ALREADY_RECORDING}
    return render_template('main.html', **template_data)
  
  subprocess.Popen([CAMERA, str(record_time)])
  time.sleep(5)
  if os.path.isfile(LOCK):
    return redirect('/')
  
  template_data = {'recording': False, 'error': LOCK_FAILURE}
  return render_template('main.html', **template_data)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080, debug=True)
