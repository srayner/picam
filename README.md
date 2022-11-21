# Pi-Cam

Raspberry-Pi camera steaming server.

## How it works
The Pi streams the output of the camera module over
the web via Flask. Devices connected to the same
network can access the camera stream via a web browser.
The web browser can also send commands to the Flask server
instructing to take a still photograph or turn the light
on or off.

```
<picam:5000>
```

## Supported models

* should run on any Raspberry-Pi
* tested on Raspberry-Pi B+ (2014) @900MHz

## Installation Instructions
Install the following dependencies.

```
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev
sudo apt-get install libqtgui4
sudo apt-get install libqt4-test
sudo apt-get install libhdf5-dev

sudo pip3 install flask
sudo pip3 install numpy
sudo pip3 install imutils

sudo apt-get install python3-opencv

```

## Step 1 – Clone this git repo:

```
cd /home/pi
git clone https://github.com/srayner/picam.git
```

## Step 2 – Launch Web Stream

```
sudo python3 /home/pi/picam/main.py
```

## Step 3 – Post Installation

A good idea is to make the the camera stream auto
start at bootup of your pi. You will now not need
to re-run the script every time you want to create
the stream.
1. Open the /etc/profile for editing:

```
sudo nano /etc/profile
```

2. Go the end of the and add the following (from above):

```
sudo python3 /home/pi/picam/main.py
```

This would cause the following terminal command to auto-start each time the Raspberry Pi boots up. This in effect creates a headless setup - which would be accessed via SSH.
Note: make sure SSH is enabled.

