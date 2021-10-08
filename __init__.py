from mycroft import MycroftSkill, intent_file_handler
import RPi.GPIO as GPIO

class Smarthome(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.OUT)

    @intent_file_handler('smarthome.lights.on.intent')
    def handle_smarthome_lights_on_intent(self, message):
        GPIO.output(17, GPIO.LOW)

    @intent_file_handler('smarthome.lights.off.intent')
    def handle_smarthome_lights_off_intent(self, message):
        GPIO.output(17, GPIO.HIGH)

def create_skill():
    return Smarthome()