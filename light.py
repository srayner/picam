import RPi.GPIO as GPIO

class Light(object):

    def __init__(self, pin = 8):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
        self.pin = pin
        self.status = "off"
        
    def __del__(self):
        GPIO.output(self.pin, GPIO.LOW)
        
    def toggle(self):
        if self.status == "off":
            GPIO.output(self.pin, GPIO.HIGH)
            self.status = "on"
        else:
            GPIO.output(self.pin, GPIO.LOW)
            self.status = "off"
        
        return {"status": self.status};
            
