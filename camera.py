#!/usr/bin/python

import os
import picamera
import sys
import time

LOCK='/home/pi/pi-camera-recorder/camera.lock'
DEFAULT=5

if os.path.isfile(LOCK):
  print 'Not running, camera is in use'
  sys.exit(1)

if len(sys.argv) != 2:
  record_seconds=DEFAULT
else:
  record_seconds=int(sys.argv[1])
print 'Setting record seconds to: %s' % record_seconds

with picamera.PiCamera() as camera:
  try:
    open(LOCK, 'a').close()
    camera.framerate = 30
    camera.resolution = (1920,1080)
    camera.start_recording(
        time.strftime('recordings/%Y-%m-%d-%H-%M-%S.h264', time.localtime()))
    camera.wait_recording(record_seconds)
  finally:
    camera.stop_recording()
    os.remove(LOCK)
