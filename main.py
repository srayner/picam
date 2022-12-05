#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory
from camera import VideoCamera
from light import Light
import os
import glob

pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.
light = Light()

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def get_status():
    '''this could be any function that blocks until data is ready'''
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

@app.route('/status')
def status_stream():
    def event():
        while True:
            # wait for source data to be available, then push it
            yield 'data: {}\n\n'.format(get_status())
    return Response(event(), mimetype="text/event-stream")

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# Take a photo when pressing camera button
@app.route('/picture')
def take_picture():
    pi_camera.take_picture()
    return "None"
    
# Toggle light
@app.route('/toggle-light')
def toggle_light():
    return light.toggle()

# List photos
@app.route('/pictures')
def list_pictures():
    return {"pictures": glob.glob('*.jpg')}

if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
