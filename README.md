# pi-camera-recorder
Pi camera recording web interface.

This presents a restful interface to trigger pi camera recordings.

Install Instructions
--------------------
1. Login raspberry pi, install dependencies and clone code

```bash
sudo apt install python-picamera python3-picamera python-picamera-docs python-dev python-imaging python-pip python-flask  flask
git clone https://github.com/r-pufky/pi-camera-recorder
```

2. [Ensure camera port is enabled](https://www.raspberrypi.org/documentation/configuration/camera.md)
* Select Camera -> Enable
```bash
sudo raspi-config
```

Usage:
------
Run recorder.py and access interface via http://localhost:8080. Recordings will be saved to recordings/.

This should probably be turned into a service if used more more than a demo.
